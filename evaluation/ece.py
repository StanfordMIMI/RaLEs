"""
Defines custom metrics for use with HuggingFace evaluate

Metrics implemented:
    - ece (Expected Calibration Error) 
"""

import evaluate
import datasets
import numpy as np

_DESCRIPTION = """
ECE (expected calibration error) is a measure of calibration error. It is defined as the expected difference between the predicted probability (confidence) and the accuracy of the prediction.

It can be computed as:

ECE = 1/N * sum_i^N (|acc_i - p_i|)

where N is the number of bins, acc_i is the accuracy in bin i, and p_i is the average confidence in bin i.

bin_gap = | avg_confidence_in_bin - accuracy_in_bin |

Usually the bins are chosen to be equally spaced in terms of confidence. For example, if we have 10 bins, the first bin would be [0, 0.1), the second bin would be [0.1, 0.2), and so on. But it's not necessary. If there are unequal bin sizes, the ECE is weighted by the number of samples in each bin.

ECE = sum_i^N N_i/n * (|acc_i - p_i|) 
where n is the total number of samples, and N_i is the number of samples in bin i.

References:
- Naeini, Mahdi Pakdaman, Gregory F. Cooper, and Milos Hauskrecht. "Obtaining Well Calibrated Probabilities Using Bayesian Binning." AAAI 2015.
- Guo, Pleiss, Sun, and Weinberger. "On Calibration of Modern Neural Networks". ICML 2017
"""

_KWARGS_DESCRIPTION = """
Args:
    probs (np.array of float): array of probabilities of dim (n,m) where n is the number of samples and m is the number of classes
    targets (np.array of int): array of ground truth labels of dim (n,) where n is the number of samples
    n_bins (int): number of bins to use for computing ECE

Returns:
    ece (float): Expected Calibration Error. Minimum possible value is 0. Maximum possible value is 1.0. A lower score means better calibration.

Examples:
    Example 1-A simple example
        >>> ece_metric = evaluate.load("ece")
        >>> results = ece_metric.compute(predictions=[[0.5,0.3,0.2], [0.5,0.3,0.2], [0.4,0.1,0.5]], references=[0, 1, 2], n_bins=10)
        >>> print(results)
        {'ece': 0.16666666666666663}
"""

_CITATION = """
#TODO: Add citation
"""

class ECE(evaluate.Metric):
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

    def ece(self, probs, targets, n_bins=10):
        """
        Args:
            probs (np.array of float or list of list of float): array of probabilities of dim (n,m) where n is the number of samples and m is the number of classes
            targets (np.array of int): array of ground truth labels of dim (n,) where n is the number of samples
            n_bins (int): number of bins to use for computing ECE

        Returns:
            ece (float): Expected Calibration Error. Minimum possible value is 0. Maximum possible value is 1.0. A lower score means better calibration.

        Code adapted from Guo et al. (2017)
        """
        probs = np.array(probs)
        targets = np.array(targets)

        assert len(probs) == len(targets)
        assert n_bins > 0

        confidences = np.max(probs, axis=1)
        predictions = np.argmax(probs, axis=1)
        accuracies = predictions == targets

        bin_boundaries = np.linspace(0, 1, n_bins + 1)
        bin_lowers = bin_boundaries[:-1]
        bin_uppers = bin_boundaries[1:]

        ece = 0.0
        for bin_lower, bin_upper in zip(bin_lowers, bin_uppers):
            # Calculate bing gap or |confidence - accuracy| in each bin
            in_bin = np.logical_and(confidences > bin_lower, confidences <= bin_upper)
            prop_in_bin = np.mean(in_bin)
            if prop_in_bin > 0:
                accuracy_in_bin = np.mean(accuracies[in_bin])
                avg_confidence_in_bin = np.mean(confidences[in_bin])
                ece += np.abs(accuracy_in_bin - avg_confidence_in_bin) * prop_in_bin

        return ece

    def _compute(self, predictions, references, n_bins=10):
        return {
            f"ece{n_bins}": self.ece(predictions, references, n_bins)
        }