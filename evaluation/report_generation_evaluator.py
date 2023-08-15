from bleu import Bleu
from rouge import RougeL
from BERTscore import BertScore
from radgraph import F1RadGraph
#TODO: take care of imports

SCORER_NAME_TO_CLASS = {
    "rougel": RougeL(),
    "bleu": Bleu(),
    "bertscore": BertScore(),
    "f1radgraph": F1RadGraph(reward_level="partial")
}
class ReportEvaluator:
    def __init__(self, scorers=['bleu','rougel','bertscore','f1radgraph']):
        self.scorers = {}
        
        for scorer_name in scorers:
            if scorer_name.lower() in SCORER_NAME_TO_CLASS:
                if scorer_name in SCORER_NAME_TO_CLASS: 
                    self.scorers[scorer_name] = SCORER_NAME_TO_CLASS[scorer_name]  
                else:
                    raise NotImplementedError(f'scorer of type {scorer_name} not implemented')

    def evaluate(self, hypotheses, references):
        assert len(hypotheses) == len(references), f'Length of hypotheses {len(hypotheses)} and references {len(references)} must match. '
        
        scores = {k:None for k in self.scorers.keys()}
        
        for scorer_name, scorer in self.scorers.items():
            print(scorer_name)
            scores[scorer_name] = scorer(refs=references, hyps=hypotheses)[0]

        return scores


if  __name__=='__main__':
    generations = ["Totally unrelated.",
                    'Lungs and pleural spaces are clear. Cardiomediastinal contour is normal.',
                    'The lungs are hyperexpanded with coarse bronchovascular markings in keeping with COPD. There is increased AP diameter and increased retrosternal airspace but the diaphragms have a near normal contour']

    ground_truths = ['The lungs are hyperexpanded with coarse bronchovascular markings in keeping with COPD. There is increased AP diameter and increased retrosternal airspace but the diaphragms have a near normal contour',
                    'The lungs are hyperexpanded with coarse bronchovascular markings in keeping with COPD. There is increased AP diameter and increased retrosternal airspace but the diaphragms have a near normal contour',
                    'The lungs are hyperexpanded with coarse bronchovascular markings in keeping with COPD. There is increased AP diameter and increased retrosternal airspace but the diaphragms have a near normal contour']
    print(len(generations))
    print(len(ground_truths))

    evaluator = ReportEvaluator()
    print(evaluator.evaluate(generations, ground_truths))