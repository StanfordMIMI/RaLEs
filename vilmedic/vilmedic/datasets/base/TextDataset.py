import os
import tqdm
import json
import sys

from torch.utils.data import Dataset
from transformers import AutoTokenizer
from transformers import BertTokenizer
from .utils import Vocab, load_file

import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="darkgrid")
os.environ["TOKENIZERS_PARALLELISM"] = "false"  # https://github.com/huggingface/transformers/issues/5486


def split_sentences(sentences):
    return [s.strip().split() for s in sentences]


def make_sentences(root, split, file):
    sentences = load_file(os.path.join(root, split + '.' + file))
    return split_sentences(sentences)


class TextDataset(Dataset):
    def __init__(self,
                 root=None,
                 file=None,
                 split=None,
                 ckpt_dir=None,
                 tokenizer=None,
                 tokenizer_max_len=None,
                 show_length=False,
                 vocab_file=None,
                 source='src',
                 max_len=250,
                 **kwargs):

        assert source in ["src", "tgt"]
        assert split is not None, "Argument split cant be None"
        assert not (file is not None and vocab_file is not None), "You cant mention both a data file and a vocab file"

        self.root = root
        self.file = file
        self.split = split
        self.source = source
        self.ckpt_dir = ckpt_dir
        self.max_len = max_len
        self.tokenizer_max_len = tokenizer_max_len
        self.vocab_file = vocab_file
        self.sentences = None

        if file is not None:
            self.sentences = make_sentences(root, split, file)

        # Create tokenizer from pretrained or vocabulary file
        if tokenizer is not None:
            self.tokenizer = AutoTokenizer.from_pretrained(tokenizer)
        else:
            if vocab_file is None:
                vocab_file = os.path.join(ckpt_dir, 'vocab.{}'.format(source))
                if split == 'train':
                    vocab = Vocab(self.sentences)
                    if not os.path.exists(vocab_file):
                        vocab.dump(vocab_file)
            self.tokenizer = BertTokenizer(vocab_file=vocab_file,
                                           do_basic_tokenize=False)

        # Create tokenizer forwards args
        self.tokenizer_args = {'return_tensors': 'pt', 'padding': True, 'add_special_tokens': True}
        if self.source == 'src':
            self.tokenizer_args.update({'add_special_tokens': False})
        if self.tokenizer_max_len is not None:
            self.tokenizer_args.update({'padding': 'max_length',
                                        'truncation': True,
                                        'max_length': self.tokenizer_max_len})

        if show_length:
            self.show_length()
            sys.exit()

    def __getitem__(self, index):
        # No trunc at test time
        return {'seq': ' '.join(self.sentences[index][:self.max_len]) if (
                self.split == 'train' and self.source == "tgt") else ' '.join(self.sentences[index])}

    def get_collate_fn(self):
        def collate_fn(batch):
            seq = self.tokenizer([s['seq'] for s in batch], **self.tokenizer_args)
            collated = {
                'input_ids': seq.input_ids,
                'attention_mask': seq.attention_mask
            }
            return collated

        return collate_fn

    def __len__(self):
        return len(self.sentences or [])

    def inference(self, sentences):
        if not isinstance(sentences, list):
            sentences = [sentences]
        return [{'seq': s} for s in sentences]

    def show_length(self):
        print("Plotting sequences length...")
        sentence_len, tokenizer_len = [], []
        self.tokenizer_args.update({'max_length': 512})
        for index in tqdm.tqdm(range(len(self))):
            sentence = self.__getitem__(index)['seq']
            x = self.tokenizer(sentence, **self.tokenizer_args).input_ids[0]
            if self.tokenizer.sep_token_id in x:
                length = ((x == self.tokenizer.sep_token_id).nonzero(as_tuple=True)[0]).item()
            elif self.tokenizer.pad_token_id in x:
                length = ((x == self.tokenizer.pad_token_id).nonzero(as_tuple=True)[0][0]).item()
            else:
                length = len(x)
            tokenizer_len.append(length)
            sentence_len.append(len(sentence.split()))

        _, ax = plt.subplots(1, 2)
        sns.histplot(tokenizer_len, ax=ax[0], binwidth=2)
        sns.histplot(sentence_len, ax=ax[1], binwidth=2)
        ax[0].set_title("tokenizer_len")
        ax[1].set_title("sentence_len")
        plt.show()

    def __repr__(self):
        return "TextDataset\n" + \
               json.dumps({"source": self.source,
                           "root": self.root,
                           "file": self.file,
                           "max_len": self.max_len,
                           "Tokenizer": {
                               "name_or_path": self.tokenizer.name_or_path,
                               "vocab_size": self.tokenizer.vocab_size,
                               "tokenizer_args": self.tokenizer_args,
                               "special_tokens": self.tokenizer.special_tokens_map_extended,
                               "bos_token_id": self.tokenizer.bos_token,
                               # "eos_token_id": self.tokenizer.vocab[self.tokenizer.eos_token],
                               # "pad_token_id": self.tokenizer.vocab[self.tokenizer.pad_token],
                           }}, indent=4,
                          sort_keys=False, default=str)
