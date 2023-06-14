"""
Creates an sh file with python commands to run the inference using the best model for a task of interest
"""

import os
import argparse
import pandas as pd

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--best_model_file', type=str, default='../results/best_results_radgraph_lp.csv')
    return parser.parse_args()

def main():
    best_model_file = parse_args().best_model_file
    best_model_df = pd.read_csv(best_model_file)
    
    # Stanza

    # with open('./predict_best_stanza_10pct.sh','w') as fout:
    # with open('./predict_best_stanza_1pct.sh','w') as fout:
    # with open('./predict_best_stanza_lp.sh','w') as fout:
        # for _,row in best_model_df.iterrows():
            # python inference.py \
            #     --model_path ../results/ner/bertbase_stanza_stanza_ner/run-0/checkpoint-770 \
            #     --dataset_name stanza \
            #     --data_split test\
            #     --output_dir ./predictions/bertbase_stanza_stanza_ner_val/ 
            
            # fout.write(f"python inference.py \\\n")
            # fout.write(f"\t--model_path {row['best_subdir']} \\\n")
            # fout.write(f"\t--dataset_name stanza \\\n")
            # fout.write(f"\t--data_split test \\\n")
            # fout.write(f"\t--output_dir ./predictions/{row['Unnamed: 0']}/ \n\n")

    # MIMIC Procedure
    # with open('./predict_best_procedure_lp.sh','w') as fout:
    # with open('./predict_best_procedure_10pct.sh','w') as fout:
    # with open('./predict_best_procedure_1pct.sh','w') as fout:
        # for _,row in best_model_df.iterrows():
            # python inference.py \
            #     --model_path ../results/classification/_bertlarge_procedure_mimiciii_ct_procedure/run-5/checkpoint-5448\
            #     --dataset_name mimiciii_ct_procedure \
            #     --data_split test \
            #     --output_dir ./predictions/bertlarge_procedure_test/ 
            
            # fout.write(f"python inference_procedure.py \\\n")
            # fout.write(f"\t--model_path {row['best_subdir']} \\\n")
            # fout.write(f"\t--dataset_name mimiciii_ct_procedure \\\n")
            # fout.write(f"\t--data_split test \\\n")
            # fout.write(f"\t--output_dir ./predictions/{row['Unnamed: 0']}{'_lp' if '_lp' in best_model_file else ''}/ \n\n")

    # RadGraph
    with open('./predict_best_radgraph_lp.sh','w') as fout:
    # with open('./predict_best_radgraph_10pct.sh','w') as fout:
    # with open('./predict_best_radgraph_1pct.sh','w') as fout:
        fout.write("cd ../fine_tuning/utils/dygiepp\n\n")
        for _,row in best_model_df.iterrows():
            # allennlp evaluate \
            #     /DEIDPATH/radiology_nlp/rales/fine_tuning/utils/dygiepp/models/radgraph_bertlarge_0/model.tar.gz\
            #     /DEIDPATH/data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
            #     --cuda-device 0 \
            #     --include-package dygie \
            #     --output-file /DEIDPATH/radiology_nlp/rales/results/re/radgraph_mimiccxr_test_bertlarge.json

            fout.write(f"mkdir {os.path.join(row['best_subdir'], 'model')}\n")
            fout.write(f"tar -xf {os.path.join(row['best_subdir'], 'model.tar.gz')} -C {os.path.join(row['best_subdir'], 'model')}\n")
            fout.write(f"cp -r {os.path.join(row['best_subdir'], 'vocabulary')} {os.path.join(row['best_subdir'], 'model')}\n")
            fout.write(f"tar -czvf {os.path.join(row['best_subdir'], 'model.tar.gz')} -C {os.path.join(row['best_subdir'], 'model')} . \n")
            fout.write(f"rm -r {os.path.join(row['best_subdir'], 'model')}\n\n")

            fout.write(f"allennlp evaluate \\\n")
            fout.write(f"\t{os.path.join(row['best_subdir'],'model.tar.gz')} \\\n")
            fout.write(f"\t/dataNAS/people/jmz/data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \\\n")
            fout.write(f"\t--cuda-device 0 \\\n")
            fout.write(f"\t--include-package dygie \\\n")
            fout.write(f"\t--output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/results/re/radgraph_lp_mimiccxr_test_{row['Unnamed: 0']}.json \n\n")

            fout.write(f"allennlp evaluate \\\n")
            fout.write(f"\t{os.path.join(row['best_subdir'],'model.tar.gz')} \\\n")
            fout.write(f"\t/dataNAS/people/jmz/data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \\\n")
            fout.write(f"\t--cuda-device 0 \\\n")
            fout.write(f"\t--include-package dygie \\\n")
            fout.write(f"\t--output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/results/re/radgraph_lp_chexpert_test_{row['Unnamed: 0']}.json \n\n")


    # RadSpRL
    # with open('./predict_best_radsprl_lp.sh','w') as fout:
    # with open('./predict_best_radsprl_10pct.sh','w') as fout:
    # with open('./predict_best_radsprl_1pct.sh','w') as fout:
        # fout.write("cd ../fine_tuning/utils/dygiepp\n\n")
        # for _,row in best_model_df.iterrows():
    #         # allennlp evaluate \
    #         #     /DEIDPATH/radiology_nlp/rales/fine_tuning/utils/dygiepp/models/radgraph_bertlarge_0/model.tar.gz\
    #         #     /DEIDPATH/data/RadSpRL/radsprl_dygiepp_test.jsonl \
    #         #     --cuda-device 0 \
    #         #     --include-package dygie \
    #         #     --output-file /DEIDPATH/radiology_nlp/rales/results/re/radgraph_mimiccxr_test_bertlarge.json

            # fout.write(f"mkdir {os.path.join(row['best_subdir'], 'model')}\n")
            # fout.write(f"tar -xf {os.path.join(row['best_subdir'], 'model.tar.gz')} -C {os.path.join(row['best_subdir'], 'model')}\n")
            # fout.write(f"cp -r {os.path.join(row['best_subdir'], 'vocabulary')} {os.path.join(row['best_subdir'], 'model')}\n")
            # fout.write(f"tar -czvf {os.path.join(row['best_subdir'], 'model.tar.gz')} -C {os.path.join(row['best_subdir'], 'model')} . \n")
            # fout.write(f"rm -r {os.path.join(row['best_subdir'], 'model')}\n\n")

            # fout.write(f"allennlp evaluate \\\n")
            # fout.write(f"\t{os.path.join(row['best_subdir'],'model.tar.gz')} \\\n")
            # fout.write(f"\t/dataNAS/people/jmz/data/RadSpRL/radsprl_dygiepp_test.jsonl \\\n")
            # fout.write(f"\t--cuda-device 0 \\\n")
            # fout.write(f"\t--include-package dygie \\\n")
            # fout.write(f"\t--output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/results/re/radsprl_lp_test_{row['Unnamed: 0']}.json \n\n")

            # fout.write(f"allennlp evaluate \\\n")
            # fout.write(f"\t{os.path.join(row['best_subdir'],'model.tar.gz')} \\\n")
            # fout.write(f"\t/dataNAS/people/jmz/data/RadSpRL/radsprl_dygiepp_test.jsonl \\\n")
            # fout.write(f"\t--cuda-device 0 \\\n")
            # fout.write(f"\t--include-package dygie \\\n")
            # fout.write(f"\t--output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/results/re/radsprl_lp_test_{row['Unnamed: 0']}.json \n\n")
            



if __name__=='__main__':
    main()


