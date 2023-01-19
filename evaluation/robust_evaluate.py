import os

import numpy as np
import pandas as pd
import torch
import json
from pprint import pprint
from tqdm import tqdm
import csv

from robustness_metrics import ece, mce, sce, nll, weighted_model_confidence, average_KL_divergence_with_uniform_distribution, average_pred_entropy

def order_predictions(predictions, label2idx):
    """
    Returns ordered predictions from a list of {'label': str, 'score': float} and a label2idx dict
    """
    label_dict_order = sorted(label2idx.items(), key=lambda x: x[1])
    label2prob = {x['label']:x['score'] for x in predictions}
    ordered_predictions = [label2prob[label] for label, _ in label_dict_order]
    return ordered_predictions

root_dir = '/home/nandita/nab_code/RaLEs/nab_outputs'
predictions_dir = '/home/nandita/nab_code/RaLEs/nab_outputs/predictions'
logits_dir = '/home/nandita/nab_code/RaLEs/nab_outputs/logits'
data_label_dict_path = '/home/nandita/nab_code/RaLEs/nab_outputs/data_label_dict.json'
idx2label_path = '/home/nandita/nab_code/RaLEs/nab_outputs/idx2label.json'
label2idx_path = '/home/nandita/nab_code/RaLEs/nab_outputs/label2idx.json'
save_dir = '/home/nandita/nab_code/RaLEs/nab_outputs/index_target_logits_predictions'
save_folder_name = "index_target_logits_predictions"

# load data_label_dict
with open(data_label_dict_path, 'r') as f:
    data_label_dict = json.load(f)

# load label2idx
with open(label2idx_path, 'r') as f:
    label2idx = json.load(f)

# load idx2label
with open(idx2label_path, 'r') as f:
    idx2label = json.load(f)

# # get list of predictions filenames in directory right now
# predictions_files = [os.path.join(root, name)
#                      for root, dirs, files in os.walk(predictions_dir)
#                          for name in files
#                              if name.endswith("tions.json") and "test" in root and "stanza" not in root]

# get list of logits filenames in directory right now
logits_files = [os.path.join(root, name) 
                    for root, dirs, files in os.walk(logits_dir)
                        for name in files
                            if name.endswith("tions.json") and "test" in root]

# get the corrseponding prediction file for each logit file
predictions_files = [predictions_dir + logits_file.split(logits_dir)[1] for logits_file in logits_files]


final_metrics_table = []

# read the predictions and logits files
for i, logits_path in enumerate(logits_files):

    print(logits_path)
    pred_path = predictions_files[i]

    save_path = logits_path.replace('/predictions.json', ".pkl").replace('logits', save_folder_name)
    print(save_path)

    # ensure both logits and predictions are for the same model/dataset combination
    assert logits_path.split(logits_dir)[1].split("/")[0] == pred_path.split(predictions_dir)[1].split("/")[0]

    # read the logits and predictions files
    with open(logits_path, 'r') as f:
        logits = json.load(f)
    with open(pred_path, 'r') as f:
        predictions = json.load(f)

    data_dict = {}

    datapoint_list = []
    target_list = []
    target_indices_list = []
    logits_list = []
    predictions_list = []

    # loop over each data point
    for datapoint in tqdm(logits.keys()):

        current_target = data_label_dict[datapoint]
        current_target_idx = label2idx[current_target]

        # get the ordered logits, predictions
        current_logits = logits[datapoint]
        current_predictions = predictions[datapoint]
        ordered_logits = order_predictions(current_logits, label2idx)
        ordered_predictions = order_predictions(current_predictions, label2idx)

        # append to list
        datapoint_list.append(datapoint)
        target_list.append(current_target)
        target_indices_list.append(current_target_idx)
        logits_list.append(ordered_logits)
        predictions_list.append(ordered_predictions)

    data_dict['datapoints'] = datapoint_list
    data_dict['targets'] = target_list
    data_dict['target_indices'] = np.array(target_indices_list)
    data_dict['logits'] = np.array(logits_list)
    data_dict['predictions'] = np.array(predictions_list)

    data_dict['ece'] = ece(data_dict['predictions'], data_dict['target_indices'], n_bins=10)
    data_dict['mce'] = mce(data_dict['predictions'], data_dict['target_indices'], n_bins=10)
    data_dict['sce'] = sce(data_dict['predictions'], data_dict['target_indices'], n_bins=10)
    data_dict['nll'] = nll(data_dict['logits'], data_dict['target_indices'], logits = True)
    data_dict['wmc'] = weighted_model_confidence(data_dict['predictions'], data_dict['target_indices'], weights = [1,0])
    data_dict['av_KLU'] = average_KL_divergence_with_uniform_distribution(data_dict['predictions'], data_dict['target_indices'])
    data_dict['av_predEntropy'] = average_pred_entropy(data_dict['predictions'], data_dict['target_indices'])

    print(data_dict['ece'], data_dict['mce'], data_dict['sce'], data_dict['nll'], data_dict['wmc'], data_dict['av_KLU'], data_dict['av_predEntropy'])

    # final values. Save metrics to csv file
    metrics = {'model_dataset': save_path.split('/')[-1].replace('.pkl',''), 'ece': data_dict['ece'], 'mce': data_dict['mce'], 'sce': data_dict['sce'], 'nll': data_dict['nll'], 'wmc': data_dict['wmc'], 'av_KLU': data_dict['av_KLU'], 'av_predEntropy': data_dict['av_predEntropy']}

    final_metrics_table.append(metrics)

field_names = ['model_dataset', 'ece', 'mce', 'sce', 'nll', 'wmc', 'av_KLU', 'av_predEntropy']

with open(os.path.join(root_dir, 'robustness_metrics.csv'), 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(final_metrics_table)

    