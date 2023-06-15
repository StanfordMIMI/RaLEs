import logging
import math
from typing import Any, Dict, List, Optional, Tuple

import torch
import torch.nn.functional as F
from overrides import overrides

from allennlp.data import Vocabulary
from allennlp.models.model import Model
from allennlp.modules.token_embedders import Embedding
from allennlp.modules import FeedForward
from allennlp.modules import Seq2SeqEncoder, TimeDistributed, TextFieldEmbedder, Pruner
from allennlp.modules.span_extractors import SelfAttentiveSpanExtractor, EndpointSpanExtractor
from allennlp.nn import util, InitializerApplicator, RegularizerApplicator
from allennlp.training.metrics import MentionRecall, ConllCorefScores

# Import submodules.
from dygie.models.coref import CorefResolver
from dygie.models.ner import NERTagger
from dygie.models.relation import RelationExtractor

logger = logging.getLogger(__name__)  # pylint: disable=invalid-name



@Model.register("dygie")
class DyGIE(Model):
    """
    TODO(dwadden) document me.

    Parameters
    ----------
    vocab : ``Vocabulary``
    text_field_embedder : ``TextFieldEmbedder``
        Used to embed the ``text`` ``TextField`` we get as input to the model.
    context_layer : ``Seq2SeqEncoder``
        This layer incorporates contextual information for each word in the document.
    feature_size: ``int``
        The embedding size for all the embedded features, such as distances or span widths.
    submodule_params: ``TODO(dwadden)``
        A nested dictionary specifying parameters to be passed on to initialize submodules.
    max_span_width: ``int``
        The maximum width of candidate spans.
    lexical_dropout: ``int``
        The probability of dropping out dimensions of the embedded text.
    initializer : ``InitializerApplicator``, optional (default=``InitializerApplicator()``)
        Used to initialize the model parameters.
    regularizer : ``RegularizerApplicator``, optional (default=``None``)
        If provided, will be used to calculate the regularization penalty during training.
    """
    def __init__(self,
                 vocab: Vocabulary,
                 text_field_embedder: TextFieldEmbedder,
                 context_layer: Seq2SeqEncoder,
                 modules,  # TODO(dwadden) Add type.
                 feature_size: int,
                 max_span_width: int,
                 lexical_dropout: float = 0.2,
                 use_attentive_span_extractor: bool = True,
                 initializer: InitializerApplicator = InitializerApplicator(),
                 regularizer: Optional[RegularizerApplicator] = None) -> None:
        super(DyGIE, self).__init__(vocab, regularizer)

        self._text_field_embedder = text_field_embedder
        self._context_layer = context_layer


        # TODO(dwadden) Figure out the parameters that need to get passed in.
        self._coref = CorefResolver.from_params(vocab=vocab,
                                                feature_size=feature_size,
                                                params=modules.pop("coref"))
        self._ner = NERTagger.from_params(vocab=vocab,
                                          feature_size=feature_size,
                                          params=modules.pop("ner"))
        self._relation = RelationExtractor.from_params(vocab=vocab,
                                                       feature_size=feature_size,
                                                       params=modules.pop("relation"))

        self._endpoint_span_extractor = EndpointSpanExtractor(context_layer.get_output_dim(),
                                                              combination="x,y",
                                                              num_width_embeddings=max_span_width,
                                                              span_width_embedding_dim=feature_size,
                                                              bucket_widths=False)
        if use_attentive_span_extractor:
            self._attentive_span_extractor = SelfAttentiveSpanExtractor(
                input_dim=text_field_embedder.get_output_dim())
        else:
            self._attentive_span_extractor = None

        self._max_span_width = max_span_width

        if lexical_dropout > 0:
            self._lexical_dropout = torch.nn.Dropout(p=lexical_dropout)
        else:
            self._lexical_dropout = lambda x: x
        initializer(self)

    @overrides
    def forward(self,
                text,
                spans,
                ner_labels,
                coref_labels,
                relation_labels,
                metadata):
        """
        TODO(dwadden) change this.
        """
        # TODO(dwadden) Is there some smarter way to do the batching within a document?

        # Shape: (batch_size, max_sentence_length, embedding_size)
        text_embeddings = self._lexical_dropout(self._text_field_embedder(text))
        max_sentence_length = text_embeddings.size(1)

        # Shape: (batch_size, max_sentence_length)
        text_mask = util.get_text_field_mask(text).float()

        sentence_lengths = text_mask.sum(dim=1).long()

        # Shape: (batch_size, num_spans)
        span_mask = (spans[:, :, 0] >= 0).float()
        # SpanFields return -1 when they are used as padding. As we do
        # some comparisons based on span widths when we attend over the
        # span representations that we generate from these indices, we
        # need them to be <= 0. This is only relevant in edge cases where
        # the number of spans we consider after the pruning stage is >= the
        # total number of spans, because in this case, it is possible we might
        # consider a masked span.
        # Shape: (batch_size, num_spans, 2)
        spans = F.relu(spans.float()).long()

        # Shape: (batch_size, max_sentence_length, encoding_dim)
        contextualized_embeddings = self._context_layer(text_embeddings, text_mask)
        # Shape: (batch_size, num_spans, 2 * encoding_dim + feature_size)
        endpoint_span_embeddings = self._endpoint_span_extractor(contextualized_embeddings, spans)

        if self._attentive_span_extractor is not None:
            # Shape: (batch_size, num_spans, emebedding_size)
            attended_span_embeddings = self._attentive_span_extractor(text_embeddings, spans)
            # Shape: (batch_size, num_spans, emebedding_size + 2 * encoding_dim + feature_size)
            span_embeddings = torch.cat([endpoint_span_embeddings, attended_span_embeddings], -1)
        else:
            span_embeddings = endpoint_span_embeddings

        # Make calls out to the modules to get results.
        # output_coref = self._coref(
        #     spans, span_mask, span_embeddings, sentence_lengths, coref_labels, metadata)
        # output_ner = self._ner(
        #     spans, span_mask, span_embeddings, sentence_lengths, max_sentence_length, ner_labels, metadata)
        output_relation = self._relation(
            spans, span_mask, span_embeddings, sentence_lengths, max_sentence_length, relation_labels, metadata)

        # TODO(dwadden) ... and now what?
        return output_relation


    @overrides
    def decode(self, output_dict: Dict[str, torch.Tensor]):
        """
        Converts the list of spans and predicted antecedent indices into clusters
        of spans for each element in the batch.

        Parameters
        ----------
        output_dict : ``Dict[str, torch.Tensor]``, required.
            The result of calling :func:`forward` on an instance or batch of instances.

        Returns
        -------
        The same output dictionary, but with an additional ``clusters`` key:

        clusters : ``List[List[List[Tuple[int, int]]]]``
            A nested list, representing, for each instance in the batch, the list of clusters,
            which are in turn comprised of a list of (start, end) inclusive spans into the
            original document.
        """
        pass


    def get_metrics(self, reset: bool = False) -> Dict[str, float]:
        metrics_relation = self._relation.get_metrics(reset=reset)
        # TODO(dwadden) add the metrics for the other tasks.

        return metrics_relation
