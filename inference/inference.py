"""
Performs inference on a trained model for a given dataset
"""

import os
import transformers
import datasets
import argparse
from transformers import TextClassificationPipeline, AutoModel, AutoTokenizer, AutoConfig, AutoModelForSequenceClassification
from transformers import DataCollatorWithPadding
from omegaconf import OmegaConf, dictconfig
from datasets import load_dataset
import json
MIMIC_PROTOCOLING_DIR = '/dataNAS/people/jmz/data/mimic_autoprocedure_selection/' #TODO: fix relative import

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_path', type=str, default='../results/classification/_gatortron_mimiciii_ct_procedure/run-4/checkpoint-2270')
    parser.add_argument('--dataset_name', type=str, default='mimiciii_ct_procedure')
    parser.add_argument('--output_dir', type=str, default='./predictions/gatortron_mimiciii_ct_procedure_val/')
    args = parser.parse_args()
    return args

def get_pipeline(model_path, dataset_name):
    if dataset_name == 'mimiciii_ct_procedure':
        config = AutoConfig.from_pretrained(model_path)
        
        pretrained_model = AutoModelForSequenceClassification.from_pretrained(model_path, config=config)
        tokenizer = AutoTokenizer.from_pretrained(model_path)
        pipeline = TextClassificationPipeline(
                    model=pretrained_model,
                    tokenizer=tokenizer,
                    top_k=None,
                    batch_size=32,)
    return pipeline
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

def main():
    args = parse_args()    

    pipeline = get_pipeline(args.model_path, args.dataset_name)
    data_files, text_col, label_col, id_col = get_data_files_by_task(args.dataset_name)

    dataset = load_data(data_files)
    dataset = dataset['val']
    
    predictions = pipeline(dataset[text_col])
    row_ids = dataset[id_col]

    preds_dict = {row_id:pred for row_id, pred in zip(row_ids, predictions)}

    # Save predictions
    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)
    with open(os.path.join(args.output_dir, 'predictions.json'), 'w') as f:
        json.dump(preds_dict, f)
    

if __name__=='__main__':
    main()