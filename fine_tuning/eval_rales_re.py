"""
Perform evaluation on RaLEs RE tasks

Adapted from:
https://github.com/thunlp/PL-Marker/blob/master/run_re.py  (b4863d4)

Changes:
    -adding specific path for cache
"""

# coding=utf-8
# Copyright 2018 The Google AI Language Team Authors and The HuggingFace Inc. team.
# Copyright (c) 2018, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import, division, print_function

import argparse
import glob
import logging
import os
import random
from collections import defaultdict
import re
import shutil

import numpy as np
import torch
from torch.utils.data import (DataLoader, RandomSampler, SequentialSampler,
                              TensorDataset)
from torch.utils.data.distributed import DistributedSampler
from tqdm import tqdm, trange
import time
from transformers import (WEIGHTS_NAME, BertConfig,
                                  BertTokenizer,
                                  RobertaConfig,
                                  RobertaTokenizer,
                                  get_linear_schedule_with_warmup,
                                  AdamW,
                                  AlbertConfig,
                                  AlbertTokenizer,
                                  )
from utils.models import AutoPLMarkerModelForRE

from transformers import AutoConfig, AutoTokenizer
from torch.utils.data import TensorDataset, Dataset
import json
import pickle
import numpy as np
import unicodedata
import itertools
import timeit
import sys
from tqdm import tqdm

logger = logging.getLogger(__name__)
from constants import TRANSFORMERS_DOWNLOAD_PATH, RADGRAPH_DIR

# ALL_MODELS = sum((tuple(conf.pretrained_config_archive_map.keys()) for conf in (BertConfig,  AlbertConfig)), ())

MODEL_CLASSES = {
    # 'bertsub': (BertConfig, BertForACEBothOneDropoutSub, BertTokenizer),
    # 'bertnonersub': (BertConfig, BertForACEBothOneDropoutSubNoNer, BertTokenizer),
    # 'albertsub': (AlbertConfig, AlbertForACEBothOneDropoutSub, AlbertTokenizer),
    'auto': (AutoConfig, AutoPLMarkerModelForRE, AutoTokenizer),
}

task_ner_labels = {
    'radsprl': [''],
    'radgraph': ['ANAT-DP','OBS-DA','OBS-DP','OBS-U'],
}

task_rel_labels = {
    'radgraph': ['PER-SOC', 'OTHER-AFF', 'ART', 'GPE-AFF', 'EMP-ORG', 'PHYS'],
    'radsprl': ['located_at','suggestive_of','modify'],
}

def set_seed(args):
    random.seed(args.seed)
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)
    if args.n_gpu > 0:
        torch.cuda.manual_seed_all(args.seed)



def _rotate_checkpoints(args, checkpoint_prefix, use_mtime=False):
    if not args.save_total_limit:
        return
    if args.save_total_limit <= 0:
        return

    # Check if we should delete older checkpoint(s)
    glob_checkpoints = glob.glob(os.path.join(args.output_dir, '{}-*'.format(checkpoint_prefix)))
    if len(glob_checkpoints) <= args.save_total_limit:
        return

    ordering_and_checkpoint_path = []
    for path in glob_checkpoints:
        if use_mtime:
            ordering_and_checkpoint_path.append((os.path.getmtime(path), path))
        else:
            regex_match = re.match('.*{}-([0-9]+)'.format(checkpoint_prefix), path)
            if regex_match and regex_match.groups():
                ordering_and_checkpoint_path.append((int(regex_match.groups()[0]), path))

    checkpoints_sorted = sorted(ordering_and_checkpoint_path)
    checkpoints_sorted = [checkpoint[1] for checkpoint in checkpoints_sorted]
    number_of_checkpoints_to_delete = max(0, len(checkpoints_sorted) - args.save_total_limit)
    checkpoints_to_be_deleted = checkpoints_sorted[:number_of_checkpoints_to_delete]
    for checkpoint in checkpoints_to_be_deleted:
        logger.info("Deleting older checkpoint [{}] due to args.save_total_limit".format(checkpoint))
        shutil.rmtree(checkpoint)

