# python inference.py \
#     --model_path ../results/classification/_bertbase_procedure_mimiciii_ct_procedure/run-3/checkpoint-7264\
#     --dataset_name mimiciii_ct_procedure \
#     --data_split test \
#     --output_dir ./predictions/bertbase_procedure_test/ 

python inference.py \
    --model_path ../results/classification/_bertlarge_procedure_mimiciii_ct_procedure/run-5/checkpoint-5448\
    --dataset_name mimiciii_ct_procedure \
    --data_split test \
    --output_dir ./predictions/bertlarge_procedure_test/ 

# python inference.py \
#     --model_path ../results/classification/_roberta_base_mimiciii_ct_procedure/run-0/checkpoint-5448\
#     --dataset_name mimiciii_ct_procedure \
#     --data_split test \
#     --output_dir ./predictions/robertabase_procedure_test/

# python inference.py \
#     --model_path ../results/classification/_roberta_large_mimiciii_ct_procedure/run-8/checkpoint-3632\
#     --dataset_name mimiciii_ct_procedure \
#     --data_split test \
#     --output_dir ./predictions/robertalarge_procedure_test/

# python inference.py \
#     --model_path ../results/classification/_electrasmall_procedure_mimiciii_ct_procedure/run-4/checkpoint-9080\
#     --dataset_name mimiciii_ct_procedure \
#     --data_split test \
#     --output_dir ./predictions/electrasmall_procedure_test/

# python inference.py \
#     --model_path ../results/classification/_electrabase_procedure_mimiciii_ct_procedure/run-1/checkpoint-5448\
#     --dataset_name mimiciii_ct_procedure \
#     --data_split test \
#     --output_dir ./predictions/electrabase_procedure_test/

python inference.py \
    --model_path ../results/classification/_electralarge_procedure_mimiciii_ct_procedure/run-7/checkpoint-9080\
    --dataset_name mimiciii_ct_procedure \
    --data_split test \
    --output_dir ./predictions/electralarge_procedure_test/

# python inference.py \
#     --model_path ../results/classification/_biolinkbertbase_procedure_mimiciii_ct_procedure/run-0/checkpoint-7264\
#     --dataset_name mimiciii_ct_procedure \
#     --data_split test \
#     --output_dir ./predictions/debertav3base_procedure_test/

# python inference.py \
#     --model_path ../results/classification/_deberta-v3-large_mimiciii_ct_procedure/run-3/checkpoint-7264\
#     --dataset_name mimiciii_ct_procedure \
#     --data_split test \
#     --output_dir ./predictions/debertav3large_procedure_test/

# python inference.py \
#     --model_path ../results/classification/_pubmedbert_base_mimiciii_ct_procedure/run-8/checkpoint-7264\
#     --dataset_name mimiciii_ct_procedure \
#     --data_split test \
#     --output_dir ./predictions/pubmedbert_procedure_test/

python inference.py \
    --model_path ../results/classification/_biolinkbertbase_procedure_mimiciii_ct_procedure/run-0/checkpoint-7264\
    --dataset_name mimiciii_ct_procedure \
    --data_split test \
    --output_dir ./predictions/biolinkbertbase_procedure_test/

# python inference.py \
#     --model_path ../results/classification/_biolinkbert-large_mimiciii_ct_procedure/run-9/checkpoint-1362\
#     --dataset_name mimiciii_ct_procedure \
#     --data_split test \
#     --output_dir ./predictions/biolinkbertlarge_procedure_test/

# python inference.py \
#     --model_path ../results/classification/_bioclinicalbert_mimiciii_ct_procedure/run-3/checkpoint-3632\
#     --dataset_name mimiciii_ct_procedure \
#     --data_split test \
#     --output_dir ./predictions/bioclinicalbert_procedure_test/

# python inference.py \
#     --model_path ../results/classification/_gatortron_mimiciii_ct_procedure/run-4/checkpoint-2270\
#     --dataset_name mimiciii_ct_procedure \
#     --data_split test \
#     --output_dir ./predictions/gatortron_procedure_test/

# python inference.py \
#     --model_path ../results/classification/_radbert_stanford_mimiciii_ct_procedure/run-0/checkpoint-10896\
#     --dataset_name mimiciii_ct_procedure \
#     --data_split test \
#     --output_dir ./predictions/radbert1_procedure_test/

# python inference.py \
#     --model_path ../results/classification/_radbert_ucsd_mimiciii_ct_procedure/run-9/checkpoint-1362\
#     --dataset_name mimiciii_ct_procedure \
#     --data_split test \
#     --output_dir ./predictions/radbert2_procedure_test/