import torch.nn as nn
import copy
import functools

# v4.3.2
from transformers.models.auto import AutoModelForCausalLM, AutoConfig
from transformers.models.bert_generation import BertGenerationEncoder, BertGenerationConfig, BertGenerationDecoder
from transformers import EncoderDecoderModel as HFEncoderDecoderModel
from vilmedic.networks.models.utils import get_n_params
from vilmedic.networks.blocks.huggingface.decoder.beam_search import beam_search


class DecoderModel(nn.Module):
    """
    If proto is mentioned in encoder and decoder dict, loads pretrained models from proto strings.
    Otherwise, loads a BertGenerationEncoder/BertGenerationDecoder model from encoder and decoder dict.
    """

    def __init__(self, decoder, **kwargs):
        super().__init__()
        if 'proto' in decoder:
            path = decoder.pop('proto')
            dec_config = AutoConfig.from_pretrained(path)
            dec_config.is_decoder = True
            dec_config.add_cross_attention = True
            self.decoder = AutoModelForCausalLM.from_pretrained(path, config=dec_config)
        else:
            dec_config = BertGenerationConfig(**decoder)
            dec_config.is_decoder = True
            dec_config.add_cross_attention = True
            self.decoder = BertGenerationDecoder(dec_config)

        # Evaluation
        self.decoder.beam_search = functools.partial(beam_search, self.decoder)

    def forward(self, input_ids, attention_mask, encoder_outputs=None, encoder_attention_mask=None, **kwargs):
        input_ids = input_ids.cuda()
        attention_mask = attention_mask.cuda()
        out = self.decoder(input_ids=input_ids,
                           attention_mask=attention_mask,
                           encoder_hidden_states=encoder_outputs,
                           encoder_attention_mask=encoder_attention_mask,
                           labels=input_ids,
                           **kwargs)
        out = vars(out)
        return out

    def __repr__(self):
        s = str(type(self.decoder).__name__) + '(' + str(self.decoder.config) + ')\n'
        return s
