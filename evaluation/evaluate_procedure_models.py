import os
import transformers
import datasets
import argparse
from datasets import load_dataset
import json
from omegaconf import OmegaConf, dictconfig
import evaluate
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report
import matplotlib.pyplot as plt
from evaluate_stanza_models import bootstrap

MIMIC_PROTOCOLING_DIR = '/dataNAS/people/jmz/data/mimic_autoprocedure_selection/' #TODO: fix relative import
LOINC_PATH = '/dataNAS/people/jmz/data/ontologies/loinc_radlex'

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--predictions_fpath', type=str, default='../inference/predictions/gatortron_mimiciii_ct_procedure_val/predictions.json')
    parser.add_argument('--dataset_name', type=str, default='mimiciii_ct_procedure')
    parser.add_argument('--data_split', type=str, default='val')
    parser.add_argument('--bootstrap', action='store_true')
    parser.add_argument('--extended_error_analysis', action='store_true', default=False)

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
        return load_dataset('csv', data_files={k:v for k,v in fpaths.items()})
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
                'test': os.path.join(MIMIC_PROTOCOLING_DIR, 'mimiciii_ct_procedure_test.csv'),
                'newpts_test': os.path.join(MIMIC_PROTOCOLING_DIR, 'mimiciii_ct_procedure_nonoverlappatients_test.csv'),
                'repeatpts_test': os.path.join(MIMIC_PROTOCOLING_DIR, 'mimiciii_ct_procedure_overlappatients_test.csv')
                }, text_col, label_col, id_col
                
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

def plot_perf_by_support(predictions_formatted, labels, idx2label):
    top_predictions = [pred.index(max(pred)) for pred in predictions_formatted]

    # Compute per-class metrics
    report_dict = classification_report(labels, top_predictions, target_names=[idx2label[i] for i in range(len(idx2label))], output_dict=True)
    
    support = [report_dict[label]['support']/1000 for label in idx2label.values()]
    f1_scores = [report_dict[label]['f1-score'] for label in idx2label.values()]

    plt.figure(figsize=(10, 10), dpi=300)
    plt.scatter(support, f1_scores, color='blue', s=50, edgecolors='black', alpha=0.6)
    plt.xlabel("Number of Reports (Thousands)", fontsize=32)
    plt.ylabel("F1", fontsize=32)
    plt.xticks(fontsize=28)
    plt.yticks(fontsize=28)

    annotation_offsets = [(-50, -30), (150, -20), (40, -20), (80, 20)] 
    
    selected_indices = [support.index(max(support)), support.index(min(support)), 4, 25]

    for idx, offset in zip(selected_indices, annotation_offsets):
        plt.annotate(idx2label[idx], 
                    (support[idx], f1_scores[idx]), 
                    textcoords="offset points", 
                    xytext=offset, 
                    ha='center', 
                    fontsize=18,
                    arrowprops=dict(facecolor='black', arrowstyle="->", connectionstyle="arc3,rad=0.3"))

    plt.grid(False)

    plt.tight_layout()
    plt.savefig('../results/gatortron_procedure_f1score_support.png')

    return report_dict

def get_best_and_worst_examples(predictions_formatted, labels, n=3):

    true_scores = [predictions[label] for predictions, label in zip(predictions_formatted, labels)]

    zipped = list(enumerate(true_scores))

    sorted_by_error = sorted(zipped, key=lambda x: x[1])

    worst_example_indices = [index for index, _ in sorted_by_error][:n]
    best_example_indices = [index for index, _ in sorted_by_error[::-1]][:n]

    return worst_example_indices, best_example_indices


def main():
    args = parse_args()
    # load dataset
    data_files, text_col, label_col, id_col = get_data_files_by_task(args.dataset_name)
    dataset = load_data(data_files)[args.data_split]
    dataset_alltest = load_data(data_files)['test']
    
    data_label_dict = dict(zip([str(x) for x in dataset['ROW_ID']], dataset['procedure_label']))
    data_indication_dict = dict(zip([str(x) for x in dataset['ROW_ID']], dataset['indication']))
    
    label2idx = {label:idx for idx, label in enumerate(sorted(list(set(dataset_alltest['procedure_label']))))}
    
    idx2label = {idx:label for label, idx in label2idx.items()}

    if LOINC_PATH is not None and os.path.exists(LOINC_PATH):
        import pandas as pd
        #label to descrition
        loinc_table = pd.read_csv(os.path.join(LOINC_PATH,'Loinc.csv'), low_memory=False)[['LOINC_NUM','CLASS','SHORTNAME','LONG_COMMON_NAME']]
        loinc_table = loinc_table[loinc_table['CLASS']=='RAD']
        loinc2short = dict(zip(loinc_table['LOINC_NUM'],loinc_table['SHORTNAME']))

        def map_label_to_description(label):
            if '_' in label:
                labels = label.split('_')
            else:
                labels = [label]
            return ' + '.join([loinc2short[l] if l in loinc2short else l for l in labels])

        idx2label = {idx:map_label_to_description(label) for idx, label in idx2label.items()}
    
    # load predictions
    with open(args.predictions_fpath, 'r') as f:
        predictions = json.load(f)
    
    predictions = {k:v for k,v in predictions.items() if k in data_label_dict.keys()}
    predictions_formatted = [order_predictions(predictions[x], label2idx) for x in predictions.keys()]
    predictions_ids = [x for x in predictions.keys()]
    labels = [label2idx[data_label_dict[x]] for x in predictions.keys()]

    # print(len(predictions_formatted))
    # print(len(labels))
    # exit()
    eval_name = args.predictions_fpath.split('/')[-2]
    
    # evaluate
    # accuracy at k
    accuracyatk = evaluate.load('./accuracyatk.py')
    metrics = {}
    metrics[eval_name] = {}
    for k in [1, 3, 5]:
        metrics[eval_name][f'accuracyatk{k}'] = '{:.3f}'.format(accuracyatk.compute(predictions=predictions_formatted, references=labels, k=k)[f'accuracyat{k}'])
    print(f'{eval_name} : {metrics[eval_name]}')



     
    if args.extended_error_analysis:

        report = plot_perf_by_support(predictions_formatted, labels, idx2label)
        
        format_dict_for_printing = lambda x: {k: f'{v:.3f}' if k!='support' else v for k,v in x.items() }
        formatted_report = {k:format_dict_for_printing(v) for k,v in report.items() if k not in ['accuracy','macro avg', 'weighted avg']}

        worst_3, best_3 = get_best_and_worst_examples(predictions_formatted, labels, n=3)

        for idx, example in enumerate(worst_3):
            print('-'*50)
            print(f"bad example {idx+1}")
            print(f'Indication: {data_indication_dict[predictions_ids[example]]}')
            print(f'True label: {idx2label[labels[example]]}')
            print(f'Predicted label: {idx2label[predictions_formatted[example].index(max(predictions_formatted[example]))]}')
            print(f'Probability (predicted label): {max(predictions_formatted[example]):.3f}')
            print(f'Probability (ground truth): {predictions_formatted[example][labels[example]]:.3f}')

        for idx, example in enumerate(best_3):
            print('-'*50)
            print(f"good example {idx+1}")
            print(f'Indication: {data_indication_dict[predictions_ids[example]]}')
            print(f'True label: {idx2label[labels[example]]}')
            print(f'Predicted label: {idx2label[predictions_formatted[example].index(max(predictions_formatted[example]))]}')
            print(f'Probability (predicted label): {max(predictions_formatted[example]):.3f}')
            print(f'Probability (ground truth): {predictions_formatted[example][labels[example]]:.3f}')

            
            



if __name__ == '__main__':
    main()