#RadGraph - RE inference
##########################################################################################
##########################################################################################
#MIMIC-CXR
##########################################################################################
##########################################################################################
allennlp predict \
    /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/fine_tuning/utils/dygiepp/models/radgraph_bertbase_0/model.tar.gz\
    /dataNAS/people/jmz/data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
    --cuda-device 0 \
    --predictor dygie \
    --include-package dygie \
    --use-dataset-reader\
    --silent\
    --output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/inference/predictions/radgraph/radgraph_mimiccxr_test_bertbase.json

allennlp predict \
    /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/fine_tuning/utils/dygiepp/models/radgraph_bertlarge_0/model.tar.gz\
    /dataNAS/people/jmz/data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
    --cuda-device 0 \
    --predictor dygie \
    --include-package dygie \
    --use-dataset-reader\
    --silent\
    --output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/inference/predictions/radgraph/radgraph_mimiccxr_test_bertlarge.json

allennlp predict \
    /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/fine_tuning/utils/dygiepp/models/radgraph_robertabase_2/model.tar.gz\
    /dataNAS/people/jmz/data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
    --cuda-device 0 \
    --predictor dygie \
    --include-package dygie \
    --use-dataset-reader\
    --silent\
    --output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/inference/predictions/radgraph/radgraph_mimiccxr_test_robertabase.json

allennlp predict \
    /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/fine_tuning/utils/dygiepp/models/radgraph_robertalarge_0/model.tar.gz\
    /dataNAS/people/jmz/data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
    --cuda-device 0 \
    --predictor dygie \
    --include-package dygie \
    --use-dataset-reader\
    --silent\
    --output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/inference/predictions/radgraph/radgraph_mimiccxr_test_robertalarge.json

allennlp predict \
    /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/fine_tuning/utils/dygiepp/models/radgraph_electrasmall_0/model.tar.gz\
    /dataNAS/people/jmz/data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
    --cuda-device 0 \
    --predictor dygie \
    --include-package dygie \
    --use-dataset-reader\
    --silent\
    --output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/inference/predictions/radgraph/radgraph_mimiccxr_test_electrasmall.json

allennlp predict \
    /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/fine_tuning/utils/dygiepp/models/radgraph_electra_base/model.tar.gz\
    /dataNAS/people/jmz/data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
    --cuda-device 0 \
    --predictor dygie \
    --include-package dygie \
    --use-dataset-reader\
    --silent\
    --output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/inference/predictions/radgraph/radgraph_mimiccxr_test_electrabase.json

allennlp predict \
    /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/fine_tuning/utils/dygiepp/models/radgraph_electralarge_0/model.tar.gz\
    /dataNAS/people/jmz/data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
    --cuda-device 0 \
    --predictor dygie \
    --include-package dygie \
    --use-dataset-reader\
    --silent\
    --output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/inference/predictions/radgraph/radgraph_mimiccxr_test_electralarge.json

allennlp predict \
    /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/fine_tuning/utils/dygiepp/models/radgraph_debertav3base_0/model.tar.gz\
    /dataNAS/people/jmz/data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
    --cuda-device 0 \
    --predictor dygie \
    --include-package dygie \
    --use-dataset-reader\
    --silent\
    --output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/inference/predictions/radgraph/radgraph_mimiccxr_test_debertav3base.json

allennlp predict \
    /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/fine_tuning/utils/dygiepp/models/radgraph_debertav3large_0/model.tar.gz\
    /dataNAS/people/jmz/data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
    --cuda-device 0 \
    --predictor dygie \
    --include-package dygie \
    --use-dataset-reader\
    --silent\
    --output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/inference/predictions/radgraph/radgraph_mimiccxr_test_debertav3large.json

allennlp predict \
    /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/fine_tuning/utils/dygiepp/models/radgraph_pubmedbert_2/model.tar.gz\
    /dataNAS/people/jmz/data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
    --cuda-device 0 \
    --predictor dygie \
    --include-package dygie \
    --use-dataset-reader\
    --silent\
    --output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/inference/predictions/radgraph/radgraph_mimiccxr_test_pubmedbert.json

