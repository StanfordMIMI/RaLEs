"""
Creates an sh file with python commands to evaluate the predictions from the best model for a task of interest
"""

import os
import argparse
import pandas as pd


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--experiment', type=str, default='procedure_1pct')
    return parser.parse_args()

def main():
    experiment_name = parse_args().experiment
    predictions_main_dir = '../inference/predictions/'
    predictions_dirs = [os.path.abspath(os.path.join(predictions_main_dir, x)) for x in os.listdir(predictions_main_dir) if x.endswith(experiment_name)]
    
    # with open('./evaluate_best_stanza_lp.sh','w') as fout:
    #     for d in predictions_dirs:
    #         # python evaluate_stanza_models.py\
    #         #     --predictions_fpath '../inference/predictions/stanza/bertlarge_stanza_stanza_ner_test/predictions.json'\
    #         #     --dataset_name stanza \
    #         #     --bootstrap\
    #         #     --data_split test
            
    #         fout.write(f"python evaluate_stanza_models.py\\\n")
    #         fout.write(f"\t--predictions_fpath '{d}/predictions.json'\\\n")
    #         fout.write(f"\t--dataset_name stanza \\\n")
    #         fout.write(f"\t--data_split test \\\n")
    #         fout.write(f"\t--bootstrap \n")

    with open('./evaluate_best_procedure_1pct.sh','w') as fout:
        for d in predictions_dirs:
            # python evaluate_models.py\
            #     --predictions_fpath '../inference/predictions/bertlarge_procedure_test/predictions.json'\
            #     --dataset_name mimiciii_ct_procedure \
            #     --data_split test
            
            fout.write(f"python evaluate_procedure_models.py\\\n")
            fout.write(f"\t--predictions_fpath '{d}/predictions.json'\\\n")
            fout.write(f"\t--dataset_name mimiciii_ct_procedure \\\n")
            fout.write(f"\t--data_split test \\\n")
            fout.write(f"\t--bootstrap \n")






if __name__=='__main__':
    main()
