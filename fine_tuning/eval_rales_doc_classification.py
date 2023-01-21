import logging
import os
import sys
from dataclasses import dataclass, field
from typing import Optional

import datasets
import numpy as np
from datasets import ClassLabel, load_dataset

import evaluate
import transformers
from transformers import (
    AutoConfig,
    AutoModelForSequenceClassification,
    AutoTokenizer,
    DataCollatorWithPadding,
    HfArgumentParser,
    PretrainedConfig,
    PreTrainedTokenizerFast,
    ElectraTokenizerFast,
    Trainer,
    TrainingArguments,
    set_seed,
)
from transformers.trainer_utils import get_last_checkpoint
from transformers.utils import check_min_version, send_example_telemetry
from transformers.utils.versions import require_version
from constants import TRANSFORMERS_DOWNLOAD_PATH, MIMIC_PROTOCOLING_DIR
from omegaconf import OmegaConf, dictconfig
import wandb

def load_data(fpaths):
    """
    Load data from a filepath
    """
    
    if isinstance(fpaths, dictconfig.DictConfig):
        # print(type(dict(fpaths)))
        dset = load_dataset('csv', data_files=dict(fpaths))
        return dset
    elif fpaths[0].endswith('.csv'): #TODO make this compatible with dict not list
        return load_dataset('csv', data_files={'train':[x for x in fpaths if 'train' in x]}), \
                load_dataset('csv', data_files={'test':[x for x in fpaths if 'test' in x]})
    else:
        raise NotImplementedError('Loading data from {} is not implemented'.format(fpaths[0].split('.')[-1]))

def get_default_config():
    """
    Returns OmegaConf object containing default parameters
    """
    default_config = """
    eval_name: rales_eval
    model_name_or_path: bert-base-uncased
    tokenizer_path: bert-base-uncased
    cache_dir: TRANSFORMERS_DOWNLOAD_PATH
    eval_datasets: ['mimiciii_ct_procedure']
    output_dir: '../results/classification'
    seed: 3751

    eval_batch_size: 512
    dataset_text_col: 'order_text'
    """
    return OmegaConf.create(default_config)

def parse_config(config_to_parse):
    """
    Overrides default config with user-provided config
    """
    parsed_config = get_default_config()

    for key in config_to_parse:
        parsed_config[key] = config_to_parse[key]

    return parsed_config

def get_data_files_by_task(task):
    """
    Get the data files for a given task
    """
    if task == 'mimiciii_ct_procedure':
        text_col = 'indication'
        label_col = 'procedure_label'
        to_remove = ['ROW_ID']
        return {'train': os.path.join(MIMIC_PROTOCOLING_DIR, 'mimiciii_ct_procedure_train.csv'), 
                'val':   os.path.join(MIMIC_PROTOCOLING_DIR, 'mimiciii_ct_procedure_dev.csv'), 
                'test': os.path.join(MIMIC_PROTOCOLING_DIR, 'mimiciii_ct_procedure_test.csv')}, text_col, label_col, to_remove
                
    else:
        raise NotImplementedError('Loading data from {} is not implemented'.format(task))

def do_document_classification_rales(task, config=None):
    """
    Performs fine-tuning and evaluation on a given task
    """
    if config is None:
        config = get_default_config()
    else:
        config = parse_config(config)

    config.data_files, text_col, label_col, cols_to_remove = get_data_files_by_task(task)
    # set seed
    set_seed(config.seed)
    # load and format data
    data = load_data(config.data_files)
    data = data.rename_column(text_col,'text').rename_column(label_col,'label')
    # data = data.remove_columns(cols_to_remove)
    n_labels = len(set(data['train']['label']))
    label2id = {label:idx for idx,label in enumerate(set(data['train']['label']))}
    id2label = {idx:label for label,idx in label2id.items()}
    new_features = data['train'].features.copy()
    new_features['label'] = ClassLabel(names=[id2label[idx] for idx in sorted(list(id2label.keys()))])
    data = data.cast(new_features)
    
    # load tokenizer
    tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_path, cache_dir=config.cache_dir)

    def preprocess_fn(x):
        return tokenizer(x['text'], padding=True, truncation=True)

    tokenized_data = data.map(preprocess_fn, batched=True)
    
    data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

    # load model
    def init_model():
        return AutoModelForSequenceClassification.from_pretrained(config.model_name_or_path, cache_dir=config.cache_dir, num_labels=n_labels, label2id=label2id, id2label=id2label)

    # load metrics
    accuracy = evaluate.load('accuracy')
    precision = evaluate.load('precision')
    recall = evaluate.load('recall')
    f1score = evaluate.load('f1')
    auroc = evaluate.load('roc_auc')
    matthews = evaluate.load('matthews_correlation')
    def compute_metrics(eval_pred):
        results = {}
        probs, labels = eval_pred
        predictions = probs.argmax(axis=-1)
        results['accuracy'] = accuracy.compute(predictions=predictions, references=labels)['accuracy']
        results['precision'] = precision.compute(predictions=predictions, references=labels, average='micro')['precision']
        results['recall'] = recall.compute(predictions=predictions, references=labels, average='micro')['recall']
        results['f1_micro'] = f1score.compute(predictions=predictions, references=labels, average='micro')['f1']
        results['f1_macro'] = f1score.compute(predictions=predictions, references=labels, average='macro')['f1']
        results['matthews_correlation'] = matthews.compute(predictions=predictions, references=labels)['matthews_correlation']
        
        return results

    # define train args
    train_args = TrainingArguments(
        output_dir=f'{config.output_dir}_{config.eval_name}_{task}',
        overwrite_output_dir=True,
        do_eval=True,
        evaluation_strategy='epoch',
        logging_strategy='epoch',
        save_strategy='epoch',
        save_total_limit=1,
        load_best_model_at_end=True,
        metric_for_best_model='f1_micro',
        per_device_eval_batch_size=config.eval_batch_size,
    )

    trainer = Trainer(
        model_init=init_model,
        args=train_args,
        train_dataset=tokenized_data['train'],
        eval_dataset=tokenized_data['test'],
        tokenizer=tokenizer,
        data_collator=data_collator,
        compute_metrics=compute_metrics,
    )
    def hp_space(trial):
        """
        formatted as optuna objective (see https://optuna.readthedocs.io/en/stable/tutorial/10_key_features/002_configurations.html#sphx-glr-tutorial-10-key-features-002-configurations-py)
        """
        return {
            "learning_rate": trial.suggest_float("learning_rate", 1e-6, 1e-4, log=True),
            "num_train_epochs": trial.suggest_int("num_train_epochs", 3, 6),
            "per_device_train_batch_size": trial.suggest_categorical("per_device_train_batch_size", [32,64,128]),
            "weight_decay": trial.suggest_float("weight_decay", 1e-12, 1e-1, log=True)
        }

    best_model = trainer.hyperparameter_search(
        direction='maximize',
        n_trials=10, 
        hp_space=hp_space,
        compute_objective= lambda metrics: metrics['eval_accuracy'],
        study_name= f'{config.output_dir}_{config.eval_name}_{task}'
        )

    # evaluate best model
    # trainer.test(best_model)
if __name__=='__main__':
    main()