allennlp predict \
    /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/fine_tuning/utils/dygiepp/models/radgraph_biolinkbertbase_0/model.tar.gz\
    /dataNAS/people/jmz/data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
    --cuda-device 0 \
    --predictor dygie \
    --include-package dygie \
    --use-dataset-reader\
    --silent\
    --output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/inference/predictions/radgraph/radgraph_mimiccxr_test_biolinkbertbase.json


allennlp predict \
    /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/fine_tuning/utils/dygiepp/models/radgraph_biolinkbertlarge_0/model.tar.gz\
    /dataNAS/people/jmz/data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
    --cuda-device 0 \
    --predictor dygie \
    --include-package dygie \
    --use-dataset-reader\
    --silent\
    --output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/inference/predictions/radgraph/radgraph_mimiccxr_test_biolinkbertlarge.json

allennlp predict \
    /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/fine_tuning/utils/dygiepp/models/radgraph_bioclinicalbert_0/model.tar.gz\
    /dataNAS/people/jmz/data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
    --cuda-device 0 \
    --predictor dygie \
    --include-package dygie \
    --use-dataset-reader\
    --silent\
    --output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/inference/predictions/radgraph/radgraph_mimiccxr_test_bioclinicalbert.json

allennlp predict \
    /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/fine_tuning/utils/dygiepp/models/radgraph_gatortron_0/model.tar.gz\
    /dataNAS/people/jmz/data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
    --cuda-device 0 \
    --predictor dygie \
    --include-package dygie \
    --use-dataset-reader\
    --silent\
    --output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/inference/predictions/radgraph/radgraph_mimiccxr_test_gatortron.json

allennlp predict \
    /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/fine_tuning/utils/dygiepp/models/radgraph_radbert1_2/model.tar.gz\
    /dataNAS/people/jmz/data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
    --cuda-device 0 \
    --predictor dygie \
    --include-package dygie \
    --use-dataset-reader\
    --silent\
    --output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/inference/predictions/radgraph/radgraph_mimiccxr_test_radbert1.json

allennlp predict \
    /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/fine_tuning/utils/dygiepp/models/radgraph_radbert2_2/model.tar.gz\
    /dataNAS/people/jmz/data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
    --cuda-device 0 \
    --predictor dygie \
    --include-package dygie \
    --use-dataset-reader\
    --silent\
    --output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/inference/predictions/radgraph/radgraph_mimiccxr_test_radbert2.json
##########################################################################################
##########################################################################################
#CheXpert
##########################################################################################
##########################################################################################
allennlp predict \
    /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/fine_tuning/utils/dygiepp/models/radgraph_bertbase_0/model.tar.gz\
    /dataNAS/people/jmz/data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
    --cuda-device 0 \
    --predictor dygie \
    --include-package dygie \
    --use-dataset-reader\
    --silent\
    --output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/inference/predictions/radgraph/radgraph_chexpert_test_bertbase.json

allennlp predict \
    /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/fine_tuning/utils/dygiepp/models/radgraph_bertlarge_0/model.tar.gz\
    /dataNAS/people/jmz/data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
    --cuda-device 0 \
    --predictor dygie \
    --include-package dygie \
    --use-dataset-reader\
    --silent\
    --output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/inference/predictions/radgraph/radgraph_chexpert_test_bertlarge.json

allennlp predict \
    /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/fine_tuning/utils/dygiepp/models/radgraph_robertabase_2/model.tar.gz\
    /dataNAS/people/jmz/data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
    --cuda-device 0 \
    --predictor dygie \
    --include-package dygie \
    --use-dataset-reader\
    --silent\
    --output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/inference/predictions/radgraph/radgraph_chexpert_test_robertabase.json

allennlp predict \
    /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/fine_tuning/utils/dygiepp/models/radgraph_robertalarge_0/model.tar.gz\
    /dataNAS/people/jmz/data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
    --cuda-device 0 \
    --predictor dygie \
    --include-package dygie \
    --use-dataset-reader\
    --silent\
    --output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/inference/predictions/radgraph/radgraph_chexpert_test_robertalarge.json

