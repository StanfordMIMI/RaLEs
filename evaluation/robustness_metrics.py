import numpy as np
import torch
from scipy.special import rel_entr

def ece(probs, targets, n_bins=10):
    """
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

def mce(probs, targets, n_bins=10):
    """
    MCE (maximum calibration error) is a measure of calibration error. It is defined as the maximum difference between the predicted probability (confidence) and the accuracy of the prediction.

    It can be computed as:

    MCE = max_i (|acc_i - p_i|)
    where acc_i is the accuracy in bin i, and p_i is the average confidence in bin i.

    bin_gap = | avg_confidence_in_bin - accuracy_in_bin |

    Usually the bins are chosen to be equally spaced in terms of confidence. For example, if we have 10 bins, the first bin would be [0, 0.1), the second bin would be [0.1, 0.2), and so on. But it's not necessary. If there are unequal bin sizes, the MCE is weighted by the number of samples in each bin.

    Args:
        probs (np.array of float or list of list of float): array of probabilities of dim (n,m) where n is the number of samples and m is the number of classes
        targets (np.array of int): array of ground truth labels of dim (n,) where n is the number of samples
        n_bins (int): number of bins to use for computing MCE

    Returns:
        mce (float): Maximum Calibration Error. Minimum possible value is 0. Maximum possible value is 1.0. A lower score means better calibration.
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

    bin_gaps = []
    for bin_lower, bin_upper in zip(bin_lowers, bin_uppers):
        # Calculate bin gap or |confidence - accuracy| in each bin
        in_bin = np.logical_and(confidences > bin_lower, confidences <= bin_upper)
        prop_in_bin = np.mean(in_bin)
        if prop_in_bin > 0:
            accuracy_in_bin = np.mean(accuracies[in_bin])
            avg_confidence_in_bin = np.mean(confidences[in_bin])
            bin_gap = np.abs(accuracy_in_bin - avg_confidence_in_bin) * prop_in_bin
            bin_gaps.append(bin_gap)

    mce = np.max(bin_gaps)

    return mce

def sce(probs, targets, n_bins=10):
    """
    SCE (static calibration error) is a measure of calibration error. It is a simple extension of the ECE, allowing for class conditionality in the multi-class setting. 

    It can be computed as:

    SCE = 1/K * sum_k^K sum_b^B [n_bk/N * (|acc_bk - p_bk|) 

    where K is the number of classes, B is the number of bins, n_bk is the number of samples in bin b for class k, N is the total number of samples, acc_bk is the accuracy in bin b for class k, and p_bk is the average confidence in bin b for class k.

    References:
    Nixon et al. (2019) - Measuring Calibration in Deep Learning. https://arxiv.org/abs/1904.01685

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

def nll(inputs, targets, logits = True):
    """
    NLL (Negative Log Likelihood) is a measure of the quality of probabilistic predictions. It is defined as the average negative log probability of the true class. It is a proper scoring metric. 

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

    return loss.numpy()

def weighted_model_confidence(probs, targets, weights = [1.0,0.0]):
    """
    WMC (Weighted Model Confidence) is a measure of the overall model confidence using  probabilistic predictions. It is defined as the weighted average confidence of the model in its predictions (rewarding / positive weight when it's confident and accurate, penalizing / negative weight when confident and inaccurate). 

    Args:
        probs (np.array of float or list of list of float): array of probabilities of dim (n,m) where n is the number of samples and m is the number of classes
        targets (np.array of int): array of ground truth labels of dim (n,) where n is the number of samples
        weights (list of float): list of weights for accuracy and inaccuracy (default: [1,0])

    Returns:
        wmc (float): Weighted model confidence. Higher the better. Maximum possible value is 1 and minimum possible value is 0. (assuming weights are 1 and 0)

    (Original metric)
    """
    probs = np.array(probs)
    targets = np.array(targets)

    assert len(probs) == len(targets)

    confidences = np.max(probs, axis=1)
    predictions = np.argmax(probs, axis=1)
    accuracies = predictions == targets

    weight_array = np.array([weights[0] if item else weights[1] for item in accuracies])

    wmc = np.dot(confidences, weight_array) / len(targets)

    return wmc

def average_KL_divergence_with_uniform_distribution(probs, targets):
    """
    Average of KL divergence of each data sample's probability distribution with uniform distribution  across all data samples. Higher the better. Minimum possible value is 0.
    Args:
        probs (np.array of float or list of list of float): array of probabilities of dim (n,m) where n is the number of samples and m is the number of classes
        targets (np.array of int): array of ground truth labels of dim (n,) where n is the number of samples
    Returns:
        avg_KL_U (float): average KL divergence of the predicted class with uniform distribution. Higher the better. Minimum possible value is 0. 
    """

    probs = np.array(probs)
    targets = np.array(targets)

    assert len(probs) == len(targets)

    num_classes = probs.shape[1] # (assumption: class labels or targets range from 0, 1, ... num_classes-1)

    unif = 1.0/num_classes * np.ones(probs.shape)
    KL_U = np.sum(rel_entr(unif, probs) , axis = 1)

    return np.mean(KL_U)


def average_pred_entropy(probs, targets):
    """
    Average predictive entropy. Lower the better.
    Args:
        probs (np.array of float or list of list of float): array of probabilities of dim (n,m) where n is the number of samples and m is the number of classes
        targets (np.array of int): array of ground truth labels of dim (n,) where n is the number of samples
    Returns:
        avg_pred_entropy (float): average predictive entropy. Lower the better. 
    """

    probs = np.array(probs)
    targets = np.array(targets)

    assert len(probs) == len(targets)
  
    # calculate entropy of the predicted class
    predEntropy = -1 * np.sum( np.log(probs) * probs , axis = 1)

    return np.mean(predEntropy)

