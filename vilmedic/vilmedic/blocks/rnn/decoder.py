# -*- coding: utf-8 -*-
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable

from .layers.ff import FF
from .layers.attention import Attention


def get_rnn_hidden_state(h):
    """Returns h_t transparently regardless of RNN type."""
    return h if not isinstance(h, tuple) else h[0]


class ConditionalDecoder(nn.Module):
    """A conditional decoder with attention à la dl4mt-tutorial."""

    def __init__(self, input_size, hidden_size, n_vocab, rnn_type,
                 encoder_size=200, tied_emb=False,
                 dec_init='zero', dec_init_activ='tanh', dec_init_size=None,
                 att_type='mlp', att_activ='tanh', att_bottleneck='ctx', att_temp=1.0,
                 transform_ctx=True, mlp_bias=False, dropout_out=0, **kwargs):
        super().__init__()

        # Normalize case
        self.rnn_type = rnn_type.upper()

        # Safety checks
        assert self.rnn_type in ('GRU', 'LSTM'), \
            "rnn_type '{}' not known".format(rnn_type)
        assert dec_init in ('zero', 'mean_ctx', 'feats'), \
            "dec_init '{}' not known".format(dec_init)

        RNN = getattr(nn, '{}Cell'.format(self.rnn_type))
        # LSTMs have also the cell state
        self.n_states = 1 if self.rnn_type == 'GRU' else 2

        # Set custom handlers for GRU/LSTM
        if self.rnn_type == 'GRU':
            self._rnn_unpack_states = lambda x: x
            self._rnn_pack_states = lambda x: x
        elif self.rnn_type == 'LSTM':
            self._rnn_unpack_states = self._lstm_unpack_states
            self._rnn_pack_states = self._lstm_pack_states

        # Other arguments
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.encoder_size = encoder_size
        self.n_vocab = n_vocab
        self.tied_emb = tied_emb
        self.dec_init = dec_init
        self.dec_init_size = dec_init_size
        self.dec_init_activ = dec_init_activ
        self.att_type = att_type
        self.att_bottleneck = att_bottleneck
        self.att_activ = att_activ
        self.att_temp = att_temp
        self.transform_ctx = transform_ctx
        self.mlp_bias = mlp_bias
        self.dropout_out = dropout_out

        # Create target embeddings
        self.emb = nn.Embedding(self.n_vocab, self.input_size,
                                padding_idx=0)

        # Create attention layer
        self.att = Attention(self.encoder_size, self.hidden_size,
                             transform_ctx=self.transform_ctx,
                             mlp_bias=self.mlp_bias,
                             att_type=self.att_type,
                             att_activ=self.att_activ,
                             att_bottleneck=self.att_bottleneck,
                             temp=self.att_temp)

        # Decoder initializer FF (for 'mean_ctx' or auxiliary 'feats')
        if self.dec_init in ('mean_ctx', 'feats'):
            if self.dec_init == 'mean_ctx':
                self.dec_init_size = self.encoder_size
            self.ff_dec_init = FF(
                self.dec_init_size,
                self.hidden_size * self.n_states, activ=self.dec_init_activ)

        # Create first decoder layer necessary for attention
        self.dec0 = RNN(self.input_size, self.hidden_size)
        self.dec1 = RNN(self.hidden_size, self.hidden_size)

        # Output dropout
        if self.dropout_out > 0:
            self.do_out = nn.Dropout(p=self.dropout_out)

        # Output bottleneck: maps hidden states to target emb dim
        self.hid2out = FF(self.hidden_size, self.input_size,
                          bias_zero=True, activ='tanh')

        # Final softmax
        self.out2prob = FF(self.input_size, self.n_vocab)

        # Tie input embedding matrix and output embedding matrix
        if self.tied_emb:
            self.out2prob.weight = self.emb.weight

        self.nll_loss = nn.NLLLoss(reduction="sum", ignore_index=0)

    def _lstm_pack_states(self, h):
        return torch.cat(h, dim=-1)

    def _lstm_unpack_states(self, h):
        # Split h_t and c_t into two tensors and return a tuple
        return torch.split(h, self.hidden_size, dim=-1)

    def f_init(self, ctx_dict):
        """Returns the initial h_0 for the decoder."""
        if self.dec_init == 'zero':
            ctx, _ = ctx_dict['enc']
            h_0 = torch.zeros(ctx.shape[1], self.hidden_size * self.n_states)
            return Variable(h_0).cuda()
        elif self.dec_init == 'mean_ctx':
            ctx, ctx_mask = ctx_dict['enc']
            if ctx_mask is None:
                return self.ff_dec_init(ctx.mean(0))
            else:
                return self.ff_dec_init(ctx.sum(0) / ctx_mask.sum(0).unsqueeze(1))
        elif self.dec_init == 'feats':
            ctx, _ = ctx_dict['feats']
            return self.ff_dec_init(ctx.squeeze(0))
        else:
            raise NotImplementedError(self.dec_init)

    def f_next(self, ctx_dict, y, h):
        # Get hidden states from the first decoder (purely cond. on LM)
        h1_c1 = self.dec0(y, self._rnn_unpack_states(h))
        h1 = get_rnn_hidden_state(h1_c1)

        # Apply attention
        self.txt_alpha_t, txt_z_t = self.att(
            h1.unsqueeze(0), *ctx_dict['enc'])

        # Run second decoder (h1 is compatible now as it was returned by GRU)
        h2_c2 = self.dec1(txt_z_t, h1_c1)
        h2 = get_rnn_hidden_state(h2_c2)

        # This is a bottleneck to avoid going from H to V directly
        logit = self.hid2out(h2)

        # Apply dropout if any
        if self.dropout_out > 0:
            logit = self.do_out(logit)

        # Transform logit to T*B*V (V: vocab_size)
        # Compute log_softmax over token dim
        log_p = F.log_softmax(self.out2prob(logit), dim=-1)

        # Return log probs and new hidden states
        return log_p, self._rnn_pack_states(h2_c2)

    def forward(self, ctx_dict, y):
        """Computes the softmax outputs given source annotations `ctxs` and
        ground-truth target token indices `y`. Only called during training.

        Arguments:
            ctxs(Variable): A variable of `S*B*ctx_dim` representing the source
                annotations in an order compatible with ground-truth targets.
            y(Variable): A variable of `T*B` containing ground-truth target
                token indices for the given batch.
        """
        self.alphas = []

        loss = 0.0
        logps = None if self.training else torch.zeros(
            y.shape[0] - 1, y.shape[1], self.n_vocab).cuda()

        # Convert token indices to embeddings -> T*B*E
        y_emb = self.emb(y)

        # Get initial hidden state
        h = self.f_init(ctx_dict)

        # -1: So that we skip the timestep where input is <eos>
        for t in range(y_emb.shape[0] - 1):
            log_p, h = self.f_next(ctx_dict, y_emb[t], h)
            if not self.training:
                logps[t] = log_p.data
            loss += self.nll_loss(log_p, y[t + 1])

        return {'loss': loss, 'logps': logps}
