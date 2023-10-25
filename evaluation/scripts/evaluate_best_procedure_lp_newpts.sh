PREDICTIONS_DIR=/dataNAS/people/jmz/predictions/rales_predictions
python evaluate_procedure_models.py\
	--predictions_fpath $PREDICTIONS_DIR'/_bertbase_mimiciii_ct_procedure_lp/predictions.json'\
	--dataset_name mimiciii_ct_procedure \
	--data_split newpts_test 
python evaluate_procedure_models.py\
	--predictions_fpath $PREDICTIONS_DIR'/_bertlarge_mimiciii_ct_procedure_lp/predictions.json'\
	--dataset_name mimiciii_ct_procedure \
	--data_split newpts_test 
python evaluate_procedure_models.py\
	--predictions_fpath $PREDICTIONS_DIR'/_robertabase_mimiciii_ct_procedure_lp/predictions.json'\
	--dataset_name mimiciii_ct_procedure \
	--data_split newpts_test 
python evaluate_procedure_models.py\
	--predictions_fpath $PREDICTIONS_DIR'/_robertalarge_mimiciii_ct_procedure_lp/predictions.json'\
	--dataset_name mimiciii_ct_procedure \
	--data_split newpts_test 
python evaluate_procedure_models.py\
	--predictions_fpath $PREDICTIONS_DIR'/_electrasmall_mimiciii_ct_procedure_lp/predictions.json'\
	--dataset_name mimiciii_ct_procedure \
	--data_split newpts_test 
python evaluate_procedure_models.py\
	--predictions_fpath $PREDICTIONS_DIR'/_electrabase_mimiciii_ct_procedure_lp/predictions.json'\
	--dataset_name mimiciii_ct_procedure \
	--data_split newpts_test 
python evaluate_procedure_models.py\
	--predictions_fpath $PREDICTIONS_DIR'/_electralarge_mimiciii_ct_procedure_lp/predictions.json'\
	--dataset_name mimiciii_ct_procedure \
	--data_split newpts_test 
python evaluate_procedure_models.py\
	--predictions_fpath $PREDICTIONS_DIR'/_debertav3base_mimiciii_ct_procedure_lp/predictions.json'\
	--dataset_name mimiciii_ct_procedure \
	--data_split newpts_test 
python evaluate_procedure_models.py\
	--predictions_fpath $PREDICTIONS_DIR'/_debertav3large_mimiciii_ct_procedure_lp/predictions.json'\
	--dataset_name mimiciii_ct_procedure \
	--data_split newpts_test 
python evaluate_procedure_models.py\
	--predictions_fpath $PREDICTIONS_DIR'/_pubmedbert_mimiciii_ct_procedure_lp/predictions.json'\
	--dataset_name mimiciii_ct_procedure \
	--data_split newpts_test 
python evaluate_procedure_models.py\
	--predictions_fpath $PREDICTIONS_DIR'/_biolinkbertbase_mimiciii_ct_procedure_lp/predictions.json'\
	--dataset_name mimiciii_ct_procedure \
	--data_split newpts_test 
python evaluate_procedure_models.py\
	--predictions_fpath $PREDICTIONS_DIR'/_biolinkbertlarge_mimiciii_ct_procedure_lp/predictions.json'\
	--dataset_name mimiciii_ct_procedure \
	--data_split newpts_test 
python evaluate_procedure_models.py\
	--predictions_fpath $PREDICTIONS_DIR'/_bioclinicalbert_mimiciii_ct_procedure_lp/predictions.json'\
	--dataset_name mimiciii_ct_procedure \
	--data_split newpts_test 
python evaluate_procedure_models.py\
	--predictions_fpath $PREDICTIONS_DIR'/_gatortron_mimiciii_ct_procedure_lp/predictions.json'\
	--dataset_name mimiciii_ct_procedure \
	--data_split newpts_test 
python evaluate_procedure_models.py\
	--predictions_fpath $PREDICTIONS_DIR'/_radbert1_mimiciii_ct_procedure_lp/predictions.json'\
	--dataset_name mimiciii_ct_procedure \
	--data_split newpts_test 
python evaluate_procedure_models.py\
	--predictions_fpath $PREDICTIONS_DIR'/_radbert2_mimiciii_ct_procedure_lp/predictions.json'\
	--dataset_name mimiciii_ct_procedure \
	--data_split newpts_test 