def train(args, model, tokenizer):
    """ Train the model """
    if args.local_rank in [-1, 0]:
        tb_writer = SummaryWriter("logs/"+args.data_dir[max(args.data_dir.rfind('/'),0):]+"_re_logs/"+args.output_dir[args.output_dir.rfind('/'):])

    args.train_batch_size = args.per_gpu_train_batch_size * max(1, args.n_gpu)

    train_dataset = RadGraphREDataset(tokenizer=tokenizer, args=args, max_pair_length=args.max_pair_length)

    train_sampler = RandomSampler(train_dataset) if args.local_rank == -1 else DistributedSampler(train_dataset)
    train_dataloader = DataLoader(train_dataset, sampler=train_sampler, batch_size=args.train_batch_size, num_workers=4*int(args.output_dir.find('test')==-1))

    if args.max_steps > 0:
        t_total = args.max_steps
        args.num_train_epochs = args.max_steps // (len(train_dataloader) // args.gradient_accumulation_steps) + 1
    else:
        t_total = len(train_dataloader) // args.gradient_accumulation_steps * args.num_train_epochs

    # Prepare optimizer and schedule (linear warmup and decay)
    no_decay = ['bias', 'LayerNorm.weight']
    optimizer_grouped_parameters = [
        {'params': [p for n, p in model.named_parameters() if not any(nd in n for nd in no_decay)], 'weight_decay': args.weight_decay},
        {'params': [p for n, p in model.named_parameters() if any(nd in n for nd in no_decay)], 'weight_decay': 0.0}
        ]
    
    optimizer = AdamW(optimizer_grouped_parameters, lr=args.learning_rate, eps=args.adam_epsilon)
    if args.warmup_steps==-1:
        scheduler = get_linear_schedule_with_warmup(
            optimizer, num_warmup_steps=int(0.1*t_total), num_training_steps=t_total
        )
    else:
        scheduler = get_linear_schedule_with_warmup(
            optimizer, num_warmup_steps=args.warmup_steps, num_training_steps=t_total
        )

    if args.fp16:
        try:
            from apex import amp
        except ImportError:
            raise ImportError("Please install apex from https://www.github.com/nvidia/apex to use fp16 training.")
        model, optimizer = amp.initialize(model, optimizer, opt_level=args.fp16_opt_level)
    # ori_model = model
    # multi-gpu training (should be after apex fp16 initialization)
    if args.n_gpu > 1:
        model = torch.nn.DataParallel(model)

    # Distributed training (should be after apex fp16 initialization)
    if args.local_rank != -1:
        model = torch.nn.parallel.DistributedDataParallel(model, device_ids=[args.local_rank],
                                                          output_device=args.local_rank,
                                                          find_unused_parameters=True)

    # Train!
    logger.info("***** Running training *****")
    logger.info("  Num examples = %d", len(train_dataset))
    logger.info("  Num Epochs = %d", args.num_train_epochs)
    logger.info("  Instantaneous batch size per GPU = %d", args.per_gpu_train_batch_size)
    logger.info("  Total train batch size (w. parallel, distributed & accumulation) = %d",
                   args.train_batch_size * args.gradient_accumulation_steps * (torch.distributed.get_world_size() if args.local_rank != -1 else 1))
    logger.info("  Gradient Accumulation steps = %d", args.gradient_accumulation_steps)
    logger.info("  Total optimization steps = %d", t_total)

    global_step = 0
    tr_loss, logging_loss = 0.0, 0.0
    tr_ner_loss, logging_ner_loss = 0.0, 0.0
    tr_re_loss, logging_re_loss = 0.0, 0.0

    model.zero_grad()
    train_iterator = trange(int(args.num_train_epochs), desc="Epoch", disable=args.local_rank not in [-1, 0])
    set_seed(args)  # Added here for reproductibility (even between python 2 and 3)
    best_f1 = -1



    for _ in train_iterator:
        if args.shuffle and _ > 0:
            train_dataset.initialize()
        epoch_iterator = tqdm(train_dataloader, desc="Iteration", disable=args.local_rank not in [-1, 0])
        for step, batch in enumerate(epoch_iterator):

            model.train()
            batch = tuple(t.to(args.device) for t in batch)

            inputs = {'input_ids':      batch[0],
                      'attention_mask': batch[1],
                      'position_ids':   batch[2],
                      'labels':         batch[5],
                      'ner_labels':     batch[6],
                      }


            inputs['sub_positions'] = batch[3]
            if args.model_type.find('span')!=-1:
                inputs['mention_pos'] = batch[4]
            if args.model_type.endswith('bertonedropoutnersub'):
                inputs['sub_ner_labels'] = batch[7]

            outputs = model(**inputs)
            loss = outputs[0]  # model outputs are always tuple in pytorch-transformers (see doc)
            re_loss = outputs[1]
            ner_loss = outputs[2]

            if args.n_gpu > 1:
                loss = loss.mean() # mean() to average on multi-gpu parallel training
            if args.gradient_accumulation_steps > 1:
                loss = loss / args.gradient_accumulation_steps
                re_loss = re_loss / args.gradient_accumulation_steps
                ner_loss = ner_loss / args.gradient_accumulation_steps

            if args.fp16:
                with amp.scale_loss(loss, optimizer) as scaled_loss:
                    scaled_loss.backward()
            else:
                loss.backward()

            tr_loss += loss.item()
            if re_loss > 0:
                tr_re_loss += re_loss.item()
            if ner_loss > 0:
                tr_ner_loss += ner_loss.item()


            if (step + 1) % args.gradient_accumulation_steps == 0:
                if args.max_grad_norm > 0:
                    if args.fp16:
                        torch.nn.utils.clip_grad_norm_(amp.master_params(optimizer), args.max_grad_norm)
                    else:
                        torch.nn.utils.clip_grad_norm_(model.parameters(), args.max_grad_norm)

                optimizer.step()
                scheduler.step()  # Update learning rate schedule
                model.zero_grad()
                global_step += 1

                # if args.model_type.endswith('rel') :
                #     ori_model.bert.encoder.layer[args.add_coref_layer].attention.self.relative_attention_bias.weight.data[0].zero_() # 可以手动乘个mask

                if args.local_rank in [-1, 0] and args.logging_steps > 0 and global_step % args.logging_steps == 0:
                    # Log metrics
                    tb_writer.add_scalar('lr', scheduler.get_lr()[0], global_step)
                    tb_writer.add_scalar('loss', (tr_loss - logging_loss)/args.logging_steps, global_step)
                    logging_loss = tr_loss

                    tb_writer.add_scalar('RE_loss', (tr_re_loss - logging_re_loss)/args.logging_steps, global_step)
                    logging_re_loss = tr_re_loss

                    tb_writer.add_scalar('NER_loss', (tr_ner_loss - logging_ner_loss)/args.logging_steps, global_step)
                    logging_ner_loss = tr_ner_loss


                if args.local_rank in [-1, 0] and args.save_steps > 0 and global_step % args.save_steps == 0: # valid for bert/spanbert
                    update = True
                    # Save model checkpoint
                    if args.evaluate_during_training:  # Only evaluate when single GPU otherwise metrics may not average well
                        results = evaluate(args, model, tokenizer)
                        f1 = results['f1_with_ner']
                        tb_writer.add_scalar('f1_with_ner', f1, global_step)

                        if f1 > best_f1:
                            best_f1 = f1
                            print ('Best F1', best_f1)
                        else:
                            update = False

                    if update:
                        checkpoint_prefix = 'checkpoint'
                        output_dir = os.path.join(args.output_dir, '{}-{}'.format(checkpoint_prefix, global_step))
                        if not os.path.exists(output_dir):
                            os.makedirs(output_dir)
                        model_to_save = model.module if hasattr(model, 'module') else model  # Take care of distributed/parallel training

                        model_to_save.save_pretrained(output_dir)

                        torch.save(args, os.path.join(output_dir, 'training_args.bin'))
                        logger.info("Saving model checkpoint to %s", output_dir)

                        _rotate_checkpoints(args, checkpoint_prefix)

            if args.max_steps > 0 and global_step > args.max_steps:
                epoch_iterator.close()
                break
        if args.max_steps > 0 and global_step > args.max_steps:
            train_iterator.close()
            break

    if args.local_rank in [-1, 0]:
        tb_writer.close()


    return global_step, tr_loss / global_step, best_f1

