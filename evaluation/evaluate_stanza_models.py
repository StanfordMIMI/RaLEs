import os
from pathlib import Path
import transformers
import datasets
import argparse
from datasets import load_dataset
import json
from omegaconf import OmegaConf, dictconfig
import evaluate
from datasets import load_dataset
import numpy as np
# from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
# import matplotlib.pyplot as plt
import ast
# from metrics import AccuracyAtK
STANZA_DIR = '/DEIDPATH/data/radiology_NER/Radiology-NER/' #TODO: fix relative import

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--predictions_fpath', type=str, default='../inference/predictions/gatortron_mimiciii_ct_procedure_val/predictions.json')
    parser.add_argument('--dataset_name', type=str, default='stanza')
    parser.add_argument('--data_split', type=str, default='val')
    parser.add_argument('--output_path', type=str, default='./bootstrap_results/stanza/')
    parser.add_argument('--bootstrap', action='store_true')
    args = parser.parse_args()
    return args

def load_data(fpaths):
    """
    TODO: import from fine-tuning script instead
    Load data from a filepath
    """
    
    if isinstance(fpaths, dictconfig.DictConfig) or isinstance(fpaths, dict):
        if '.csv' in fpaths['train']:
            dset = load_dataset('csv', data_files=dict(fpaths))
        elif '.json' in fpaths['train']:
            dset = load_dataset('json', data_files=dict(fpaths))
        return dset
    elif fpaths[0].endswith('.csv'): #TODO make this compatible with dict not list
        return load_dataset('csv', data_files={'train':[x for x in fpaths if 'train' in x]}), \
                load_dataset('csv', data_files={'test':[x for x in fpaths if 'test' in x]})
    else:
        raise NotImplementedError('Loading data from {} is not implemented'.format(fpaths[0].split('.')[-1]))

def get_data_files_by_task(task):
    """
    TODO: import from fine-tuning script instead
    Get the data files for a given task
    """
    if task == 'mimiciii_ct_procedure':
        text_col = 'indication'
        label_col = 'procedure_label'
        id_col = 'ROW_ID'
        return {'train': os.path.join(MIMIC_PROTOCOLING_DIR, 'mimiciii_ct_procedure_train.csv'), 
                'val':   os.path.join(MIMIC_PROTOCOLING_DIR, 'mimiciii_ct_procedure_dev.csv'), 
                'test': os.path.join(MIMIC_PROTOCOLING_DIR, 'mimiciii_ct_procedure_test.csv')}, text_col, label_col, id_col
    if task == 'stanza':
        text_col = 'words'
        label_col = 'ner'
        id_col = None
        return {'train': os.path.join(STANZA_DIR, 'train.json'), 
                'val':   os.path.join(STANZA_DIR, 'dev.json'), 
                'test': os.path.join(STANZA_DIR, 'test.json')}, text_col, label_col, id_col
    else:
        raise NotImplementedError('Loading data from {} is not implemented'.format(task))

# def order_predictions(predictions, label2idx):
#     """
#     Returns ordered predictions from a list of {'label': str, 'score': float} and a label2idx dict
#     """
#     label_dict_order = sorted(label2idx.items(), key=lambda x: x[1])
#     label2prob = {x['label']:x['score'] for x in predictions}
#     ordered_predictions = [label2prob[label] for label, _ in label_dict_order]
#     return ordered_predictions

def get_idx_to_wordidx(wordlist):
    idx2wordidx = {}
    start=0
    for i, word in enumerate(wordlist):
        idx2wordidx[(start, start+len(word))] = i
        start += len(word)+1
    return idx2wordidx

def process_dataset(dataset, text_col, label_col):
    new_dataset = {}
    for i in range(len(dataset)):
        new_dataset[i] = {}
        new_dataset[i]['id'] = i
        new_dataset[i]['words'] = dataset[text_col][i]
        new_dataset[i]['ner'] = dataset[label_col][i]
        new_dataset[i]['idx2wordidx'] = get_idx_to_wordidx(dataset[text_col][i])
        new_dataset[i]['wordidx2idx'] = {v:k for k,v in new_dataset[i]['idx2wordidx'].items()}
    
    return new_dataset