allennlp predict \
    /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/fine_tuning/utils/dygiepp/models/radgraph_electrasmall_0/model.tar.gz\
    /dataNAS/people/jmz/data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
    --cuda-device 0 \
    --predictor dygie \
    --include-package dygie \
    --use-dataset-reader\
    --silent\
    --output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/inference/predictions/radgraph/radgraph_chexpert_test_electrasmall.json

allennlp predict \
    /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/fine_tuning/utils/dygiepp/models/radgraph_electra_base/model.tar.gz\
    /dataNAS/people/jmz/data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
    --cuda-device 0 \
    --predictor dygie \
    --include-package dygie \
    --use-dataset-reader\
    --silent\
    --output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/inference/predictions/radgraph/radgraph_chexpert_test_electrabase.json

allennlp predict \
    /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/fine_tuning/utils/dygiepp/models/radgraph_electralarge_0/model.tar.gz\
    /dataNAS/people/jmz/data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
    --cuda-device 0 \
    --predictor dygie \
    --include-package dygie \
    --use-dataset-reader\
    --silent\
    --output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/inference/predictions/radgraph/radgraph_chexpert_test_electralarge.json

allennlp predict \
    /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/fine_tuning/utils/dygiepp/models/radgraph_debertav3base_0/model.tar.gz\
    /dataNAS/people/jmz/data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
    --cuda-device 0 \
    --predictor dygie \
    --include-package dygie \
    --use-dataset-reader\
    --silent\
    --output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/inference/predictions/radgraph/radgraph_chexpert_test_debertav3base.json

allennlp predict \
    /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/fine_tuning/utils/dygiepp/models/radgraph_debertav3large_0/model.tar.gz\
    /dataNAS/people/jmz/data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
    --cuda-device 0 \
    --predictor dygie \
    --include-package dygie \
    --use-dataset-reader\
    --silent\
    --output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/inference/predictions/radgraph/radgraph_chexpert_test_debertav3large.json

allennlp predict \
    /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/fine_tuning/utils/dygiepp/models/radgraph_pubmedbert_2/model.tar.gz\
    /dataNAS/people/jmz/data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
    --cuda-device 0 \
    --predictor dygie \
    --include-package dygie \
    --use-dataset-reader\
    --silent\
    --output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/inference/predictions/radgraph/radgraph_chexpert_test_pubmedbert.json

allennlp predict \
    /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/fine_tuning/utils/dygiepp/models/radgraph_biolinkbertbase_0/model.tar.gz\
    /dataNAS/people/jmz/data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
    --cuda-device 0 \
    --predictor dygie \
    --include-package dygie \
    --use-dataset-reader\
    --silent\
    --output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/inference/predictions/radgraph/radgraph_chexpert_test_biolinkbertbase.json

allennlp predict \
    /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/fine_tuning/utils/dygiepp/models/radgraph_biolinkbertlarge_0/model.tar.gz\
    /dataNAS/people/jmz/data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
    --cuda-device 0 \
    --predictor dygie \
    --include-package dygie \
    --use-dataset-reader\
    --silent\
    --output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/inference/predictions/radgraph/radgraph_chexpert_test_biolinkbertlarge.json

allennlp predict \
    /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/fine_tuning/utils/dygiepp/models/radgraph_bioclinicalbert_0/model.tar.gz\
    /dataNAS/people/jmz/data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
    --cuda-device 0 \
    --predictor dygie \
    --include-package dygie \
    --use-dataset-reader\
    --silent\
    --output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/inference/predictions/radgraph/radgraph_chexpert_test_bioclinicalbert.json

allennlp predict \
    /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/fine_tuning/utils/dygiepp/models/radgraph_gatortron_0/model.tar.gz\
    /dataNAS/people/jmz/data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
    --cuda-device 0 \
    --predictor dygie \
    --include-package dygie \
    --use-dataset-reader\
    --silent\
    --output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/inference/predictions/radgraph/radgraph_chexpert_test_gatortron.json