def to_list(tensor):
    return tensor.detach().cpu().tolist()

def evaluate(args, model, tokenizer, prefix="", do_test=False):

    eval_output_dir = args.output_dir

    eval_dataset = RadGraphREDataset(tokenizer=tokenizer, args=args, evaluate=True, do_test=do_test, max_pair_length=args.max_pair_length)
    golden_labels = set(eval_dataset.golden_labels)
    golden_labels_withner = set(eval_dataset.golden_labels_withner)
    label_list = list(eval_dataset.label_list)
    sym_labels = list(eval_dataset.sym_labels)
    tot_recall = eval_dataset.tot_recall

    if not os.path.exists(eval_output_dir) and args.local_rank in [-1, 0]:
        os.makedirs(eval_output_dir)

    args.eval_batch_size = args.per_gpu_eval_batch_size * max(1, args.n_gpu)


    scores = defaultdict(dict)
    # ner_pred = not args.model_type.endswith('noner')
    example_subs = set([])
    num_label = len(label_list)

    logger.info("***** Running evaluation {} *****".format(prefix))
    logger.info("  Batch size = %d", args.eval_batch_size)

    model.eval()

    eval_sampler = SequentialSampler(eval_dataset) 
    eval_dataloader = DataLoader(eval_dataset, sampler=eval_sampler, batch_size=args.eval_batch_size,  collate_fn=RadGraphREDataset.collate_fn, num_workers=4*int(args.output_dir.find('test')==-1))

    # Eval!
    logger.info("  Num examples = %d", len(eval_dataset))

    start_time = timeit.default_timer() 

    for batch in tqdm(eval_dataloader, desc="Evaluating"):
        indexs = batch[-3]
        subs = batch[-2]
        batch_m2s = batch[-1]
        ner_labels = batch[6]

        batch = tuple(t.to(args.device) for t in batch[:-3])

        with torch.no_grad():
            inputs = {'input_ids':      batch[0],
                    'attention_mask': batch[1],
                    'position_ids':   batch[2],
                    #   'labels':         batch[4],
                    #   'ner_labels':     batch[5],
                    }

            inputs['sub_positions'] = batch[3]
            if args.model_type.find('span')!=-1:
                inputs['mention_pos'] = batch[4]

            outputs = model(**inputs)

            logits = outputs[0]

            if args.eval_logsoftmax:  # perform a bit better
                logits = torch.nn.functional.log_softmax(logits, dim=-1)

            elif args.eval_softmax:
                logits = torch.nn.functional.softmax(logits, dim=-1)

            if args.use_ner_results or args.model_type.endswith('nonersub'):                 
                ner_preds = ner_labels
            else:
                ner_preds = torch.argmax(outputs[1], dim=-1)
            logits = logits.cpu().numpy()
            ner_preds = ner_preds.cpu().numpy()
            for i in range(len(indexs)):
                index = indexs[i]
                sub = subs[i]
                m2s = batch_m2s[i]
                example_subs.add(((index[0], index[1]), (sub[0], sub[1])))
                for j in range(len(m2s)):
                    obj = m2s[j]
                    ner_label = eval_dataset.ner_label_list[ner_preds[i,j]]
                    scores[(index[0], index[1])][( (sub[0], sub[1]), (obj[0], obj[1]))] = (logits[i, j].tolist(), ner_label)
            
    cor = 0 
    tot_pred = 0
    cor_with_ner = 0
    global_predicted_ners = eval_dataset.global_predicted_ners
    ner_golden_labels = eval_dataset.ner_golden_labels
    ner_cor = 0 
    ner_tot_pred = 0
    ner_ori_cor = 0
    tot_output_results = defaultdict(list)
    if not args.eval_unidirect:     # eval_unidrect is for ablation study
        # print (len(scores))
        for example_index, pair_dict in sorted(scores.items(), key=lambda x:x[0]):  
            visited  = set([])
            sentence_results = []
            for k1, (v1, v2_ner_label) in pair_dict.items():
                
                if k1 in visited:
                    continue
                visited.add(k1)

                if v2_ner_label=='NIL':
                    continue
                v1 = list(v1)
                m1 = k1[0]
                m2 = k1[1]
                if m1 == m2:
                    continue
                k2 = (m2, m1)
                v2s = pair_dict.get(k2, None)
                if v2s is not None:
                    visited.add(k2)
                    v2, v1_ner_label = v2s
                    v2 = v2[ : len(sym_labels)] + v2[num_label:] + v2[len(sym_labels) : num_label]

                    for j in range(len(v2)):
                        v1[j] += v2[j]
                else:
                    assert ( False )

                if v1_ner_label=='NIL':
                    continue

                pred_label = np.argmax(v1)
                if pred_label>0:
                    if pred_label >= num_label:
                        pred_label = pred_label - num_label + len(sym_labels)
                        m1, m2 = m2, m1
                        v1_ner_label, v2_ner_label = v2_ner_label, v1_ner_label

                    pred_score = v1[pred_label]

                    sentence_results.append( (pred_score, m1, m2, pred_label, v1_ner_label, v2_ner_label) )

            sentence_results.sort(key=lambda x: -x[0])
            no_overlap = []
            def is_overlap(m1, m2):
                if m2[0]<=m1[0] and m1[0]<=m2[1]:
                    return True
                if m1[0]<=m2[0] and m2[0]<=m1[1]:
                    return True
                return False

            output_preds = []

            for item in sentence_results:
                m1 = item[1]
                m2 = item[2]
                overlap = False
                for x in no_overlap:
                    _m1 = x[1]
                    _m2 = x[2]
                    # same relation type & overlap subject & overlap object --> delete
                    if item[3]==x[3] and (is_overlap(m1, _m1) and is_overlap(m2, _m2)):
                        overlap = True
                        break

                pred_label = label_list[item[3]]


                if not overlap:
                    no_overlap.append(item)

            pos2ner = {}

            for item in no_overlap:
                m1 = item[1]
                m2 = item[2]
                pred_label = label_list[item[3]]
                tot_pred += 1
                if pred_label in sym_labels:
                    tot_pred += 1 # duplicate
                    if (example_index, m1, m2, pred_label) in golden_labels or (example_index, m2, m1, pred_label) in golden_labels:
                        cor += 2
                else:
                    if (example_index, m1, m2, pred_label) in golden_labels:
                        cor += 1        

                if m1 not in pos2ner:
                    pos2ner[m1] = item[4]
                if m2 not in pos2ner:
                    pos2ner[m2] = item[5]

                output_preds.append((m1, m2, pred_label))
                if pred_label in sym_labels:
                    if (example_index, (m1[0], m1[1], pos2ner[m1]), (m2[0], m2[1], pos2ner[m2]), pred_label) in golden_labels_withner  \
                            or (example_index,  (m2[0], m2[1], pos2ner[m2]), (m1[0], m1[1], pos2ner[m1]), pred_label) in golden_labels_withner:
                        cor_with_ner += 2
                else:  
                    if (example_index, (m1[0], m1[1], pos2ner[m1]), (m2[0], m2[1], pos2ner[m2]), pred_label) in golden_labels_withner:
                        cor_with_ner += 1      

            if do_test:
                #output_w.write(json.dumps(output_preds) + '\n')
                tot_output_results[example_index[0]].append((example_index[1],  output_preds))

            # refine NER results
            ner_results = list(global_predicted_ners[example_index])
            for i in range(len(ner_results)):
                start, end, label = ner_results[i] 
                if (example_index, (start, end), label) in ner_golden_labels:
                    ner_ori_cor += 1
                if (start, end) in pos2ner:
                    label = pos2ner[(start, end)]
                if (example_index, (start, end), label) in ner_golden_labels:
                    ner_cor += 1
                ner_tot_pred += 1
        
    else:

        for example_index, pair_dict in sorted(scores.items(), key=lambda x:x[0]):  
            sentence_results = []
            for k1, (v1, v2_ner_label) in pair_dict.items():
                
                if v2_ner_label=='NIL':
                    continue
                v1 = list(v1)
                m1 = k1[0]
                m2 = k1[1]
                if m1 == m2:
                    continue
              
                pred_label = np.argmax(v1)
                if pred_label>0 and pred_label < num_label:

                    pred_score = v1[pred_label]

                    sentence_results.append( (pred_score, m1, m2, pred_label, None, v2_ner_label) )

            sentence_results.sort(key=lambda x: -x[0])
            no_overlap = []
            def is_overlap(m1, m2):
                if m2[0]<=m1[0] and m1[0]<=m2[1]:
                    return True
                if m1[0]<=m2[0] and m2[0]<=m1[1]:
                    return True
                return False

            output_preds = []

            for item in sentence_results:
                m1 = item[1]
                m2 = item[2]
                overlap = False
                for x in no_overlap:
                    _m1 = x[1]
                    _m2 = x[2]
                    if item[3]==x[3] and (is_overlap(m1, _m1) and is_overlap(m2, _m2)):
                        overlap = True
                        break

                pred_label = label_list[item[3]]

                output_preds.append((m1, m2, pred_label))

                if not overlap:
                    no_overlap.append(item)

            pos2ner = {}
            predpos2ner = {}
            ner_results = list(global_predicted_ners[example_index])
            for start, end, label in ner_results:
                predpos2ner[(start, end)] = label

            for item in no_overlap:
                m1 = item[1]
                m2 = item[2]
                pred_label = label_list[item[3]]
                tot_pred += 1

                if (example_index, m1, m2, pred_label) in golden_labels:
                    cor += 1        

                if m1 not in pos2ner:
                    pos2ner[m1] = predpos2ner[m1]#item[4]

                if m2 not in pos2ner:
                    pos2ner[m2] = item[5]

                # if pred_label in sym_labels:
                #     if (example_index, (m1[0], m1[1], pos2ner[m1]), (m2[0], m2[1], pos2ner[m2]), pred_label) in golden_labels_withner \
                #         or (example_index,  (m2[0], m2[1], pos2ner[m2]), (m1[0], m1[1], pos2ner[m1]), pred_label) in golden_labels_withner:
                #         cor_with_ner += 2
                # else:  
                if (example_index, (m1[0], m1[1], pos2ner[m1]), (m2[0], m2[1], pos2ner[m2]), pred_label) in golden_labels_withner:
                    cor_with_ner += 1      
            
            # refine NER results
            ner_results = list(global_predicted_ners[example_index])
            for i in range(len(ner_results)):
                start, end, label = ner_results[i] 
                if (example_index, (start, end), label) in ner_golden_labels:
                    ner_ori_cor += 1
                if (start, end) in pos2ner:
                    label = pos2ner[(start, end)]
                if (example_index, (start, end), label) in ner_golden_labels:
                    ner_cor += 1
                ner_tot_pred += 1


    evalTime = timeit.default_timer() - start_time
    logger.info("  Evaluation done in total %f secs (%f example per second)", evalTime,  len(global_predicted_ners) / evalTime)

    if do_test:
        output_w = open(os.path.join(args.output_dir, 'pred_results.json'), 'w')
        json.dump(tot_output_results, output_w)

    ner_p = ner_cor / ner_tot_pred if ner_tot_pred > 0 else 0 
    ner_r = ner_cor / len(ner_golden_labels) 
    ner_f1 = 2 * (ner_p * ner_r) / (ner_p + ner_r) if ner_cor > 0 else 0.0

    p = cor / tot_pred if tot_pred > 0 else 0 
    r = cor / tot_recall 
    f1 = 2 * (p * r) / (p + r) if cor > 0 else 0.0
    assert(tot_recall==len(golden_labels))

    p_with_ner = cor_with_ner / tot_pred if tot_pred > 0 else 0 
    r_with_ner = cor_with_ner / tot_recall
    assert(tot_recall==len(golden_labels_withner))
    f1_with_ner = 2 * (p_with_ner * r_with_ner) / (p_with_ner + r_with_ner) if cor_with_ner > 0 else 0.0

    results = {'f1':  f1,  'f1_with_ner': f1_with_ner, 'ner_f1': ner_f1}

    logger.info("Result: %s", json.dumps(results))

    return results



