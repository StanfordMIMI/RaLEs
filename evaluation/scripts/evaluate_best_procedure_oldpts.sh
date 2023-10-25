PREDICTIONS_DIR=/dataNAS/people/jmz/predictions/rales_predictions
python evaluate_procedure_models.py\
    --predictions_fpath $PREDICTIONS_DIR'/bertbase_procedure_test/predictions.json'\
    --dataset_name mimiciii_ct_procedure \
    --data_split repeatpts_test

python evaluate_procedure_models.py\
    --predictions_fpath $PREDICTIONS_DIR'/bertlarge_procedure_test/predictions.json'\
    --dataset_name mimiciii_ct_procedure \
    --data_split newpts_test

python evaluate_procedure_models.py\
    --predictions_fpath $PREDICTIONS_DIR'/robertabase_procedure_test/predictions.json'\
    --dataset_name mimiciii_ct_procedure \
    --data_split newpts_test

python evaluate_procedure_models.py\
    --predictions_fpath $PREDICTIONS_DIR'/robertalarge_procedure_test/predictions.json'\
    --dataset_name mimiciii_ct_procedure \
    --data_split newpts_test

python evaluate_procedure_models.py\
    --predictions_fpath $PREDICTIONS_DIR'/electrasmall_procedure_test/predictions.json'\
    --dataset_name mimiciii_ct_procedure \
    --data_split newpts_test

python evaluate_procedure_models.py\
    --predictions_fpath $PREDICTIONS_DIR'/electrabase_procedure_test/predictions.json'\
    --dataset_name mimiciii_ct_procedure \
    --data_split newpts_test

python evaluate_procedure_models.py\
    --predictions_fpath $PREDICTIONS_DIR'/electralarge_procedure_test/predictions.json'\
    --dataset_name mimiciii_ct_procedure \
    --data_split newpts_test

python evaluate_procedure_models.py\
    --predictions_fpath $PREDICTIONS_DIR'/debertav3base_procedure_test/predictions.json'\
    --dataset_name mimiciii_ct_procedure \
    --data_split newpts_test

python evaluate_procedure_models.py\
    --predictions_fpath $PREDICTIONS_DIR'/debertav3large_procedure_test/predictions.json'\
    --dataset_name mimiciii_ct_procedure \
    --data_split newpts_test

python evaluate_procedure_models.py\
    --predictions_fpath $PREDICTIONS_DIR'/pubmedbert_procedure_test/predictions.json'\
    --dataset_name mimiciii_ct_procedure \
    --data_split newpts_test

python evaluate_procedure_models.py\
    --predictions_fpath $PREDICTIONS_DIR'/biolinkbertbase_procedure_test/predictions.json'\
    --dataset_name mimiciii_ct_procedure \
    --data_split newpts_test

python evaluate_procedure_models.py\
    --predictions_fpath $PREDICTIONS_DIR'/biolinkbertlarge_procedure_test/predictions.json'\
    --dataset_name mimiciii_ct_procedure \
    --data_split newpts_test

python evaluate_procedure_models.py\
    --predictions_fpath $PREDICTIONS_DIR'/bioclinicalbert_procedure_test/predictions.json'\
    --dataset_name mimiciii_ct_procedure \
    --data_split newpts_test

python evaluate_procedure_models.py\
    --predictions_fpath $PREDICTIONS_DIR'/gatortron_procedure_test/predictions.json'\
    --dataset_name mimiciii_ct_procedure \
    --data_split newpts_test

python evaluate_procedure_models.py\
    --predictions_fpath $PREDICTIONS_DIR'/radbert1_procedure_test/predictions.json'\
    --dataset_name mimiciii_ct_procedure \
    --data_split newpts_test

python evaluate_procedure_models.py\
    --predictions_fpath $PREDICTIONS_DIR'/radbert2_procedure_test/predictions.json'\
    --dataset_name mimiciii_ct_procedure \
    --data_split newpts_test