allennlp predict \
    /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/fine_tuning/utils/dygiepp/models/radgraph_radbert1_2/model.tar.gz\
    /dataNAS/people/jmz/data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
    --cuda-device 0 \
    --predictor dygie \
    --include-package dygie \
    --use-dataset-reader\
    --silent\
    --output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/inference/predictions/radgraph/radgraph_chexpert_test_radbert1.json

allennlp predict \
    /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/fine_tuning/utils/dygiepp/models/radgraph_radbert2_2/model.tar.gz\
    /dataNAS/people/jmz/data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
    --cuda-device 0 \
    --predictor dygie \
    --include-package dygie \
    --use-dataset-reader\
    --silent\
    --output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/inference/predictions/radgraph/radgraph_chexpert_test_radbert2.json

##########################################################################################
##########################################################################################
# RADSPRL
##########################################################################################
##########################################################################################
allennlp predict \
    /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/fine_tuning/utils/dygiepp/models/radsprl_bertbase_0/model.tar.gz\
    /dataNAS/people/jmz/data/RadSpRL/radsprl_dygiepp_test.jsonl \
    --cuda-device 0 \
    --predictor dygie \
    --include-package dygie \
    --use-dataset-reader\
    --silent\
    --output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/inference/predictions/radsprl/radsprl_test_bertbase.json

allennlp predict \
    /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/fine_tuning/utils/dygiepp/models/radsprl_bertlarge_11/model.tar.gz\
    /dataNAS/people/jmz/data/RadSpRL/radsprl_dygiepp_test.jsonl \
    --cuda-device 0 \
    --predictor dygie \
    --include-package dygie \
    --use-dataset-reader\
    --silent\
    --output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/inference/predictions/radsprl/radsprl_test_bertlarge.json

allennlp predict \
    /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/fine_tuning/utils/dygiepp/models/radsprl_robertabase_0/model.tar.gz\
    /dataNAS/people/jmz/data/RadSpRL/radsprl_dygiepp_test.jsonl \
    --cuda-device 0 \
    --predictor dygie \
    --include-package dygie \
    --use-dataset-reader\
    --silent\
    --output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/inference/predictions/radsprl/radsprl_test_robertabase.json

allennlp predict \
    /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/fine_tuning/utils/dygiepp/models/radsprl_robertalarge_2/model.tar.gz\
    /dataNAS/people/jmz/data/RadSpRL/radsprl_dygiepp_test.jsonl \
    --cuda-device 0 \
    --predictor dygie \
    --include-package dygie \
    --use-dataset-reader\
    --silent\
    --output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/inference/predictions/radsprl/radsprl_test_robertalarge.json

allennlp predict \
    /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/fine_tuning/utils/dygiepp/models/radsprl_electrasmall_0/model.tar.gz\
    /dataNAS/people/jmz/data/RadSpRL/radsprl_dygiepp_test.jsonl \
    --cuda-device 0 \
    --predictor dygie \
    --include-package dygie \
    --use-dataset-reader\
    --silent\
    --output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/inference/predictions/radsprl/radsprl_test_electrasmall.json

allennlp predict \
    /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/fine_tuning/utils/dygiepp/models/radsprl_electrabase_0/model.tar.gz\
    /dataNAS/people/jmz/data/RadSpRL/radsprl_dygiepp_test.jsonl \
    --cuda-device 0 \
    --predictor dygie \
    --include-package dygie \
    --use-dataset-reader\
    --silent\
    --output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/inference/predictions/radsprl/radsprl_test_electrabase.json

allennlp predict \
    /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/fine_tuning/utils/dygiepp/models/radsprl_electralarge_4/model.tar.gz\
    /dataNAS/people/jmz/data/RadSpRL/radsprl_dygiepp_test.jsonl \
    --cuda-device 0 \
    --predictor dygie \
    --include-package dygie \
    --use-dataset-reader\
    --silent\
    --output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/inference/predictions/radsprl/radsprl_test_electralarge.json