def run_re(eval_name='', task=''):
    parser = argparse.ArgumentParser()

    ## Required parameters
    parser.add_argument("--model_type", default='auto', type=str, required=True,
                        help="Model type selected in the list: " + ", ".join(MODEL_CLASSES.keys()))
    parser.add_argument("--model_name_or_path", default=None, type=str, required=True,
                        help="Path to pre-trained model")
    parser.add_argument("--output_dir", default=None, type=str, required=True,
                        help="The output directory where the model predictions and checkpoints will be written.")

    ## Other parameters
    parser.add_argument("--config_name", default="", type=str,
                        help="Pretrained config name or path if not the same as model_name")
    parser.add_argument("--tokenizer_name", default="", type=str,
                        help="Pretrained tokenizer name or path if not the same as model_name")
    parser.add_argument("--cache_dir", default="", type=str,
                        help="Where do you want to store the pre-trained models downloaded from s3")
    parser.add_argument("--max_seq_length", default=384, type=int,
                        help="The maximum total input sequence length after tokenization. Sequences longer "
                             "than this will be truncated, sequences shorter will be padded.")
    parser.add_argument("--do_train", action='store_true',
                        help="Whether to run training.")
    parser.add_argument("--do_eval", action='store_true',
                        help="Whether to run eval on the dev set.")

    parser.add_argument("--evaluate_during_training", action='store_true',
                        help="Rul evaluation during training at each logging step.")
    parser.add_argument("--do_lower_case", action='store_true',
                        help="Set this flag if you are using an uncased model.")

    parser.add_argument("--per_gpu_train_batch_size", default=8, type=int,
                        help="Batch size per GPU/CPU for training.")
    parser.add_argument("--per_gpu_eval_batch_size", default=8, type=int,
                        help="Batch size per GPU/CPU for evaluation.")
    parser.add_argument('--gradient_accumulation_steps', type=int, default=1,
                        help="Number of updates steps to accumulate before performing a backward/update pass.")
    parser.add_argument("--learning_rate", default=2e-5, type=float,
                        help="The initial learning rate for Adam.")
    parser.add_argument("--weight_decay", default=0.0, type=float,
                        help="Weight deay if we apply some.")
    parser.add_argument("--adam_epsilon", default=1e-8, type=float,
                        help="Epsilon for Adam optimizer.")
    parser.add_argument("--max_grad_norm", default=1.0, type=float,
                        help="Max gradient norm.")
    parser.add_argument("--num_train_epochs", default=10.0, type=float,
                        help="Total number of training epochs to perform.")
    parser.add_argument("--max_steps", default=-1, type=int,
                        help="If > 0: set total number of training steps to perform. Override num_train_epochs.")
    parser.add_argument("--warmup_steps", default=-1, type=int,
                        help="Linear warmup over warmup_steps.")

    parser.add_argument('--logging_steps', type=int, default=5,
                        help="Log every X updates steps.")
    parser.add_argument('--save_steps', type=int, default=1000,
                        help="Save checkpoint every X updates steps.")
    parser.add_argument("--eval_all_checkpoints", action='store_true',
                        help="Evaluate all checkpoints starting with the same prefix as model_name ending and ending with step number")
    parser.add_argument("--no_cuda", action='store_true',
                        help="Avoid using CUDA when available")
    parser.add_argument('--overwrite_output_dir', action='store_true',
                        help="Overwrite the content of the output directory")
    parser.add_argument('--overwrite_cache', action='store_true',
                        help="Overwrite the cached training and evaluation sets")
    parser.add_argument('--seed', type=int, default=42,
                        help="random seed for initialization")

    parser.add_argument('--fp16', action='store_true',
                        help="Whether to use 16-bit (mixed) precision (through NVIDIA apex) instead of 32-bit")
    parser.add_argument('--fp16_opt_level', type=str, default='O1',
                        help="For fp16: Apex AMP optimization level selected in ['O0', 'O1', 'O2', and 'O3']."
                             "See details at https://nvidia.github.io/apex/amp.html")
    parser.add_argument('--server_ip', type=str, default='', help="For distant debugging.")
    parser.add_argument('--server_port', type=str, default='', help="For distant debugging.")
    parser.add_argument('--save_total_limit', type=int, default=1,
                        help='Limit the total amount of checkpoints, delete the older checkpoints in the output_dir, does not delete by default')

    parser.add_argument("--train_file",  default="train.json", type=str)
    parser.add_argument("--dev_file",  default="dev.json", type=str)
    parser.add_argument("--test_file",  default="test.json", type=str)
    parser.add_argument('--max_pair_length', type=int, default=64,  help="")
    parser.add_argument("--alpha", default=1.0, type=float)
    parser.add_argument('--save_results', action='store_true')
    parser.add_argument('--no_test', action='store_true')
    parser.add_argument('--eval_logsoftmax', action='store_true')
    parser.add_argument('--eval_softmax', action='store_true')
    parser.add_argument('--shuffle', action='store_true')
    parser.add_argument('--lminit', action='store_true')
    parser.add_argument('--no_sym', action='store_true')
    parser.add_argument('--att_left', action='store_true')
    parser.add_argument('--att_right', action='store_true')
    parser.add_argument('--use_ner_results', action='store_true')
    parser.add_argument('--use_typemarker', action='store_true')
    parser.add_argument('--eval_unidirect', action='store_true')

    args = parser.parse_args()

    if os.path.exists(args.output_dir) and os.listdir(args.output_dir) and args.do_train and not args.overwrite_output_dir:
        raise ValueError("Output directory ({}) already exists and is not empty. Use --overwrite_output_dir to overcome.".format(args.output_dir))

    def create_exp_dir(path, scripts_to_save=None):
        if args.output_dir.endswith("test"):
            return
        if not os.path.exists(path):
            os.mkdir(path)

        print('Experiment dir : {}'.format(path))
        if scripts_to_save is not None:
            if not os.path.exists(os.path.join(path, 'scripts')):
                os.mkdir(os.path.join(path, 'scripts'))
            for script in scripts_to_save:
                dst_file = os.path.join(path, 'scripts', os.path.basename(script))
                shutil.copyfile(script, dst_file)

    # if args.do_train and args.local_rank in [-1, 0] and args.output_dir.find('test')==-1:
    #     create_exp_dir(args.output_dir, scripts_to_save=['run_re.py', 'transformers/src/transformers/modeling_bert.py', 'transformers/src/transformers/modeling_albert.py'])


    # Setup distant debugging if needed
    if args.server_ip and args.server_port:
        # Distant debugging - see https://code.visualstudio.com/docs/python/debugging#_attach-to-a-local-script
        import ptvsd
        print("Waiting for debugger attach")
        ptvsd.enable_attach(address=(args.server_ip, args.server_port), redirect_output=True)
        ptvsd.wait_for_attach()

    # Setup CUDA, GPU & distributed training
    # if args.local_rank == -1 or args.no_cuda:
    device = torch.device("cuda" if torch.cuda.is_available() and not args.no_cuda else "cpu")
    args.n_gpu = torch.cuda.device_count()
    # else:  # Initializes the distributed backend which will take care of sychronizing nodes/GPUs
    #     torch.cuda.set_device(args.local_rank)
    #     device = torch.device("cuda", args.local_rank)
    #     torch.distributed.init_process_group(backend='nccl')
    #     args.n_gpu = 1
    args.device = device

    # Setup logging
    logging.basicConfig(format = '%(asctime)s - %(levelname)s - %(name)s -   %(message)s',
                        datefmt = '%m/%d/%Y %H:%M:%S',
                        level = logging.INFO) # logging.INFO if args.local_rank in [-1, 0] else
    # logger.warning("Process rank: %s, device: %s, n_gpu: %s, distributed training: %s, 16-bits training: %s",
    #                 args.local_rank, device, args.n_gpu, bool(args.local_rank != -1), args.fp16)

    # Set seed
    set_seed(args)

    if task == 'radgraph':
        num_ner_labels = 4
        num_lables = 4
    elif task == 'radsprl':
        num_ner_labels = 4
        num_labels = 4
    else:
        assert (False)

    # Load pretrained model and tokenizer
    
    args.model_type = args.model_type.lower()

    config_class, model_class, tokenizer_class = MODEL_CLASSES['auto']#MODEL_CLASSES[args.model_type]

    config = config_class.from_pretrained(args.config_name if args.config_name else args.model_name_or_path, num_labels=num_labels)
    tokenizer = tokenizer_class.from_pretrained(args.model_name_or_path,  do_lower_case=args.do_lower_case)

    config.max_seq_length = args.max_seq_length
    config.alpha = args.alpha
    config.num_ner_labels = num_ner_labels

    model = model_class.from_pretrained(args.model_name_or_path, from_tf=bool('.ckpt' in args.model_name_or_path), config=config)


    if args.model_type.startswith('albert'):
        if args.use_typemarker:
            special_tokens_dict = {'additional_special_tokens': ['[unused' + str(x) + ']' for x in range(num_ner_labels*4+2)]}
        else:
            special_tokens_dict = {'additional_special_tokens': ['[unused' + str(x) + ']' for x in range(4)]}
        tokenizer.add_special_tokens(special_tokens_dict)
        # print ('add tokens:', tokenizer.additional_special_tokens)
        # print ('add ids:', tokenizer.additional_special_tokens_ids)
        model.albert.resize_token_embeddings(len(tokenizer))

    if args.do_train:
        subject_id = tokenizer.encode('subject', add_special_tokens=False)
        assert(len(subject_id)==1)
        subject_id = subject_id[0]
        object_id = tokenizer.encode('object', add_special_tokens=False)
        assert(len(object_id)==1)
        object_id = object_id[0]

        mask_id = tokenizer.encode('[MASK]', add_special_tokens=False)
        assert(len(mask_id)==1)
        mask_id = mask_id[0]

        logger.info(" subject_id = %s, object_id = %s, mask_id = %s", subject_id, object_id, mask_id)

        if args.lminit: 
            if args.model_type.startswith('albert'):
                word_embeddings = model.albert.embeddings.word_embeddings.weight.data
                subs = 30000
                sube = 30001
                objs = 30002
                obje = 30003
            else:
                word_embeddings = model.bert.embeddings.word_embeddings.weight.data
                subs = 1
                sube = 2
                objs = 3
                obje = 4

            word_embeddings[subs].copy_(word_embeddings[mask_id])     
            word_embeddings[sube].copy_(word_embeddings[subject_id])   

            word_embeddings[objs].copy_(word_embeddings[mask_id])      
            word_embeddings[obje].copy_(word_embeddings[object_id])     

    if args.local_rank == 0:
        torch.distributed.barrier()  # Make sure only the first process in distributed training will download model & vocab

    model.to(args.device)

    logger.info("Training/evaluation parameters %s", args)
    best_f1 = 0
    # Training
    if args.do_train:
        # train_dataset = load_and_cache_examples(args,  tokenizer, evaluate=False)
        global_step, tr_loss, best_f1 = train(args, model, tokenizer)
        logger.info(" global_step = %s, average loss = %s", global_step, tr_loss)

    # Saving best-practices: if you use defaults names for the model, you can reload it using from_pretrained()
    if args.do_train and (args.local_rank == -1 or torch.distributed.get_rank() == 0):
        # Create output directory if needed
        if not os.path.exists(args.output_dir) and args.local_rank in [-1, 0]:
            os.makedirs(args.output_dir)
        update = True
        if args.evaluate_during_training:
            results = evaluate(args, model, tokenizer)
            f1 = results['f1_with_ner']
            if f1 > best_f1:
                best_f1 = f1
                print ('Best F1', best_f1)
            else:
                update = False

        if update:
            checkpoint_prefix = 'checkpoint'
            output_dir = os.path.join(args.output_dir, '{}-{}'.format(checkpoint_prefix, global_step))
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            model_to_save = model.module if hasattr(model, 'module') else model  # Take care of distributed/parallel training

            model_to_save.save_pretrained(output_dir)

            torch.save(args, os.path.join(output_dir, 'training_args.bin'))
            logger.info("Saving model checkpoint to %s", output_dir)
            _rotate_checkpoints(args, checkpoint_prefix)

        tokenizer.save_pretrained(args.output_dir)

        torch.save(args, os.path.join(args.output_dir, 'training_args.bin'))


    # Evaluation
    results = {'dev_best_f1': best_f1}
    if args.do_eval and args.local_rank in [-1, 0]:

        checkpoints = [args.output_dir]

        WEIGHTS_NAME = 'pytorch_model.bin'

        if args.eval_all_checkpoints:
            checkpoints = list(os.path.dirname(c) for c in sorted(glob.glob(args.output_dir + '/**/' + WEIGHTS_NAME, recursive=True)))

        logger.info("Evaluate the following checkpoints: %s", checkpoints)
        for checkpoint in checkpoints:
            global_step = checkpoint.split('-')[-1] if len(checkpoints) > 1 else ""

            model = model_class.from_pretrained(checkpoint, config=config)

            model.to(args.device)
            result = evaluate(args, model, tokenizer, prefix=global_step, do_test=not args.no_test)
            result = dict((k + '_{}'.format(global_step), v) for k, v in result.items())
            results.update(result)
        print (results)

        if args.no_test:  # choose best resutls on dev set
            bestv = 0
            k = 0
            for k, v in results.items():
                if v > bestv:
                    bestk = k
            print (bestk)

        output_eval_file = os.path.join(args.output_dir, "results.json")
        json.dump(results, open(output_eval_file, "w"))

