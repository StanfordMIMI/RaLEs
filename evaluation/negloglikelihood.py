"""
Defines custom metrics for use with HuggingFace evaluate

Metrics implemented:
    - NLL (Negative Log Likelihood)
"""

import evaluate
import datasets
import numpy as np
import torch

_DESCRIPTION = """
NLL (Negative Log Likelihood) is a measure of the quality of probabilistic predictions. It is defined as the average negative log probability of the true class. It is a proper scoring metric. 
"""

_KWARGS_DESCRIPTION = """
Args:
    inputs (np.array of float or list of list of float): array of logits or probabilities of dim (n,m) where n is the number of samples and m is the number of classess
    targets (np.array of int): array of ground truth labels of dim (n,) where n is the number of samples
    logits (bool): whether the inputs are logits or probabilities (default: True)

Returns:
    loss (float): negative log likelihood

Examples:
    Example 1-A simple example
        >>> nll_metric = evaluate.load("nll")
        >>> results = nll_metric.compute(inputs=[[0.5,0.3,0.2], [0.5,0.3,0.2], [0.4,0.1,0.5], [0.1,0.3,0.6]], references=[0, 1, 1, 2], logits=False)
        >>> print(results)
        {'nll': 1.1776326894760132}

Note that we compute the cross entropy loss from the logits instead of NLL after softmax for numerical stability issues if possible.
"""

_CITATION = """
#TODO: Add citation
"""

class NLL(evaluate.Metric):
    def _info(self):
        return evaluate.MetricInfo(
            description=_DESCRIPTION,
            citation=_CITATION,
            inputs_description=_KWARGS_DESCRIPTION,
            features=datasets.Features( 
                {
                    "inputs": datasets.Sequence(datasets.Value("float32")), #TODO: get logits instead of probs?
                    "references": datasets.Value("int32")
                }
            ),
            reference_urls=[],
        )

    def nll(self, inputs, targets, logits = True):
        """
        Args:
            inputs (np.array of float or list of list of float): array of logits or probabilities of dim (n,m) where n is the number of samples and m is the number of classess
            targets (np.array of int): array of ground truth labels of dim (n,) where n is the number of samples
            logits (bool): whether the inputs are logits or probabilities (default: True)

        Returns:
            nll (float): negative log likelihood
        """
        inputs = torch.tensor(inputs)
        targets = torch.tensor(targets)

        assert len(inputs) == len(targets)

        if logits:
            logits = inputs
            criterion = torch.nn.CrossEntropyLoss()
            loss = criterion(logits, targets)
        else:
            probs = inputs
            criterion = torch.nn.NLLLoss()
            loss = criterion(torch.log(probs), targets)

        return loss.item()

    def _compute(self, inputs, references, n_bins=10):
        return {
            f"nll{n_bins}": self.nll(inputs, references, n_bins)
        }