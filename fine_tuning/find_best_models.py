"""
Navigates results directory and identifies the best model for each task and model type.
"""
import os
import transformers
import json
import argparse
import pandas as pd

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--results_dir', type=str, default='../results/ner/')
<<<<<<< HEAD
    
=======
    parser.add_argument('--output_dir', type=str, default='./classification/')
>>>>>>> 718153e (updated stanza hyperparameter search)
    args = parser.parse_args()
    return args

def flatten(l):
    """
    Flattens a list of lists
    """
    return [item for sublist in l for item in sublist]

def splitall(dir_path, all_parts=[]):
    """
    Returns a list of all subdirectories in a path
    """
    if dir_path == '':
        return all_parts
    elif os.path.split(dir_path)[0] == dir_path:
        return [dir_path] + all_parts
    
    (head, tail) = os.path.split(dir_path)
    return splitall(head,[tail]+all_parts)


def get_grouped_results_dirs(dirs, exp_name='mimiciii_ct_procedure'):
    """
    Returns a dictionary mapping an experiment name to a list of results directories
    """
    grouped_results_dirs = {}
    # find experiment names (formatted as expName_datasetName)
    dirs_split = [splitall(d) for d in dirs]
    experiment_names = set([x for x in flatten(dirs_split) if exp_name in x])
    
    # find dirs that group results for each experiment
    grouped_results_dirs = {x:[] for x in experiment_names}
    for d in dirs_split:
        for i,w in enumerate(d):
            if w in experiment_names:
                grouped_results_dirs[w] =os.path.join(*d[:i+1])
    
    return grouped_results_dirs

def find_best_subdir(experiment_path):
    """
    Returns path to subdirectory containing best results for a given experiment_path
    """
    # find all subdirectories
    subdirs = [root for root, dirs, files in os.walk(experiment_path) if 'trainer_state.json' in files]
    # find best subdirectory
    best_subdir = None
    best_metric = 0
    for subdir in subdirs:
        # load trainer state
        with open(os.path.join(subdir,'trainer_state.json'),'r') as f:
            trainer_state = json.load(f)
        # find best metric
        if trainer_state['best_metric'] >= best_metric:
            best_metric = trainer_state['best_metric']
            best_subdir = subdir
    print(best_subdir)
    best_subdir = os.path.abspath(best_subdir)
    return best_subdir, best_metric

def get_best_results(results_dir, exp_name='mimiciii_ct_procedure'):
    """
    Returns a dictionary mapping an experiment name to a list of results directories
    """
    # find all experiments
    results_dirs = [root for root, dirs, files in os.walk(results_dir) if 'trainer_state.json' in files]
    grouped_results_dirs = get_grouped_results_dirs(results_dirs, exp_name=exp_name)
    best_results = {}
    for k in grouped_results_dirs.keys():
        best_subdir, best_metric = find_best_subdir(grouped_results_dirs[k])
        best_results[k] = {'best_metric':f'{best_metric:.2%}', 'best_subdir':best_subdir}
    return best_results

def get_best_results_dygiepp(results_dir, exp_name):
    #find all relevant experiments
    if '_' in exp_name:
        experiment_names_parts = exp_name.split('_')
        relevant_subdirs = [x for x in os.listdir(results_dir) if experiment_names_parts[0] in x and experiment_names_parts[1] in x]
    else:
        relevant_subdirs = [x for x in os.listdir(results_dir) if x.startswith(exp_name)]

    grouped_subdirs = [(x.split('_')[1],x) for x in relevant_subdirs]
    grouped_subdirs_dict = {}
    for x in grouped_subdirs:
        if x[0] not in grouped_subdirs_dict:
            grouped_subdirs_dict[x[0]] = []
        grouped_subdirs_dict[x[0]] += [x[1]]
    
    # find best subdir for each experiment
    best_subdirs = {}
    for model in grouped_subdirs_dict:
        best_metric = 0
        best_subdir = None
        for exp in grouped_subdirs_dict[model]:
            subdir = os.path.join(results_dir, exp)
            try:
                with open(os.path.join(subdir,'metrics.json'),'r') as f:
                    trainer_state = json.load(f)
                if trainer_state['validation__MEAN__ner_f1'] >= best_metric:
                    best_metric = trainer_state['validation__MEAN__ner_f1']
                    best_subdir = subdir
            except:
                print(f'No metrics.json found in {subdir}')
        best_subdirs[model] = {'best_metric':f'{best_metric:.2%}', 'best_subdir':best_subdir}

    return best_subdirs


def main(): 
    args = parse_args()

    # get best results
    
    # best_results = get_best_results(args.results_dir, exp_name='mimiciii_ct_procedure_10pct')
    # pd.DataFrame(best_results).T.to_csv('../results/best_results_procedure_10pct.csv')
    
    # best_results = get_best_results(args.results_dir, exp_name='mimiciii_ct_procedure_1pct')
    # pd.DataFrame(best_results).T.to_csv('../results/best_results_procedure_1pct.csv')

    # best_results = get_best_results(args.results_dir, exp_name='stanza_ner_1pct')
    # pd.DataFrame(best_results).T.to_csv('../results/best_results_stanza_1pct.csv')
    
    # best_results = get_best_results(args.results_dir, exp_name='stanza_ner_10pct')
    # pd.DataFrame(best_results).T.to_csv('../results/best_results_stanza_10pct.csv')

    # best_results = get_best_results(args.results_dir, exp_name='stanza_ner')
    # pd.DataFrame(best_results).T.to_csv('../results/best_results_stanza_lp.csv')
    
    # best_results = get_best_results(args.results_dir, exp_name='mimiciii_ct_procedure')
    # pd.DataFrame(best_results).T.to_csv('../results/best_results_procedure_lp.csv')
    
    best_results = get_best_results_dygiepp(args.results_dir, exp_name='radgraph_lp')
    pd.DataFrame(best_results).T.to_csv('../results/best_results_radgraph_lp.csv')

    best_results = get_best_results_dygiepp(args.results_dir, exp_name='radgraph10pct')
    pd.DataFrame(best_results).T.to_csv('../results/best_results_radgraph_10pct.csv')

    # best_results = get_best_results_dygiepp(args.results_dir, exp_name='radgraph1pct')
    # pd.DataFrame(best_results).T.to_csv('../results/best_results_radgraph_1pct.csv')

    # best_results = get_best_results_dygiepp(args.results_dir, exp_name='radsprl_lp')
    # pd.DataFrame(best_results).T.to_csv('../results/best_results_radsprl_lp.csv')

    best_results = get_best_results_dygiepp(args.results_dir, exp_name='radsprl10pct')
    pd.DataFrame(best_results).T.to_csv('../results/best_results_radsprl_10pct.csv')

    # best_results = get_best_results_dygiepp(args.results_dir, exp_name='radsprl1pct')
    # pd.DataFrame(best_results).T.to_csv('../results/best_results_radsprl_1pct.csv')
if __name__=='__main__':
    main()