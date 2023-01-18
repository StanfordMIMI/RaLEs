import os
import transformers
import datasets
import argparse
from datasets import load_dataset
import json
from omegaconf import OmegaConf, dictconfig
import evaluate
from datasets import load_dataset
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
# from metrics import AccuracyAtK
MIMIC_PROTOCOLING_DIR = '/dataNAS/people/jmz/data/mimic_autoprocedure_selection/' #TODO: fix relative import

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--predictions_fpath', type=str, default='../inference/predictions/gatortron_mimiciii_ct_procedure_val/predictions.json')
    parser.add_argument('--dataset_name', type=str, default='mimiciii_ct_procedure')
    parser.add_argument('--data_split', type=str, default='val')
    args = parser.parse_args()
    return args

def load_data(fpaths):
    """
    TODO: import from fine-tuning script instead
    Load data from a filepath
    """
    
    if isinstance(fpaths, dictconfig.DictConfig) or isinstance(fpaths, dict):
        # print(type(dict(fpaths)))
        dset = load_dataset('csv', data_files=dict(fpaths))
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
                
    else:
        raise NotImplementedError('Loading data from {} is not implemented'.format(task))

def order_predictions(predictions, label2idx):
    """
    Returns ordered predictions from a list of {'label': str, 'score': float} and a label2idx dict
    """
    label_dict_order = sorted(label2idx.items(), key=lambda x: x[1])
    label2prob = {x['label']:x['score'] for x in predictions}
    ordered_predictions = [label2prob[label] for label, _ in label_dict_order]
    return ordered_predictions

def main():
    args = parse_args()
    # load dataset
    data_files, text_col, label_col, id_col = get_data_files_by_task(args.dataset_name)
    dataset = load_data(data_files)
    data_label_dict = dict(zip([str(x) for x in dataset[args.data_split]['ROW_ID']], dataset[args.data_split]['procedure_label']))
    
    label2idx = {label:idx for idx, label in enumerate(sorted(list(set(dataset['train']['procedure_label']))))}
    idx2label = {idx:label for label, idx in label2idx.items()}
    
    # load predictions
    with open(args.predictions_fpath, 'r') as f:
        predictions = json.load(f)
    
    predictions_formatted = [order_predictions(predictions[x], label2idx) for x in predictions.keys()]
    labels = [label2idx[data_label_dict[x]] for x in predictions.keys()]
    
    eval_name = args.predictions_fpath.split('/')[-2]
    
    # evaluate
    # accuracy at k
    accuracyatk = evaluate.load('./accuracyatk.py')
    metrics = {}
    metrics[eval_name] = {}
    for k in [1, 3, 5]:
        metrics[eval_name][f'accuracyatk{k}'] = accuracyatk.compute(predictions=predictions_formatted, references=labels, k=k)[f'accuracyat{k}']
    print(metrics)

    # confusion matrix
    # fig = plt.figure(figsize=(10,10))
    # ConfusionMatrixDisplay.from_predictions(labels, [x.index(max(x)) for x in predictions_formatted], 
    #                                     include_values=False, 
    #                                     normalize='true', 
    #                                     display_labels=[x[1] for x in sorted(zip(idx2label.keys(), idx2label.values()), key=lambda x: x[0])], 
    #                                     xticks_rotation='vertical')#.plot(ax=fig.gca())
    # plt.savefig('confusion_matrix.png')


if __name__ == '__main__':
    main()