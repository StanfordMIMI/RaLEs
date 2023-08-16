python inference.py \
    --model_path ../results/ner/bertbase_stanza_stanza_ner/run-0/checkpoint-770 \
    --dataset_name stanza \
    --data_split test\
    --output_dir ./predictions/stanza/bertbase_stanza_stanza_ner_test/
    
python inference.py \
    --model_path ../results/ner/bertlarge_stanza_stanza_ner/run-0/checkpoint-308\
    --dataset_name stanza \
    --data_split test\
    --output_dir ./predictions/stanza/bertlarge_stanza_stanza_ner_test/ 

python inference.py \
    --model_path ../results/ner/robertabase_stanza_stanza_ner/run-7/checkpoint-616\
    --dataset_name stanza \
    --data_split test\
    --output_dir ./predictions/stanza/robertabase_stanza_stanza_ner_test/

python inference.py \
    --model_path ../results/ner/robertalarge_stanza_stanza_ner/run-3/checkpoint-308\
    --dataset_name stanza \
    --data_split test\
    --output_dir ./predictions/stanza/robertalarge_stanza_stanza_ner_test/

python inference.py \
    --model_path ../results/ner/electrasmall_stanza_stanza_ner/run-1/checkpoint-770\
    --dataset_name stanza \
    --data_split test\
    --output_dir ./predictions/stanza/electrasmall_stanza_stanza_ner_test/

python inference.py \
    --model_path ../results/ner/electrabase_stanza_stanza_ner/run-6/checkpoint-770\
    --dataset_name stanza \
    --data_split test\
    --output_dir ./predictions/stanza/electrabase_stanza_stanza_ner_test/

python inference.py \
    --model_path ../results/ner/electralarge_stanza_stanza_ner/run-5/checkpoint-308\
    --dataset_name stanza \
    --data_split test\
    --output_dir ./predictions/stanza/electralarge_stanza_stanza_ner_test/

python inference.py \
    --model_path ../results/ner/debertav3base_stanza_stanza_ner/run-8/checkpoint-616\
    --dataset_name stanza \
    --data_split test\
    --output_dir ./predictions/stanza/debertav3base_stanza_stanza_ner_test/

python inference.py \
    --model_path ../results/ner/debertav3large_stanza_stanza_ner/run-6/checkpoint-385\
    --dataset_name stanza \
    --data_split test\
    --output_dir ./predictions/stanza/debertav3large_stanza_stanza_ner_test/

python inference.py \
    --model_path ../results/ner/pubmedbert_stanza_stanza_ner/run-9/checkpoint-616\
    --dataset_name stanza \
    --data_split test\
    --output_dir ./predictions/stanza/pubmedbert_stanza_stanza_ner_test/

python inference.py \
    --model_path ../results/ner/biolinkbertbase_stanza_stanza_ner/run-4/checkpoint-616\
    --dataset_name stanza \
    --data_split test\
    --output_dir ./predictions/stanza/debertav3base_stanza_stanza_ner_test/

python inference.py \
    --model_path ../results/ner/biolinkbertlarge_stanza_stanza_ner/run-3/checkpoint-462\
    --dataset_name stanza \
    --data_split test\
    --output_dir ./predictions/stanza/debertav3large_stanza_stanza_ner_test/

python inference.py \
    --model_path ../results/ner/bioclinicalbert_stanza_stanza_ner/run-1/checkpoint-616\
    --dataset_name stanza \
    --data_split test\
    --output_dir ./predictions/stanza/bioclinicalbert_stanza_stanza_ner_test/

python inference.py \
    --model_path ../results/ner/gatortron_stanza_stanza_ner/run-7/checkpoint-385\
    --dataset_name stanza \
    --data_split test\
    --output_dir ./predictions/stanza/gatortron_stanza_stanza_ner_test/

python inference.py \
    --model_path ../results/ner/radbert1_stanza_stanza_ner/run-6/checkpoint-770\
    --dataset_name stanza \
    --data_split test\
    --output_dir ./predictions/stanza/radbert1_stanza_stanza_ner_test/

python inference.py \
    --model_path ../results/ner/radbert2_stanza_stanza_ner/run-9/checkpoint-770\
    --dataset_name stanza \
    --data_split test\
    --output_dir ./predictions/stanza/radbert2_stanza_stanza_ner_test/