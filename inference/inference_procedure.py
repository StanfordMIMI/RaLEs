"""
Performs inference on a trained model for a given dataset
"""

import os
import transformers
import datasets
import argparse
from transformers import TextClassificationPipeline, AutoModel, AutoTokenizer, AutoConfig, AutoModelForSequenceClassification, AutoModelForTokenClassification, TokenClassificationPipeline
from transformers import DataCollatorForTokenClassification, DataCollatorWithPadding, Trainer
from omegaconf import OmegaConf, dictconfig
from datasets import load_dataset
from torch.utils.data import DataLoader
from torch.utils.data.sampler import SequentialSampler
import torch.nn.functional as F
import evaluate
import json
import numpy as np
from transformers.trainer_pt_utils import nested_concat

MIMIC_PROTOCOLING_DIR = '/PATH_TO//data/mimic_autoprocedure_selection/' #TODO: fix relative import
STANZA_DIR = '/PATH_TO//data/radiology_NER/Radiology-NER/' #TODO: fix relative import

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_path', type=str, default='../results/classification/_gatortron_mimiciii_ct_procedure/run-4/checkpoint-2270')
    parser.add_argument('--dataset_name', type=str, default='mimiciii_ct_procedure')
    parser.add_argument('--data_split', type=str, default='val')
    parser.add_argument('--output_type', type=str, default='score') #score vs logits
    parser.add_argument('--output_dir', type=str, default='./predictions/gatortron_mimiciii_ct_procedure_val/')
    args = parser.parse_args()
    return args

def get_pipeline(model_path, dataset_name, output_type):
    if dataset_name == 'mimiciii_ct_procedure':
        config = AutoConfig.from_pretrained(model_path)
        
        pretrained_model = AutoModelForSequenceClassification.from_pretrained(model_path, config=config)
        tokenizer = AutoTokenizer.from_pretrained(model_path)
        if output_type == 'score':
            pipeline = TextClassificationPipeline(
                        model=pretrained_model,
                        tokenizer=tokenizer,
                        top_k=None,
                        batch_size=32,
                        device=0,)
        elif output_type == 'logits':
            pipeline = TextClassificationPipeline(
                        model=pretrained_model,
                        tokenizer=tokenizer,
                        top_k=None,
                        batch_size=32,
                        device=0,
                        function_to_apply="none")
        else:
            raise NotImplementedError('output_type {} is not implemented'.format(output_type))
    if dataset_name == 'stanza':
        config = AutoConfig.from_pretrained(model_path)
        
        pretrained_model = AutoModelForTokenClassification.from_pretrained(model_path, config=config)
        tokenizer = AutoTokenizer.from_pretrained(model_path)
        pipeline = TokenClassificationPipeline(
                    model=pretrained_model,
                    tokenizer=tokenizer,
                    batch_size=1,
                    device=0,
                    aggregation_strategy='first')
    return pipeline, pretrained_model, tokenizer

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

def eval_using_trainer(pipeline, tokenizer, model, dataset, text_col, label_col, id_col, task, model_path, output_dir):
    #TODO: check
    
    metric = evaluate.load("seqeval")
    def compute_metrics(p):
        predictions, labels = p
        predictions = np.argmax(predictions, axis=2)

        # Remove ignored index (special tokens)
        true_predictions = [
            [label_list[p] for (p, l) in zip(prediction, label) if l != -100]
            for prediction, label in zip(predictions, labels)
        ]
        true_labels = [
            [label_list[l] for (p, l) in zip(prediction, label) if l != -100]
            for prediction, label in zip(predictions, labels)
        ]

        results = metric.compute(predictions=true_predictions, references=true_labels)
        if True:
            # Unpack nested dictionaries
            final_results = {}
            for key, value in results.items():
                if isinstance(value, dict):
                    for n, v in value.items():
                        final_results[f"{key}_{n}"] = v
                else:
                    final_results[key] = value
            return final_results
        else:
            return {
                "precision": results["overall_precision"],
                "recall": results["overall_recall"],
                "f1": results["overall_f1"],
                "accuracy": results["overall_accuracy"],
            }
    from transformers import TrainingArguments
    trainer = Trainer(model=model,
        args=None,
        train_dataset=None,
        eval_dataset=val_dataset,
        tokenizer=tokenizer,
        data_collator=data_collator,
        compute_metrics=compute_metrics,
    )
    trainer.evaluate()

class NumpyEncoder(json.JSONEncoder):
    """from https://stackoverflow.com/a/47626762/10307491"""
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


def main():
    args = parse_args()    
    
    pipeline, model, tokenizer = get_pipeline(args.model_path, args.dataset_name, args.output_type)
    
    data_files, text_col, label_col, id_col = get_data_files_by_task(args.dataset_name)

    dataset = load_data(data_files)
    dataset = dataset[args.data_split]
    
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