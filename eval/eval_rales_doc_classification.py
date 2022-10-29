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
from constants import TRANSFORMERS_DOWNLOAD_PATH, STANFORD_BODYCT_PROTOCOL_DIR, MIMIC_PROTOCOLING_DIR
from omegaconf import OmegaConf, dictconfig
# from ray.tune.schedulers import PopulationBasedTraining
# from ray import tune
import wandb

def load_data(fpaths):
    """
    Load data from a filepath
    """
    
    if isinstance(fpaths, dictconfig.DictConfig):
        
        return load_dataset('csv', data_files=fpaths)
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
    eval_datasets: ['stanford_body_ct_protocol']
    output_dir: '../results/classification'
    seed: 3751

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
    if task == 'stanford_body_ct_protocol':
        return {'train': os.path.join(STANFORD_BODYCT_PROTOCOL_DIR, 'body_ct_protocols_ge_train.csv'),
                'test':os.path.join(STANFORD_BODYCT_PROTOCOL_DIR, 'body_ct_protocols_ge_test.csv')}
    elif task == 'mimiciii_ct_procedure':
        return {'train': os.path.join(MIMIC_PROTOCOLING_DIR, 'mimiciii_ct_procedure_train.csv'), 
                'val':   os.path.join(MIMIC_PROTOCOLING_DIR, 'mimiciii_ct_procedure_dev.csv'), 
                'test': os.path.join(MIMIC_PROTOCOLING_DIR, 'mimiciii_ct_procedure_test.csv')}
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

    config.data_files = get_data_files_by_task(task)
    # set seed
    set_seed(config.seed)
    # load data
    data = load_data(config.data_files)
    print(data)
    exit()
    train_data = data['train']
    for label_col in [x for x in train_data['train'].features if 'label' in x]: #train 1 classifier per label class
        cols_to_remove = [x for x in train_data['train'].features if (x != label_col) & ('label' in x)]
        train_data_tmp = train_data.remove_columns(cols_to_remove)
        test_data_tmp = test_data.remove_columns(cols_to_remove)
        
        new_features = train_data_tmp['train'].features.copy()
        class_labels = list(set(train_data_tmp['train'][label_col]))
        n_labels = len(class_labels)
        new_features[label_col] = ClassLabel(names=class_labels)
        train_data_tmp['train'] = train_data_tmp['train'].cast(new_features)
        test_data_tmp['test'] = test_data_tmp['test'].cast(new_features)

        train_data_tmp['train'] = train_data_tmp['train'].rename_column(label_col, 'label')
        test_data_tmp['test'] = test_data_tmp['test'].rename_column(label_col, 'label')
        train_data_tmp['train'] = train_data_tmp['train'].rename_column(config.dataset_text_col, 'text')
        test_data_tmp['test'] = test_data_tmp['test'].rename_column(config.dataset_text_col, 'text')
    
        if 'val' not in train_data_tmp and 'test' not in train_data_tmp:
            train_data_tmp = train_data_tmp['train'].train_test_split(test_size=0.2, shuffle=True, seed=config.seed, stratify_by_column='label')


        # load tokenizer
        if config.tokenizer_path.endswith('.json'):
            tokenizer = ElectraTokenizerFast(tokenizer_file=config.tokenizer_path)
        else:
            tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_path, cache_dir=config.cache_dir)

        def preprocess_fn(x):
            return tokenizer(x['text'], truncation=True)

        tokenized_train_data = train_data_tmp.map(preprocess_fn, batched=True)
        tokenized_test_data = test_data_tmp.map(preprocess_fn, batched=True)
        
        data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

        # load model
        def init_model():
            return AutoModelForSequenceClassification.from_pretrained(config.model_name_or_path, cache_dir=config.cache_dir, num_labels=n_labels)

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
            # results['f1'] = f1score.compute(predictions=predictions, references=labels, average=None)
            results['f1_micro'] = f1score.compute(predictions=predictions, references=labels, average='micro')['f1']
            results['f1_macro'] = f1score.compute(predictions=predictions, references=labels, average='macro')['f1']
            # results['roc_auc'] = auroc.compute(predictions=predictions, references=labels)
            results['matthews_correlation'] = matthews.compute(predictions=predictions, references=labels)['matthews_correlation']
            
            return results

        # define train args
        train_args = TrainingArguments(
            output_dir=f'{config.output_dir}_{config.eval_name}_{label_col}',
            overwrite_output_dir=True,
            do_eval=True,
            evaluation_strategy='epoch',
            logging_strategy='epoch',
            save_strategy='epoch',
            save_total_limit=1,
            load_best_model_at_end=True,
            metric_for_best_model='eval_accuracy',
        )

        trainer = Trainer(
            model_init=init_model,
            args=train_args,
            train_dataset=tokenized_train_data['train'],
            eval_dataset=tokenized_train_data['test'],
            tokenizer=tokenizer,
            data_collator=data_collator,
            compute_metrics=compute_metrics,
        )
        def hp_space(trial):
            return {
                "learning_rate": trial.suggest_float("learning_rate", 1e-6, 1e-4, log=True),
                "num_train_epochs": trial.suggest_int("num_train_epochs", 3, 6),
                "per_device_train_batch_size": trial.suggest_categorical("per_device_train_batch_size", [8192, 16384]),
                "weight_decay": trial.suggest_float("weight_decay", 1e-12, 1e-1, log=True)
            }
        # scheduler = PopulationBasedTraining(
        #     mode='max',
        #     metric='mean_accuracy',
        #     perturbation_interval=2,
        #     hyperparam_mutations={
        #         'learning_rate': tune.loguniform(1e-6, 1e-2),
        #         'weight_decay': tune.uniform(1e-12, 1e-1),
        #         'per_device_train_batch_size': tune.choice([8,16,32]),
        #         'num_train_epochs': tune.choice([2,3,4,5,6,7,8,9,10]),
        #     },
        # )
        best_model = trainer.hyperparameter_search(
            direction='maximize',
            n_trials=1, 
            # backend='ray',
            hp_space=hp_space,
            compute_objective= lambda metrics: metrics['eval_accuracy']
            # scheduler=scheduler,
            )

        # evaluate best model
        # trainer.test(best_model)
if __name__=='__main__':
    main()