def process_predictions_from_pipeline(predictions, dataset):
    """
    processes prediction made by AutoPipelineForTokenClassification (which introduces merges words and introduces spaces into tokens )
    """
    for k in predictions.keys():
        if k != 4:
            continue
        dataset_entry = dataset[k]
        
        pred_entity_list = ['O']*len(dataset_entry['words'])
        for pred_entity in predictions[k]:
            start, end = pred_entity['start'], pred_entity['end']
            words_in_entity = pred_entity['word'].split(' ')
            if len(words_in_entity) == 1:
                pred_entity_list[dataset_entry['idx2wordidx'][(start, end)]] = 'I-'+pred_entity['entity_group']
            else:

                for w in words_in_entity:
                    pred_entity_list[dataset_entry['idx2wordidx'][(start, start+len(w))]] = 'I-'+pred_entity['entity_group']
                    start += len(w)+1

def process_predictions(predictions, ignore_label=-100):
    processed_predictions = {}
    id2label = {int(k):v for k,v in predictions['id2labeldict'].items()}

    for k in predictions.keys():
        if k == 'id2labeldict':
            continue
        processed_predictions[k] = []
        
        true_labels = predictions[k]['labels']
        pred_labels = predictions[k]['pred_labels']
        
        processed_true_labels = [id2label[x] for x,y in zip(true_labels, pred_labels) if x != ignore_label]
        processed_pred_labels = [id2label[y] for x,y in zip(true_labels, pred_labels) if x != ignore_label]
        processed_predictions[k] = {'true_labels': processed_true_labels, 'pred_labels': processed_pred_labels}
    return processed_predictions

def bootstrap(keys, n_bootstraps=200):
    """
    Returns a list of n_bootstraps lists of keys
    """
    bootstrapped_keys = []
    for _ in range(n_bootstraps):
        bootstrapped_keys.append(np.random.choice(keys, size=len(keys), replace=True).tolist())
    return bootstrapped_keys

class NpEncoder(json.JSONEncoder):
    """
    https://stackoverflow.com/a/57915246
    """
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(NpEncoder, self).default(obj)

def main():
    args = parse_args()
    # load dataset
    data_files, text_col, label_col, id_col = get_data_files_by_task(args.dataset_name)
    # dataset = load_data(data_files)
    # dataset = dataset[args.data_split]
    # dataset = process_dataset(dataset, text_col, label_col)
    
    # load predictions
    with open(args.predictions_fpath, 'r') as f:
        predictions = json.load(f)
    
    true_pred_labels_only = process_predictions(predictions)
    
    
    #evaluate
    results = {}
    metric = evaluate.load("seqeval")
    split_results = metric.compute(predictions=[v['pred_labels'] for v in true_pred_labels_only.values()], references=[v['true_labels'] for v in true_pred_labels_only.values()])
    results[args.data_split] = split_results
    if args.bootstrap:
        bootstrapped_keys = bootstrap(list(true_pred_labels_only.keys()), 1000)
        
        for i, keys in enumerate(bootstrapped_keys):
            experiment_key = f'bootstrap_{args.data_split}_{i}'
            bootstrap_results = metric.compute(predictions=[true_pred_labels_only[k]['pred_labels'] for k in keys], 
                                                references=[true_pred_labels_only[k]['true_labels'] for k in keys])
            results[experiment_key] = bootstrap_results
        #summarize_bootstrap_results
        #TODO: implement per-class summary
        results['_bootstrap_summary'] = {} #_ to differentiate from iterations
        metrics_to_summarize = [x for x in results[args.data_split].keys() if x.startswith('overall_')]
        for metric in metrics_to_summarize:

            sorted_metric = sorted([results[k][metric] for k in results.keys() if k.startswith('bootstrap')])
            lower_ci_95 = sorted_metric[int(len(sorted_metric)*0.025)]
            upper_ci_95 = sorted_metric[int(len(sorted_metric)*0.975)]
            results['_bootstrap_summary'][metric] = {'mean': np.mean(sorted_metric), 'std': np.std(sorted_metric), 
                                                    'lower_ci_95': lower_ci_95, 'upper_ci_95': upper_ci_95}
    print(Path(args.predictions_fpath).parts[-2])
    print(results['_bootstrap_summary'])
    # save results
    with open(os.path.join(args.output_path, f'{Path(args.predictions_fpath).parts[-2]}_results.json'), 'w') as f:
        json_str = json.dumps(results, cls=NpEncoder)
        f.write(json_str)
    

if __name__ == '__main__':
    main()