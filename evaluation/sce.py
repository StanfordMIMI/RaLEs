"""
Defines custom metrics for use with HuggingFace evaluate

Metrics implemented:
    - sce (Static Calibration Error) 
"""

import evaluate
import datasets
import numpy as np

_DESCRIPTION = """
SCE (static calibration error) is a measure of calibration error. It is a simple extension of the ECE, allowing for class conditionality in the multi-class setting. 

It can be computed as:

SCE = 1/K * sum_k^K sum_b^B [n_bk/N * (|acc_bk - p_bk|) 

where K is the number of classes, B is the number of bins, n_bk is the number of samples in bin b for class k, N is the total number of samples, acc_bk is the accuracy in bin b for class k, and p_bk is the average confidence in bin b for class k.

References:
Nixon et al. (2019) - Measuring Calibration in Deep Learning. https://arxiv.org/abs/1904.01685
"""

_KWARGS_DESCRIPTION = """
Args:
    probs (np.array of float): array of probabilities of dim (n,m) where n is the number of samples and m is the number of classes
    targets (np.array of int): array of ground truth labels of dim (n,) where n is the number of samples
    n_bins (int): number of bins to use for computing SCE

Returns:
    sce (float): Static Calibration Error. Minimum possible value is 0.  Maximum possible value is 1.0. , SCE is guaranteed to be zero if only if the model is calibrated

Examples:
    Example 1-A simple example
        >>> sce_metric = evaluate.load("sce")
        >>> results = sce_metric.compute(predictions=[[0.5,0.3,0.2], [0.5,0.3,0.2], [0.4,0.1,0.5], [0.1,0.3,0.6]], references=[0, 1, 1, 2], n_bins=10)
        >>> print(results)
        {'sce': 0.2333333333333333}
"""

_CITATION = """
#TODO: Add citation
"""

class SCE(evaluate.Metric):
    def _info(self):
        return evaluate.MetricInfo(
            description=_DESCRIPTION,
            citation=_CITATION,
            inputs_description=_KWARGS_DESCRIPTION,
            features=datasets.Features( 
                {
                    "predictions": datasets.Sequence(datasets.Value("float32")),
                    "references": datasets.Value("int32")
                }
            ),
            reference_urls=[],
        )

    def sce(self, probs, targets, n_bins=10):
        """
        Args:
            probs (np.array of float or list of list of float): array of probabilities of dim (n,m) where n is the number of samples and m is the number of classes
            targets (np.array of int): array of ground truth labels of dim (n,) where n is the number of samples
            n_bins (int): number of bins to use for computing SCE

        Returns:
            sce (float): Static Calibration Error. Minimum possible value is 0.  Maximum possible value is 1.0. , SCE is guaranteed to be zero if only if the model is calibrated
        """
        probs = np.array(probs)
        targets = np.array(targets)

        num_classes = probs.shape[1] # (assumption: class labels or targets are 0, 1, ... num_classes-1)

        assert len(probs) == len(targets)
        assert n_bins > 0

        bin_boundaries = np.linspace(0, 1, n_bins + 1)
        bin_lowers = bin_boundaries[:-1]
        bin_uppers = bin_boundaries[1:]
        
        sce = 0.0
        for bin_lower, bin_upper in zip(bin_lowers, bin_uppers):
            for classLabel in range(num_classes):
                # Calculate bin gap or |confidence - accuracy| in each bin per class
                in_bin = np.logical_and(probs[:,classLabel] > bin_lower, probs[:,classLabel] <= bin_upper)
                prop_in_bin = np.mean(in_bin)
                if prop_in_bin > 0:
                    accuracy_in_bin = np.mean(targets[in_bin] == classLabel)
                    avg_confidence_in_bin = np.mean(probs[in_bin,classLabel])
                    sce += np.abs(accuracy_in_bin - avg_confidence_in_bin) * prop_in_bin

        sce /= num_classes

        return sce

    def _compute(self, predictions, references, n_bins=10):
        return {
            f"sce{n_bins}": self.sce(predictions, references, n_bins)
        }