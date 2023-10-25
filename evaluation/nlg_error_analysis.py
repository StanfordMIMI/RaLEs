import json
import os
import argparse
from report_generation_evaluator import *

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--predictions_path', type=str,  help='file containing model predictions', default="")
    parser.add_argument('--references_path', type=str,  help='file containing ground truth', default="/dataNAS/people/jmz/data/RRS/rales_rrs/BIONLP2023/test.json")
    parser.add_argument('--findings_path', type=str, help='file containing findings', default="/dataNAS/people/jmz/data/RRS/rales_rrs/BIONLP2023/test.json")
    parser.add_argument('--scorers', type=str, nargs='+', default=['bleu','rougel','bertscore','f1radgraph','chexbert','rouge2'], help='list of scorers to use')
    args = parser.parse_args()
    return args

def get_json_dataset_contents(dataset_path):
    """
    Returns the contents of a json dataset as a list of dictionaries
    """
    dataset = load_dataset('json', data_files={'data': dataset_path})['data']
    return dataset

def get_line_dataset_contents(dataset_path):
    """
    Returns the contents of a line dataset as a list of strings
    """
    with open(dataset_path) as f:
        dataset = f.readlines()
    return dataset

def get_prediction_contents(prediction_path):
    """
    Returns the contents of a prediction file as a list of dictionaries
    """
    with open(prediction_path) as f:
        predictions = json.load(f)
    return predictions

def sorted_indices(lst):
    return [i[0] for i in sorted(enumerate(lst), key=lambda x: x[1])]

def print_error_analysis(findings, generations, ground_truths, scores, sorted_idxs, index):
    print('-'*100)
    print("provided findings\n")
    print(findings[sorted_idxs[index]])
    print("prediction\n")
    print(generations[sorted_idxs[index]])
    print("ground truth\n")
    print(ground_truths[sorted_idxs[index]])
    formatted_scores = {k: f"{v:.3f}" for k, v in scores[sorted_idxs[index]].items()}
    print(f"scores: {formatted_scores}")

def main():
    args = parse_args()
    predictions_path = args.predictions_path
    references_path = args.references_path

    if predictions_path.endswith('.json'):
        generations = load_dataset('json', data_files={'data': predictions_path})['data']['predicted_impression']
    elif predictions_path.endswith('.txt'):
        generations = get_line_dataset_contents(predictions_path)
    if references_path.endswith('.json') or references_path.endswith('.jsonl'):
        ground_truths = load_dataset('json', data_files={'data': references_path})['data']['impression']
        findings = load_dataset('json', data_files={'data': references_path})['data']['findings']
    # elif references_path.endswith('.txt'):        
    #     ground_truths = get_line_dataset_contents(references_path)[:10]
    
    evaluator = ReportGenerationEvaluator(scorers=args.scorers)

    if len(generations) > 1000: #pick at random, we don't need to evaluate everything
        import random
        seed = 42
        random.seed(seed)
        indices = random.sample(range(len(generations)), 1000)
        generations = [generations[i] for i in indices]
        ground_truths = [ground_truths[i] for i in indices]

        print("sampling 1000 reports for error analysis")
    
    evaluator = ReportGenerationEvaluator(scorers=args.scorers)

    scores = []
    for i in range(len(generations)):
        scores.append(evaluator.evaluate([generations[i]], [ground_truths[i]]))
    
        # print({k:f'{v:.3f}' for k,v in evaluator.evaluate(generations, ground_truths).items()})
    preferred_metric = 'f1radgraph'
    preferred_scores = [score[preferred_metric] for score in scores]
    sorted_idxs = sorted_indices(preferred_scores)

    print(f"best prediction:")
    print_error_analysis(findings, generations, ground_truths, scores, sorted_idxs, -1)
    print("bad prediction:")
    print_error_analysis(findings, generations, ground_truths, scores, sorted_idxs, int(len(sorted_idxs)/9))
    print("worst prediction:")
    print_error_analysis(findings, generations, ground_truths, scores, sorted_idxs, 0)



if __name__=='__main__':
    main()


"""
python nlg_error_analysis.py --predictions_path /dataNAS/people/jmz/jmz_code/radiology_nlp/vilmedicbackup/ckpt/gatortron_bionlp/test_best-1_549948_hyps.txt --references_path /dataNAS/people/jmz/data/RRS/rales_rrs/BIONLP2023/test.json --findings_path /dataNAS/people/jmz/data/RRS/rales_rrs/BIONLP2023/test.json 

python nlg_error_analysis.py --predictions_path /dataNAS/people/jmz/jmz_code/radiology_nlp/vilmedicbackup/ckpt/rrs_gatortron_32_2/test_best-1_439367_hyps.txt --references_path /dataNAS/people/jmz/data/RRS/rales_rrs/MEDIQA2021/test.json --findings_path /dataNAS/people/jmz/data/RRS/rales_rrs/MEDIQA2021/test.json

Best model:
Bionlp: 
/dataNAS/people/jmz/jmz_code/radiology_nlp/vilmedicbackup/ckpt/gatortron_bionlp/test_best-1_549948_hyps.txt
preds:
/dataNAS/people/jmz/jmz_code/radiology_nlp/vilmedicbackup/ckpt/gatortron_bionlp/test_best-1_549948_refs.txt


+---------+---------+------------+-------+---------+-----------+-----------+
| Dataset | Finding | Impression | Model | ROUGE-L | F1 RadGraph | NLG Score |
+---------+---------+------------+-------+---------+-----------+-----------+
| MEDIQA  | Type1   |            | M1    |   y.yy  |    z.zz   |           |
|  2021   |         |            |-------+---------+-----------+-----------+
|         |         |            | M1    |   y.yy  |    z.zz   |           |
|         |         |            |-------+---------+-----------+-----------+
|         |         |            | M1    |   y.yy  |    z.zz   |           |
+---------+---------+------------+-------+---------+-----------+-----------+
| BIONLP  | Type2   |            | M2    |   y.yy  |    z.zz   |           |
|   2023  |         |            |-------+---------+-----------+-----------+
|         |         |            | M2    |   y.yy  |    z.zz   |           |
|         |         |            |-------+---------+-----------+-----------+
|         |         |            | M2    |   y.yy  |    z.zz   |           |
+---------+---------+------------+-------+---------+-----------+-----------+


"""