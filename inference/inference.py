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
<<<<<<< HEAD
import torch.nn.functional as F
=======
>>>>>>> dc37c4c (inference best models stanza, procedure)
import evaluate
import json
import numpy as np
from transformers.trainer_pt_utils import nested_concat

<<<<<<< HEAD
MIMIC_PROTOCOLING_DIR = '/PATH_TO//data/mimic_autoprocedure_selection/' #TODO: fix relative import
STANZA_DIR = '/PATH_TO//data/radiology_NER/Radiology-NER/' #TODO: fix relative import
=======
MIMIC_PROTOCOLING_DIR = '/dataNAS/people/jmz/data/mimic_autoprocedure_selection/' #TODO: fix relative import
STANZA_DIR = '/dataNAS/people/jmz/data/radiology_NER/Radiology-NER/' #TODO: fix relative import
>>>>>>> dc37c4c (inference best models stanza, procedure)

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
<<<<<<< HEAD
                        device=0,
=======
>>>>>>> dc37c4c (inference best models stanza, procedure)
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
<<<<<<< HEAD
                    batch_size=1,
                    device=0,
                    aggregation_strategy='first')
=======
                    batch_size=1)
>>>>>>> dc37c4c (inference best models stanza, procedure)
    return pipeline, pretrained_model, tokenizer

def tokenize_and_align_labels(examples, tokenizer, text_column_name, label_column_name, max_seq_length, label_to_id, b_to_i_label,
                              label_all_tokens=False):
    #TODO: fix to import from fine-tuning script
    tokenized_inputs = tokenizer(
        examples[text_column_name],
        padding=False,
        truncation=True,
        max_length=max_seq_length,
        is_split_into_words=True,
    )
    labels = []
    for i, label in enumerate(examples[label_column_name]):
        word_ids = tokenized_inputs.word_ids(batch_index=i)
        previous_word_idx = None
        label_ids = []
        for word_idx in word_ids:
            # Special tokens have a word id that is None. We set the label to -100 so they are automatically
            # ignored in the loss function.
            if word_idx is None:
                label_ids.append(-100)
            # We set the label for the first token of each word.
            elif word_idx != previous_word_idx:
                label_ids.append(label_to_id[label[word_idx]])
            else:
                if label_all_tokens:
                    label_ids.append(b_to_i_label[label_to_id[label[word_idx]]])
                else:
                    label_ids.append(-100)
            previous_word_idx = word_idx

        labels.append(label_ids)
    tokenized_inputs["labels"] = labels
    return tokenized_inputs

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
<<<<<<< HEAD
    
=======
    label_list = [pipeline.model.config.id2label[k] for k in pipeline.model.config.id2label]
    b_to_i_label = []
    for idx, label in enumerate(label_list):
        if label.startswith("B-") and label.replace("B-", "I-") in label_list:
            b_to_i_label.append(label_list.index(label.replace("B-", "I-")))
        else:
            b_to_i_label.append(idx)
    data_collator = DataCollatorForTokenClassification(tokenizer)
    val_dataset = dataset.map(
        tokenize_and_align_labels,
        fn_kwargs={
            'tokenizer': pipeline.tokenizer,
            'text_column_name': text_col,
            'label_column_name': label_col,
            'max_seq_length': None,
            'label_to_id': pipeline.model.config.label2id,
            'b_to_i_label': b_to_i_label,
            'label_all_tokens': False,
        },
        batched=True,
        desc="Running tokenizer on validation dataset",
        )
    val_dataset = val_dataset.remove_columns(['ner','words'])
>>>>>>> dc37c4c (inference best models stanza, procedure)
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
<<<<<<< HEAD

class NumpyEncoder(json.JSONEncoder):
    """from https://stackoverflow.com/a/47626762/10307491"""
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


=======
    
>>>>>>> dc37c4c (inference best models stanza, procedure)
def main():
    args = parse_args()    
    
    pipeline, model, tokenizer = get_pipeline(args.model_path, args.dataset_name, args.output_type)
    
    data_files, text_col, label_col, id_col = get_data_files_by_task(args.dataset_name)

    dataset = load_data(data_files)
    dataset = dataset[args.data_split]

    data_collator = DataCollatorForTokenClassification(tokenizer)
    label_list = [pipeline.model.config.id2label[k] for k in pipeline.model.config.id2label]
    b_to_i_label = []
    for idx, label in enumerate(label_list):
        if label.startswith("B-") and label.replace("B-", "I-") in label_list:
            b_to_i_label.append(label_list.index(label.replace("B-", "I-")))
        else:
            b_to_i_label.append(idx)
    data_collator = DataCollatorForTokenClassification(tokenizer)
    dataset = dataset.map(
        tokenize_and_align_labels,
        fn_kwargs={
            'tokenizer': pipeline.tokenizer,
            'text_column_name': text_col,
            'label_column_name': label_col,
            'max_seq_length': None,
            'label_to_id': pipeline.model.config.label2id,
            'b_to_i_label': b_to_i_label,
            'label_all_tokens': False,
        },
        batched=True,
        desc="Running tokenizer on validation dataset",
        )
    dataset = dataset.remove_columns(['ner','words'])
    
    dl = DataLoader(dataset, 
                    sampler=SequentialSampler(dataset),
                    batch_size=1,
                    collate_fn=data_collator)
    model.to('cuda:0')
    preds = {}
    preds['id2labeldict'] = pipeline.model.config.id2label
    for i,batch in enumerate(dl):
        preds[i] = {}
        preds[i]['input_ids'] = batch['input_ids'].numpy().tolist()[0]
        preds[i]['labels'] = batch['labels'].numpy().tolist()[0]
        
        output = model(**{k:v.to('cuda:0') for k,v in batch.items()})
        logits = output.logits[0]
        softmax = F.softmax(logits, dim=1)
        preds[i]['logits'] = logits.cpu().detach().numpy()
        preds[i]['softmax'] = softmax.cpu().detach().numpy()
        preds[i]['pred_labels'] = softmax.argmax(axis=1).tolist()

    # if id_col is not None:
    #     row_ids = dataset[id_col]
    # else:
    #     row_ids = list(range(len(dataset)))

    # preds_dict = {row_id:pred for row_id, pred in zip(row_ids, predictions)}

    # Save predictions
    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)
    with open(os.path.join(args.output_dir, 'predictions.json'), 'w') as f:
        json_string = json.dumps(preds, cls=NumpyEncoder)
        f.write(json_string)
    

if __name__=='__main__':
    main()