def do_re_rales(task, config):
    # add the model attributes to arguments for HF argparser compatibility
    print(config)
    
    sys.argv = ['eval_rales_re.py'] 
    sys.argv += ['--model_name_or_path', config['model_name_or_path']]
    sys.argv += ['--tokenizer_name', config['tokenizer_path']]
    sys.argv += ['--cache_dir', config['cache_dir']]
    sys.argv += ['--output_dir', os.path.join(config['output_dir'], config['eval_name']+'_'+task)]
    
    sys.argv += ['--evaluation_strategy', 'epoch']
    sys.argv += ['--logging_strategy', 'epoch']
    sys.argv += ['--save_strategy', 'epoch']
    sys.argv += ['--load_best_model_at_end', 'True']
    sys.argv += ['--metric_for_best_model', 'overall_f1']
    sys.argv += ['--save_total_limit', '1']

    sys.argv += ['--do_train', '--do_eval']
    
    if task == 'radgraph_re':
        train_file = os.path.join(RADGRAPH_DIR, 'train_plmarker_jsonl.json')
        validation_file = os.path.join(RADGRAPH_DIR, 'dev_plmarker_jsonl.json')
        sys.argv += ['--train_file', train_file]
        sys.argv += ['--dev_file', validation_file]
        
        run_re(eval_name=config['eval_name'], task=task)

if __name__ == "__main__":
    run_re()