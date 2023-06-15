cd ../fine_tuning/utils/dygiepp

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_biolinkbertbase_2/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_biolinkbertbase_2/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_biolinkbertbase_2/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_biolinkbertbase_2/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_biolinkbertbase_2/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_biolinkbertbase_2/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_biolinkbertbase_2/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_biolinkbertbase_2/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_biolinkbertbase_2/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_1pct_mimiccxr_test_biolinkbertbase.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_biolinkbertbase_2/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_1pct_chexpert_test_biolinkbertbase.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_debertav3base_2/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_debertav3base_2/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_debertav3base_2/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_debertav3base_2/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_debertav3base_2/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_debertav3base_2/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_debertav3base_2/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_debertav3base_2/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_debertav3base_2/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_1pct_mimiccxr_test_debertav3base.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_debertav3base_2/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_1pct_chexpert_test_debertav3base.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_electrabase_2/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_electrabase_2/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_electrabase_2/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_electrabase_2/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_electrabase_2/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_electrabase_2/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_electrabase_2/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_electrabase_2/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_electrabase_2/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_1pct_mimiccxr_test_electrabase.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_electrabase_2/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_1pct_chexpert_test_electrabase.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_electrasmall_1/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_electrasmall_1/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_electrasmall_1/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_electrasmall_1/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_electrasmall_1/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_electrasmall_1/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_electrasmall_1/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_electrasmall_1/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_electrasmall_1/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_1pct_mimiccxr_test_electrasmall.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_electrasmall_1/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_1pct_chexpert_test_electrasmall.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_gatortron_0/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_gatortron_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_gatortron_0/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_gatortron_0/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_gatortron_0/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_gatortron_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_gatortron_0/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_gatortron_0/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_gatortron_0/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_1pct_mimiccxr_test_gatortron.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_gatortron_0/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_1pct_chexpert_test_gatortron.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_radbert1_0/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_radbert1_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_radbert1_0/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_radbert1_0/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_radbert1_0/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_radbert1_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_radbert1_0/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_radbert1_0/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_radbert1_0/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_1pct_mimiccxr_test_radbert1.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_radbert1_0/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_1pct_chexpert_test_radbert1.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_radbert2_1/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_radbert2_1/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_radbert2_1/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_radbert2_1/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_radbert2_1/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_radbert2_1/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_radbert2_1/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_radbert2_1/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_radbert2_1/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_1pct_mimiccxr_test_radbert2.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_radbert2_1/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_1pct_chexpert_test_radbert2.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_robertalarge_2/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_robertalarge_2/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_robertalarge_2/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_robertalarge_2/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_robertalarge_2/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_robertalarge_2/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_robertalarge_2/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_robertalarge_2/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_robertalarge_2/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_1pct_mimiccxr_test_robertalarge.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_robertalarge_2/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_1pct_chexpert_test_robertalarge.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_pubmedbert_2/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_pubmedbert_2/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_pubmedbert_2/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_pubmedbert_2/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_pubmedbert_2/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_pubmedbert_2/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_pubmedbert_2/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_pubmedbert_2/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_pubmedbert_2/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_1pct_mimiccxr_test_pubmedbert.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_pubmedbert_2/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_1pct_chexpert_test_pubmedbert.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_debertav3large_2/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_debertav3large_2/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_debertav3large_2/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_debertav3large_2/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_debertav3large_2/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_debertav3large_2/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_debertav3large_2/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_debertav3large_2/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_debertav3large_2/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_1pct_mimiccxr_test_debertav3large.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_debertav3large_2/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_1pct_chexpert_test_debertav3large.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_bioclinicalbert_2/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_bioclinicalbert_2/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_bioclinicalbert_2/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_bioclinicalbert_2/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_bioclinicalbert_2/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_bioclinicalbert_2/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_bioclinicalbert_2/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_bioclinicalbert_2/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_bioclinicalbert_2/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_1pct_mimiccxr_test_bioclinicalbert.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_bioclinicalbert_2/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_1pct_chexpert_test_bioclinicalbert.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_electralarge_2/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_electralarge_2/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_electralarge_2/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_electralarge_2/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_electralarge_2/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_electralarge_2/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_electralarge_2/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_electralarge_2/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_electralarge_2/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_1pct_mimiccxr_test_electralarge.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_electralarge_2/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_1pct_chexpert_test_electralarge.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_biolinkbertlarge_2/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_biolinkbertlarge_2/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_biolinkbertlarge_2/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_biolinkbertlarge_2/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_biolinkbertlarge_2/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_biolinkbertlarge_2/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_biolinkbertlarge_2/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_biolinkbertlarge_2/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_biolinkbertlarge_2/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_1pct_mimiccxr_test_biolinkbertlarge.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_biolinkbertlarge_2/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_1pct_chexpert_test_biolinkbertlarge.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_bertlarge_1/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_bertlarge_1/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_bertlarge_1/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_bertlarge_1/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_bertlarge_1/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_bertlarge_1/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_bertlarge_1/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_bertlarge_1/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_bertlarge_1/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_1pct_mimiccxr_test_bertlarge.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_bertlarge_1/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_1pct_chexpert_test_bertlarge.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_robertabase_2/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_robertabase_2/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_robertabase_2/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_robertabase_2/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_robertabase_2/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_robertabase_2/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_robertabase_2/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_robertabase_2/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_robertabase_2/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_1pct_mimiccxr_test_robertabase.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_robertabase_2/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_1pct_chexpert_test_robertabase.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_bertbase_2/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_bertbase_2/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_bertbase_2/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_bertbase_2/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_bertbase_2/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_bertbase_2/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_bertbase_2/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_bertbase_2/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_bertbase_2/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_1pct_mimiccxr_test_bertbase.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph1pct_bertbase_2/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_1pct_chexpert_test_bertbase.json 