allennlp predict \
    /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/fine_tuning/utils/dygiepp/models/radsprl_debertav3base_0/model.tar.gz\
    /dataNAS/people/jmz/data/RadSpRL/radsprl_dygiepp_test.jsonl \
    --cuda-device 0 \
    --predictor dygie \
    --include-package dygie \
    --use-dataset-reader\
    --silent\
    --output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/inference/predictions/radsprl/radsprl_test_debertav3base.json

allennlp predict \
    /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/fine_tuning/utils/dygiepp/models/radsprl_debertav3large_2/model.tar.gz\
    /dataNAS/people/jmz/data/RadSpRL/radsprl_dygiepp_test.jsonl \
    --cuda-device 0 \
    --predictor dygie \
    --include-package dygie \
    --use-dataset-reader\
    --silent\
    --output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/inference/predictions/radsprl/radsprl_test_debertav3large.json

allennlp predict \
    /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/fine_tuning/utils/dygiepp/models/radsprl_pubmedbert_0/model.tar.gz\
    /dataNAS/people/jmz/data/RadSpRL/radsprl_dygiepp_test.jsonl \
    --cuda-device 0 \
    --predictor dygie \
    --include-package dygie \
    --use-dataset-reader\
    --silent\
    --output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/inference/predictions/radsprl/radsprl_test_pubmedbert.json

allennlp predict \
    /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/fine_tuning/utils/dygiepp/models/radsprl_biolinkbertbase_0/model.tar.gz\
    /dataNAS/people/jmz/data/RadSpRL/radsprl_dygiepp_test.jsonl \
    --cuda-device 0 \
    --predictor dygie \
    --include-package dygie \
    --use-dataset-reader\
    --silent\
    --output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/inference/predictions/radsprl/radsprl_test_biolinkbertbase.json

allennlp predict \
    /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/fine_tuning/utils/dygiepp/models/radsprl_biolinkbertlarge_2/model.tar.gz\
    /dataNAS/people/jmz/data/RadSpRL/radsprl_dygiepp_test.jsonl \
    --cuda-device 0 \
    --predictor dygie \
    --include-package dygie \
    --use-dataset-reader\
    --silent\
    --output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/inference/predictions/radsprl/radsprl_test_biolinkbertlarge.json

allennlp predict \
    /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/fine_tuning/utils/dygiepp/models/radsprl_bioclinicalbert_0/model.tar.gz\
    /dataNAS/people/jmz/data/RadSpRL/radsprl_dygiepp_test.jsonl \
    --cuda-device 0 \
    --predictor dygie \
    --include-package dygie \
    --use-dataset-reader\
    --silent\
    --output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/inference/predictions/radsprl/radsprl_test_bioclinicalbert.json

allennlp predict \
    /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/fine_tuning/utils/dygiepp/models/radsprl_gatortron_0/model.tar.gz\
    /dataNAS/people/jmz/data/RadSpRL/radsprl_dygiepp_test.jsonl \
    --cuda-device 0 \
    --predictor dygie \
    --include-package dygie \
    --use-dataset-reader\
    --silent\
    --output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/inference/predictions/radsprl/radsprl_test_gatortron.json

allennlp predict \
    /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/fine_tuning/utils/dygiepp/models/radsprl_radbert1_0/model.tar.gz\
    /dataNAS/people/jmz/data/RadSpRL/radsprl_dygiepp_test.jsonl \
    --cuda-device 0 \
    --predictor dygie \
    --include-package dygie \
    --use-dataset-reader\
    --silent\
    --output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/inference/predictions/radsprl/radsprl_test_radbert1.json

allennlp predict \
    /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/fine_tuning/utils/dygiepp/models/radsprl_radbert2_0/model.tar.gz\
    /dataNAS/people/jmz/data/RadSpRL/radsprl_dygiepp_test.jsonl \
    --cuda-device 0 \
    --predictor dygie \
    --include-package dygie \
    --use-dataset-reader\
    --silent\
    --output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/inference/predictions/radsprl/radsprl_test_radbert2.json