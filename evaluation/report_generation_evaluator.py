from bleu import Bleu
from rouge import RougeL
from BERTscore import BertScore
from radgraph import F1RadGraph
from chexbert import CheXbert
import argparse
from datasets import load_dataset
#TODO: take care of imports

SCORER_NAME_TO_CLASS = {
    "rougel": RougeL(),
    "bleu": Bleu(),
    "bertscore": BertScore(),
    "f1radgraph": F1RadGraph(reward_level="partial"),
    "chexbert": CheXbert()
}

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--generations_filepath', type=str, required=True, help='path to file with generated texts')
    parser.add_argument('--reference_filepath', type=str, required=True, help='path to file with ground truth texts')
    parser.add_argument('--scorers', type=str, nargs='+', default=['bleu','rougel','bertscore','f1radgraph','chexbert'], help='list of scorers to use')
    args = parser.parse_args()
    return args

class ReportGenerationEvaluator:
    def __init__(self, scorers=['bleu','rougel','bertscore','f1radgraph','chexbert']):
        self.scorers = {}
        
        for scorer_name in scorers:
            if scorer_name.lower() in SCORER_NAME_TO_CLASS:
                if scorer_name in SCORER_NAME_TO_CLASS: 
                    self.scorers[scorer_name] = SCORER_NAME_TO_CLASS[scorer_name]  
                else:
                    raise NotImplementedError(f'scorer of type {scorer_name} not implemented')

    def evaluate(self, hypotheses, references):
        assert len(hypotheses) == len(references), f'Length of hypotheses (i.e. generations) {len(hypotheses)} and references (i.e. ground truths) {len(references)} must match. '
        
        scores = {k:None for k in self.scorers.keys()}
        
        for scorer_name, scorer in self.scorers.items():
            # print(scorer_name)
            scores[scorer_name] = scorer(refs=references, hyps=hypotheses)[0]

        return scores

def test_evaluator():
    generations = ["Totally unrelated.",
                    'Lungs and pleural spaces are clear. Cardiomediastinal contour is normal.',
                    'The lungs are hyperexpanded with coarse bronchovascular markings in keeping with COPD. There is increased AP diameter and increased retrosternal airspace but the diaphragms have a near normal contour']

    ground_truths = ['The lungs are hyperexpanded with coarse bronchovascular markings in keeping with COPD. There is increased AP diameter and increased retrosternal airspace but the diaphragms have a near normal contour',
                    'The lungs are hyperexpanded with coarse bronchovascular markings in keeping with COPD. There is increased AP diameter and increased retrosternal airspace but the diaphragms have a near normal contour',
                    'The lungs are hyperexpanded with coarse bronchovascular markings in keeping with COPD. There is increased AP diameter and increased retrosternal airspace but the diaphragms have a near normal contour']
    
    evaluator = ReportGenerationEvaluator()
    print(evaluator.evaluate(generations, ground_truths))
if  __name__=='__main__':
    args = parse_args()

    generations = load_dataset('json', data_files={'data': args.generations_filepath})['data']['predicted_impression']
    ground_truths = load_dataset('json', data_files={'data': args.reference_filepath})['data']['impression']

    evaluator = ReportGenerationEvaluator(scorers=args.scorers)
    print(evaluator.evaluate(generations, ground_truths))