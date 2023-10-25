PREDICTIONS_DIR=/dataNAS/people/jmz/predictions/rales_predictions


python evaluate_procedure_models.py\
	--predictions_fpath $PREDICTIONS_DIR'/_bertbase_procedure_mimiciii_ct_procedure_10pct/predictions.json'\
	--dataset_name mimiciii_ct_procedure \
	--data_split newpts_test 

python evaluate_procedure_models.py\
	--predictions_fpath $PREDICTIONS_DIR'/_bertlarge_procedure_mimiciii_ct_procedure_10pct/predictions.json'\
	--dataset_name mimiciii_ct_procedure \
	--data_split newpts_test 

python evaluate_procedure_models.py\
	--predictions_fpath $PREDICTIONS_DIR'/_robertabase_procedure_mimiciii_ct_procedure_10pct/predictions.json'\
	--dataset_name mimiciii_ct_procedure \
	--data_split newpts_test 

python evaluate_procedure_models.py\
	--predictions_fpath $PREDICTIONS_DIR'/_robertalarge_procedure_mimiciii_ct_procedure_10pct/predictions.json'\
	--dataset_name mimiciii_ct_procedure \
	--data_split newpts_test 

python evaluate_procedure_models.py\
	--predictions_fpath $PREDICTIONS_DIR'/_electrasmall_procedure_mimiciii_ct_procedure_10pct/predictions.json'\
	--dataset_name mimiciii_ct_procedure \
	--data_split newpts_test 

python evaluate_procedure_models.py\
	--predictions_fpath $PREDICTIONS_DIR'/_electrabase_procedure_mimiciii_ct_procedure_10pct/predictions.json'\
	--dataset_name mimiciii_ct_procedure \
	--data_split newpts_test 

python evaluate_procedure_models.py\
	--predictions_fpath $PREDICTIONS_DIR'/_electralarge_procedure_mimiciii_ct_procedure_10pct/predictions.json'\
	--dataset_name mimiciii_ct_procedure \
	--data_split newpts_test 

python evaluate_procedure_models.py\
	--predictions_fpath $PREDICTIONS_DIR'/_debertav3base_procedure_mimiciii_ct_procedure_10pct/predictions.json'\
	--dataset_name mimiciii_ct_procedure \
	--data_split newpts_test 

python evaluate_procedure_models.py\
	--predictions_fpath $PREDICTIONS_DIR'/_deberta-v3-large_mimiciii_ct_procedure_10pct/predictions.json'\
	--dataset_name mimiciii_ct_procedure \
	--data_split newpts_test 

python evaluate_procedure_models.py\
	--predictions_fpath $PREDICTIONS_DIR'/_pubmedbert_base_mimiciii_ct_procedure_10pct/predictions.json'\
	--dataset_name mimiciii_ct_procedure \
	--data_split newpts_test 

python evaluate_procedure_models.py\
	--predictions_fpath $PREDICTIONS_DIR'/_biolinkbertbase_procedureeff_mimiciii_ct_procedure_10pct/predictions.json'\
	--dataset_name mimiciii_ct_procedure \
	--data_split newpts_test 

python evaluate_procedure_models.py\
	--predictions_fpath $PREDICTIONS_DIR'/_biolinkbertlarge_stanza_mimiciii_ct_procedure_10pct/predictions.json'\
	--dataset_name mimiciii_ct_procedure \
	--data_split newpts_test 

python evaluate_procedure_models.py\
	--predictions_fpath $PREDICTIONS_DIR'/_bioclinicalbert_mimiciii_ct_procedure_10pct/predictions.json'\
	--dataset_name mimiciii_ct_procedure \
	--data_split newpts_test 

python evaluate_procedure_models.py\
	--predictions_fpath $PREDICTIONS_DIR'/_gatortron_mimiciii_ct_procedure_10pct/predictions.json'\
	--dataset_name mimiciii_ct_procedure \
	--data_split newpts_test 

python evaluate_procedure_models.py\
	--predictions_fpath $PREDICTIONS_DIR'/_radbert1_mimiciii_ct_procedure_10pct/predictions.json'\
	--dataset_name mimiciii_ct_procedure \
	--data_split newpts_test 

python evaluate_procedure_models.py\
	--predictions_fpath $PREDICTIONS_DIR'/_radbert2_mimiciii_ct_procedure_10pct/predictions.json'\
	--dataset_name mimiciii_ct_procedure \
	--data_split newpts_test 

