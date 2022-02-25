import torch
import torch.nn as nn
from vilmedic.models.utils import get_n_params

from vilmedic.blocks.vision import *
from vilmedic.blocks.huggingface.encoder.encoder_model import EncoderModel
from vilmedic.blocks.losses import GLoRIALoss, gloria_attention_fn, cosine_similarity

from tqdm import tqdm
import numpy as np
from sklearn import metrics


def evaluation(models, config, dl, from_training, **kwargs):
    # No ensembling for this evaluation
    model = models[0]

    losses = []
    linguistics = []
    visuals = []

    pbar = tqdm(dl, total=len(dl))
    for i, batch in enumerate(pbar):
        batch = {k: v.cuda() for k, v in batch.items()}
        out = model(**batch)
        losses.append(out['loss'].mean().cpu().data.numpy())

        if not from_training:
            linguistics.append(out['sent_embeddings'].cpu().data)
            visuals.append(out['global_features'].cpu().data)

    if from_training:
        return {'loss': np.ndarray.mean(np.array(losses))}

    return {'loss': np.ndarray.mean(np.array(losses)),
            'linguistic': torch.cat(linguistics),
            'visual': torch.cat(visuals)
            }


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


class GLoRIA(nn.Module):

    def __init__(self, encoder, cnn, visual_embedder, loss, dl, forward_batch_size=12, **kwargs):
        super().__init__()

        # Linguistic encoder
        self.linguistic = EncoderModel(encoder)
        self.last_n_layers = encoder.last_n_layers
        self.idxtoword = {v: k for k, v in dl.dataset.tokenizer.get_vocab().items()}

        # Visual Encoder
        self.visual = eval(cnn.pop('proto'))(**cnn)
        self.global_embedder = nn.Linear(visual_embedder.feature_dim, self.linguistic.encoder.config.hidden_size)
        self.local_embedder = nn.Conv2d(visual_embedder.interm_feature_dim,
                                        self.linguistic.encoder.config.hidden_size,
                                        kernel_size=1,
                                        stride=1,
                                        padding=0,
                                        bias=False)
        self.up_sample = nn.Upsample(size=(299, 299), mode="bilinear", align_corners=True)
        # Loss
        self.loss_fn = GLoRIALoss(**loss)

        # Hook
        self.activation = {}

        def getActivation(name):
            def hook(model, input, output):
                self.activation[name] = output

            return hook

        self.visual.cnn[6].register_forward_hook(getActivation('local_features'))  # corresponds to the ouput of layer3

        # Evaluation
        self.eval_func = evaluation
        self.fbs = forward_batch_size

    def forward(self, input_ids, attention_mask, images, **kwargs):
        bs = images.shape[0]
        global_features = []
        local_features = []
        hidden_states = []

        # Forward passes
        for i in list(chunks(range(bs), min(self.fbs, bs))):
            input_ids_ = input_ids[i]
            attention_mask_ = attention_mask[i]
            images_ = images[i]

            global_features.append(self.global_embedder(self.visual(self.up_sample(images_.cuda()))))
            local_features.append(self.local_embedder(self.activation["local_features"]))
            output = self.linguistic(input_ids_.cuda(),
                                     attention_mask_.cuda(),
                                     output_hidden_states=True)
            hidden_states.append(torch.stack(output["hidden_states"]))

        global_features = torch.cat(global_features)
        local_features = torch.cat(local_features)
        hidden_states = torch.cat(hidden_states, dim=1)

        # Aggregate Token embeddings
        embeddings = hidden_states[-self.last_n_layers:]
        embeddings, sents = self.aggregate_tokens(embeddings, input_ids)

        # Linguistic local and global embeddings
        sent_embeddings = torch.sum(torch.mean(embeddings, dim=2), dim=1)
        word_embeddings = torch.sum(embeddings, dim=1)
        word_embeddings = word_embeddings.permute(0, 2, 1)

        # Losses
        loss, attention_maps = self.loss_fn(global_features, local_features, word_embeddings, sent_embeddings, sents)

        return {"loss": loss, "global_features": global_features, "local_features": local_features,
                "word_embeddings": word_embeddings, "sent_embeddings": sent_embeddings}

    def aggregate_tokens(self, embeddings, input_ids):
        num_layers, batch_size, num_words, dim = embeddings.shape
        embeddings = embeddings.permute(1, 2, 0, 3)

        agg_embs_batch = []
        sentences = []

        # loop over batch
        for embs, caption_id in zip(embeddings, input_ids):

            agg_embs = []
            token_bank = []
            words = []
            word_bank = []

            # loop over sentence
            for word_emb, word_id in zip(embs, caption_id):

                word = self.idxtoword[word_id.item()]

                if word == "[SEP]":
                    new_emb = torch.stack(token_bank)
                    new_emb = new_emb.sum(axis=0)
                    agg_embs.append(new_emb)
                    words.append("".join(word_bank))

                    agg_embs.append(word_emb)
                    words.append(word)
                    break

                if not word.startswith("##"):
                    if len(word_bank) == 0:
                        token_bank.append(word_emb)
                        word_bank.append(word)
                    else:
                        new_emb = torch.stack(token_bank)
                        new_emb = new_emb.sum(axis=0)
                        agg_embs.append(new_emb)
                        words.append("".join(word_bank))

                        token_bank = [word_emb]
                        word_bank = [word]
                else:
                    if word.startswith("##"):
                        token_bank.append(word_emb)
                        word_bank.append(word[2:])

            agg_embs = torch.stack(agg_embs)
            padding_size = num_words - len(agg_embs)
            paddings = torch.zeros(padding_size, num_layers, dim)
            paddings = paddings.to(agg_embs.device)
            words = words + ["[PAD]"] * padding_size

            agg_embs_batch.append(torch.cat([agg_embs, paddings]))
            sentences.append(words)

        agg_embs_batch = torch.stack(agg_embs_batch)
        agg_embs_batch = agg_embs_batch.permute(0, 2, 1, 3)
        return agg_embs_batch, sentences

    def zero_shot_classification(self, input_ids, attention_mask, images):

        # get similarities for each class
        similarities = self.get_similarities(
            input_ids, attention_mask, images, similarity_type="both"
        )
        class_similarities = similarities.max(axis=1)  # average between class prompts
        return class_similarities

    def get_similarities(self, input_ids, attention_mask, images, similarity_type="both"):

        # warnings
        if similarity_type not in ["global", "local", "both"]:
            raise RuntimeError(
                f"similarity type should be one of ['global', 'local', 'both']"
            )

        cap_lens = [len([t for t in i if t != 0]) for i in input_ids]

        # get global and local image features
        with torch.no_grad():
            out = self(input_ids, attention_mask, images)

        img_emb_g, img_emb_l, text_emb_l, text_emb_g = out["global_features"], out["local_features"], out[
            "word_embeddings"], out["sent_embeddings"]

        # get similarities
        global_similarities = self.get_global_similarities(img_emb_g, text_emb_g)
        local_similarities = self.get_local_similarities(
            img_emb_l, text_emb_l, cap_lens
        )
        similarities = (local_similarities + global_similarities) / 2

        if similarity_type == "global":
            return global_similarities.detach().cpu().numpy()
        elif similarity_type == "local":
            return local_similarities.detach().cpu().numpy()
        else:
            return similarities.detach().cpu().numpy()

    def get_global_similarities(self, img_emb_g, text_emb_g):
        img_emb_g = img_emb_g.detach().cpu().numpy()
        text_emb_g = text_emb_g.detach().cpu().numpy()
        global_similarities = metrics.pairwise.cosine_similarity(img_emb_g, text_emb_g)
        global_similarities = torch.tensor(global_similarities)
        return global_similarities

    def get_local_similarities(self, img_emb_l, text_emb_l, cap_lens):

        batch_size = img_emb_l.shape[0]
        similarities = []

        for i in range(len(text_emb_l)):
            words_num = cap_lens[i]
            word = (
                text_emb_l[i, :, 1: words_num + 1].unsqueeze(0).contiguous()
            )  # [1, 768, 25]

            word = word.repeat(batch_size, 1, 1)  # [48, 768, 25]
            context = img_emb_l  # [48, 768, 19, 19]

            weiContext, attn = gloria_attention_fn(
                word, context, 4.0
            )  # [48, 768, 25], [48, 25, 19, 19]

            word = word.transpose(1, 2).contiguous()  # [48, 25, 768]
            weiContext = weiContext.transpose(1, 2).contiguous()  # [48, 25, 768]

            word = word.view(batch_size * words_num, -1)  # [1200, 768]
            weiContext = weiContext.view(batch_size * words_num, -1)  # [1200, 768]
            #
            row_sim = cosine_similarity(word, weiContext)
            row_sim = row_sim.view(batch_size, words_num)  # [48, 25]

            row_sim.mul_(5.0).exp_()
            row_sim, max_row_idx = torch.max(row_sim, dim=1, keepdim=True)  # [48, 1]

            row_sim = torch.log(row_sim)

            similarities.append(row_sim)

        local_similarities = torch.cat(similarities, 1).detach().cpu()

        return local_similarities

    def __repr__(self):
        s = super().__repr__() + '\n'
        s += "{}\n".format(get_n_params(self))
        return s
