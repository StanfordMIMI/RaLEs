"""
Defines custom metrics for use with HuggingFace evaluate

Metrics implemented:
    -accuracy@k
"""

import evaluate
import datasets
import numpy as np

_DESCRIPTION = """
Accuracy at k is the proportion of correct predictions among the total number of cases processed. 
A prediction is considered correct if it appears within the top k most probable classes. 
It can be computed with:
Accuracy = (TP + TN) / (TP + TN + FP + FN)
 Where:
TP: True positive
TN: True negative
FP: False positive
FN: False negative
"""


_KWARGS_DESCRIPTION = """
Args:
    predictions (`list` of `list` of `float`): array of probabilities of dim (n,m) where n is the number of samples and m is the number of classes
    references (`list` of `int`): array of ground truth labels of dim (n,) where n is the number of samples
    k (`int`): number of top predictions to consider
    
Returns:
    accuracy@k (`float`): Accuracy score at k. Minimum possible value is 0. Maximum possible value is 1.0. A higher score means higher accuracy.
Examples:
    Example 1-A simple example
        >>> accuracyatk_metric = evaluate.load("accuracyatk")
        >>> results = accuracyatk_metric.compute(predictions=[[0.5,0.3,0.2], [0.5,0.3,0.2], [0.4,0.1,0.5], [0.1,0.3,0.6]], references=[0, 1, 1, 2], k=2)
        >>> print(results)
        {'accuracyat2': 0.75}
"""
_CITATION = """
#TODO: add citation
"""
class AccuracyAtK(evaluate.Metric):
    def _info(self):
        return evaluate.MetricInfo(
            description=_DESCRIPTION,
            citation=_CITATION,
            inputs_description=_KWARGS_DESCRIPTION,
            features=datasets.Features( #don't include k as will lead to error in evaluate.Metric._compute
                {
                    "predictions": datasets.Sequence(datasets.Value("float32")),
                    "references": datasets.Value("int32")
                }
            ),
            reference_urls=[],
        )

    def accuracyAtK(self, probs, targets, k):
        sorted_probs = np.argsort(probs, axis=1, kind='mergesort')[:, ::-1]
        hits=np.any(targets[:] == sorted_probs[:,:k].T, axis=0)    
        return np.sum(hits)/hits.shape[0]

    def _compute(self, predictions, references, k):
        return {
            f"accuracyat{k}": self.accuracyAtK(predictions, references, k)
        }