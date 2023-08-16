"""
adapted from vilmedic https://github.com/jbdel/vilmedic/blob/main/vilmedic/blocks/scorers/NLG/bertscore/bertscore.py
"""


import os
import torch
import time
import numpy as np
import torch.nn as nn
from torchmetrics.text.bert import BERTScore


class BertScore(nn.Module):
    def __init__(self):
        super(BertScore, self).__init__()
        with torch.no_grad():
            self.bert_scorer = BERTScore(model_name_or_path='distilbert-base-uncased',
                                          num_layers=5,
                                          batch_size=64,
                                          num_threads=1,
                                          all_layers=False,
                                          idf=False,
                                          device='cuda' if torch.cuda.is_available() else 'cpu',
                                          lang='en',
                                          rescale_with_baseline=True,
                                          baseline_path=None)

    def forward(self, refs, hyps):
        scores= self.bert_scorer(
            preds=hyps,
            target=refs
        )
        return torch.mean(scores["f1"]).item(), scores["f1"].tolist()