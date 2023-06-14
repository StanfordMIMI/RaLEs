cd ../fine_tuning/utils/dygiepp

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_bertbase_lp_1/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_bertbase_lp_1/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_bertbase_lp_1/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_bertbase_lp_1/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_bertbase_lp_1/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_bertbase_lp_1/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_bertbase_lp_1/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_bertbase_lp_1/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph_bertbase_lp_1/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_lp_mimiccxr_test_bertbase.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph_bertbase_lp_1/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_lp_chexpert_test_bertbase.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_bertlarge_lp_0/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_bertlarge_lp_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_bertlarge_lp_0/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_bertlarge_lp_0/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_bertlarge_lp_0/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_bertlarge_lp_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_bertlarge_lp_0/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_bertlarge_lp_0/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph_bertlarge_lp_0/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_lp_mimiccxr_test_bertlarge.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph_bertlarge_lp_0/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_lp_chexpert_test_bertlarge.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_debertav3base_lp_0/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_debertav3base_lp_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_debertav3base_lp_0/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_debertav3base_lp_0/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_debertav3base_lp_0/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_debertav3base_lp_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_debertav3base_lp_0/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_debertav3base_lp_0/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph_debertav3base_lp_0/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_lp_mimiccxr_test_debertav3base.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph_debertav3base_lp_0/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_lp_chexpert_test_debertav3base.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_electrabase_lp_0/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_electrabase_lp_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_electrabase_lp_0/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_electrabase_lp_0/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_electrabase_lp_0/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_electrabase_lp_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_electrabase_lp_0/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_electrabase_lp_0/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph_electrabase_lp_0/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_lp_mimiccxr_test_electrabase.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph_electrabase_lp_0/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_lp_chexpert_test_electrabase.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_gatortron_lp_1/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_gatortron_lp_1/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_gatortron_lp_1/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_gatortron_lp_1/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_gatortron_lp_1/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_gatortron_lp_1/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_gatortron_lp_1/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_gatortron_lp_1/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph_gatortron_lp_1/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_lp_mimiccxr_test_gatortron.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph_gatortron_lp_1/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_lp_chexpert_test_gatortron.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_pubmedbert_lp_0/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_pubmedbert_lp_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_pubmedbert_lp_0/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_pubmedbert_lp_0/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_pubmedbert_lp_0/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_pubmedbert_lp_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_pubmedbert_lp_0/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_pubmedbert_lp_0/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph_pubmedbert_lp_0/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_lp_mimiccxr_test_pubmedbert.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph_pubmedbert_lp_0/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_lp_chexpert_test_pubmedbert.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_radbert1_lp_0/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_radbert1_lp_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_radbert1_lp_0/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_radbert1_lp_0/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_radbert1_lp_0/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_radbert1_lp_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_radbert1_lp_0/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_radbert1_lp_0/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph_radbert1_lp_0/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_lp_mimiccxr_test_radbert1.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph_radbert1_lp_0/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_lp_chexpert_test_radbert1.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_radbert2_lp_0/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_radbert2_lp_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_radbert2_lp_0/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_radbert2_lp_0/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_radbert2_lp_0/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_radbert2_lp_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_radbert2_lp_0/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_radbert2_lp_0/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph_radbert2_lp_0/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_lp_mimiccxr_test_radbert2.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph_radbert2_lp_0/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_lp_chexpert_test_radbert2.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_robertabase_lp_0/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_robertabase_lp_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_robertabase_lp_0/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_robertabase_lp_0/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_robertabase_lp_0/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_robertabase_lp_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_robertabase_lp_0/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_robertabase_lp_0/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph_robertabase_lp_0/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_lp_mimiccxr_test_robertabase.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph_robertabase_lp_0/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_lp_chexpert_test_robertabase.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_robertalarge_lp_0/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_robertalarge_lp_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_robertalarge_lp_0/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_robertalarge_lp_0/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_robertalarge_lp_0/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_robertalarge_lp_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_robertalarge_lp_0/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_robertalarge_lp_0/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph_robertalarge_lp_0/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_lp_mimiccxr_test_robertalarge.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph_robertalarge_lp_0/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_lp_chexpert_test_robertalarge.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_bioclinicalbert_lp_0/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_bioclinicalbert_lp_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_bioclinicalbert_lp_0/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_bioclinicalbert_lp_0/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_bioclinicalbert_lp_0/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_bioclinicalbert_lp_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_bioclinicalbert_lp_0/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_bioclinicalbert_lp_0/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph_bioclinicalbert_lp_0/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_lp_mimiccxr_test_bioclinicalbert.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph_bioclinicalbert_lp_0/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_lp_chexpert_test_bioclinicalbert.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_biolinkbertbase_lp_0/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_biolinkbertbase_lp_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_biolinkbertbase_lp_0/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_biolinkbertbase_lp_0/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_biolinkbertbase_lp_0/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_biolinkbertbase_lp_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_biolinkbertbase_lp_0/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_biolinkbertbase_lp_0/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph_biolinkbertbase_lp_0/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_lp_mimiccxr_test_biolinkbertbase.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph_biolinkbertbase_lp_0/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_lp_chexpert_test_biolinkbertbase.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_debertav3large_lp_0/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_debertav3large_lp_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_debertav3large_lp_0/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_debertav3large_lp_0/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_debertav3large_lp_0/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_debertav3large_lp_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_debertav3large_lp_0/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_debertav3large_lp_0/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph_debertav3large_lp_0/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_lp_mimiccxr_test_debertav3large.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph_debertav3large_lp_0/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_lp_chexpert_test_debertav3large.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_electralarge_lp_0/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_electralarge_lp_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_electralarge_lp_0/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_electralarge_lp_0/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_electralarge_lp_0/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_electralarge_lp_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_electralarge_lp_0/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_electralarge_lp_0/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph_electralarge_lp_0/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_lp_mimiccxr_test_electralarge.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph_electralarge_lp_0/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_lp_chexpert_test_electralarge.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_electrasmall_lp_0/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_electrasmall_lp_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_electrasmall_lp_0/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_electrasmall_lp_0/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_electrasmall_lp_0/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_electrasmall_lp_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_electrasmall_lp_0/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_electrasmall_lp_0/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph_electrasmall_lp_0/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_lp_mimiccxr_test_electrasmall.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph_electrasmall_lp_0/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_lp_chexpert_test_electrasmall.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_biolinkbertlarge_lp_1/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_biolinkbertlarge_lp_1/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_biolinkbertlarge_lp_1/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_biolinkbertlarge_lp_1/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_biolinkbertlarge_lp_1/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_biolinkbertlarge_lp_1/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_biolinkbertlarge_lp_1/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radgraph_biolinkbertlarge_lp_1/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph_biolinkbertlarge_lp_1/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_lp_mimiccxr_test_biolinkbertlarge.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radgraph_biolinkbertlarge_lp_1/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_lp_chexpert_test_biolinkbertlarge.json 

