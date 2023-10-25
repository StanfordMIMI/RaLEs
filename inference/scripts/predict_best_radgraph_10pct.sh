cd ../fine_tuning/utils/dygiepp

mkdir /PATH_TO/models/rales/dygiepp/radgraph10pct_bertlarge_2/model
tar -xf /PATH_TO/models/rales/dygiepp/radgraph10pct_bertlarge_2/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radgraph10pct_bertlarge_2/model
cp -r /PATH_TO/models/rales/dygiepp/radgraph10pct_bertlarge_2/vocabulary /PATH_TO/models/rales/dygiepp/radgraph10pct_bertlarge_2/model
tar -czvf /PATH_TO/models/rales/dygiepp/radgraph10pct_bertlarge_2/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radgraph10pct_bertlarge_2/model . 
rm -r /PATH_TO/models/rales/dygiepp/radgraph10pct_bertlarge_2/model

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radgraph10pct_bertlarge_2/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_10pct_mimiccxr_test_bertlarge.json 

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radgraph10pct_bertlarge_2/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_10pct_chexpert_test_bertlarge.json 

mkdir /PATH_TO/models/rales/dygiepp/radgraph10pct_biolinkbertlarge_2/model
tar -xf /PATH_TO/models/rales/dygiepp/radgraph10pct_biolinkbertlarge_2/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radgraph10pct_biolinkbertlarge_2/model
cp -r /PATH_TO/models/rales/dygiepp/radgraph10pct_biolinkbertlarge_2/vocabulary /PATH_TO/models/rales/dygiepp/radgraph10pct_biolinkbertlarge_2/model
tar -czvf /PATH_TO/models/rales/dygiepp/radgraph10pct_biolinkbertlarge_2/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radgraph10pct_biolinkbertlarge_2/model . 
rm -r /PATH_TO/models/rales/dygiepp/radgraph10pct_biolinkbertlarge_2/model

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radgraph10pct_biolinkbertlarge_2/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_10pct_mimiccxr_test_biolinkbertlarge.json 

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radgraph10pct_biolinkbertlarge_2/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_10pct_chexpert_test_biolinkbertlarge.json 

mkdir /PATH_TO/models/rales/dygiepp/radgraph10pct_debertav3base_2/model
tar -xf /PATH_TO/models/rales/dygiepp/radgraph10pct_debertav3base_2/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radgraph10pct_debertav3base_2/model
cp -r /PATH_TO/models/rales/dygiepp/radgraph10pct_debertav3base_2/vocabulary /PATH_TO/models/rales/dygiepp/radgraph10pct_debertav3base_2/model
tar -czvf /PATH_TO/models/rales/dygiepp/radgraph10pct_debertav3base_2/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radgraph10pct_debertav3base_2/model . 
rm -r /PATH_TO/models/rales/dygiepp/radgraph10pct_debertav3base_2/model

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radgraph10pct_debertav3base_2/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_10pct_mimiccxr_test_debertav3base.json 

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radgraph10pct_debertav3base_2/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_10pct_chexpert_test_debertav3base.json 

mkdir /PATH_TO/models/rales/dygiepp/radgraph10pct_electrabase_2/model
tar -xf /PATH_TO/models/rales/dygiepp/radgraph10pct_electrabase_2/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radgraph10pct_electrabase_2/model
cp -r /PATH_TO/models/rales/dygiepp/radgraph10pct_electrabase_2/vocabulary /PATH_TO/models/rales/dygiepp/radgraph10pct_electrabase_2/model
tar -czvf /PATH_TO/models/rales/dygiepp/radgraph10pct_electrabase_2/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radgraph10pct_electrabase_2/model . 
rm -r /PATH_TO/models/rales/dygiepp/radgraph10pct_electrabase_2/model

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radgraph10pct_electrabase_2/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_10pct_mimiccxr_test_electrabase.json 

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radgraph10pct_electrabase_2/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_10pct_chexpert_test_electrabase.json 

mkdir /PATH_TO/models/rales/dygiepp/radgraph10pct_electralarge_2/model
tar -xf /PATH_TO/models/rales/dygiepp/radgraph10pct_electralarge_2/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radgraph10pct_electralarge_2/model
cp -r /PATH_TO/models/rales/dygiepp/radgraph10pct_electralarge_2/vocabulary /PATH_TO/models/rales/dygiepp/radgraph10pct_electralarge_2/model
tar -czvf /PATH_TO/models/rales/dygiepp/radgraph10pct_electralarge_2/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radgraph10pct_electralarge_2/model . 
rm -r /PATH_TO/models/rales/dygiepp/radgraph10pct_electralarge_2/model

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radgraph10pct_electralarge_2/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_10pct_mimiccxr_test_electralarge.json 

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radgraph10pct_electralarge_2/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_10pct_chexpert_test_electralarge.json 

mkdir /PATH_TO/models/rales/dygiepp/radgraph10pct_electrasmall_2/model
tar -xf /PATH_TO/models/rales/dygiepp/radgraph10pct_electrasmall_2/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radgraph10pct_electrasmall_2/model
cp -r /PATH_TO/models/rales/dygiepp/radgraph10pct_electrasmall_2/vocabulary /PATH_TO/models/rales/dygiepp/radgraph10pct_electrasmall_2/model
tar -czvf /PATH_TO/models/rales/dygiepp/radgraph10pct_electrasmall_2/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radgraph10pct_electrasmall_2/model . 
rm -r /PATH_TO/models/rales/dygiepp/radgraph10pct_electrasmall_2/model

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radgraph10pct_electrasmall_2/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_10pct_mimiccxr_test_electrasmall.json 

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radgraph10pct_electrasmall_2/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_10pct_chexpert_test_electrasmall.json 

mkdir /PATH_TO/models/rales/dygiepp/radgraph10pct_robertalarge_0/model
tar -xf /PATH_TO/models/rales/dygiepp/radgraph10pct_robertalarge_0/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radgraph10pct_robertalarge_0/model
cp -r /PATH_TO/models/rales/dygiepp/radgraph10pct_robertalarge_0/vocabulary /PATH_TO/models/rales/dygiepp/radgraph10pct_robertalarge_0/model
tar -czvf /PATH_TO/models/rales/dygiepp/radgraph10pct_robertalarge_0/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radgraph10pct_robertalarge_0/model . 
rm -r /PATH_TO/models/rales/dygiepp/radgraph10pct_robertalarge_0/model

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radgraph10pct_robertalarge_0/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_10pct_mimiccxr_test_robertalarge.json 

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radgraph10pct_robertalarge_0/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_10pct_chexpert_test_robertalarge.json 

mkdir /PATH_TO/models/rales/dygiepp/radgraph10pct_biolinkbertbase_2/model
tar -xf /PATH_TO/models/rales/dygiepp/radgraph10pct_biolinkbertbase_2/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radgraph10pct_biolinkbertbase_2/model
cp -r /PATH_TO/models/rales/dygiepp/radgraph10pct_biolinkbertbase_2/vocabulary /PATH_TO/models/rales/dygiepp/radgraph10pct_biolinkbertbase_2/model
tar -czvf /PATH_TO/models/rales/dygiepp/radgraph10pct_biolinkbertbase_2/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radgraph10pct_biolinkbertbase_2/model . 
rm -r /PATH_TO/models/rales/dygiepp/radgraph10pct_biolinkbertbase_2/model

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radgraph10pct_biolinkbertbase_2/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_10pct_mimiccxr_test_biolinkbertbase.json 

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radgraph10pct_biolinkbertbase_2/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_10pct_chexpert_test_biolinkbertbase.json 

mkdir /PATH_TO/models/rales/dygiepp/radgraph10pct_robertabase_0/model
tar -xf /PATH_TO/models/rales/dygiepp/radgraph10pct_robertabase_0/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radgraph10pct_robertabase_0/model
cp -r /PATH_TO/models/rales/dygiepp/radgraph10pct_robertabase_0/vocabulary /PATH_TO/models/rales/dygiepp/radgraph10pct_robertabase_0/model
tar -czvf /PATH_TO/models/rales/dygiepp/radgraph10pct_robertabase_0/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radgraph10pct_robertabase_0/model . 
rm -r /PATH_TO/models/rales/dygiepp/radgraph10pct_robertabase_0/model

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radgraph10pct_robertabase_0/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_10pct_mimiccxr_test_robertabase.json 

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radgraph10pct_robertabase_0/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_10pct_chexpert_test_robertabase.json 

mkdir /PATH_TO/models/rales/dygiepp/radgraph10pct_radbert2_2/model
tar -xf /PATH_TO/models/rales/dygiepp/radgraph10pct_radbert2_2/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radgraph10pct_radbert2_2/model
cp -r /PATH_TO/models/rales/dygiepp/radgraph10pct_radbert2_2/vocabulary /PATH_TO/models/rales/dygiepp/radgraph10pct_radbert2_2/model
tar -czvf /PATH_TO/models/rales/dygiepp/radgraph10pct_radbert2_2/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radgraph10pct_radbert2_2/model . 
rm -r /PATH_TO/models/rales/dygiepp/radgraph10pct_radbert2_2/model

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radgraph10pct_radbert2_2/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_10pct_mimiccxr_test_radbert2.json 

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radgraph10pct_radbert2_2/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_10pct_chexpert_test_radbert2.json 

mkdir /PATH_TO/models/rales/dygiepp/radgraph10pct_gatortron_0/model
tar -xf /PATH_TO/models/rales/dygiepp/radgraph10pct_gatortron_0/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radgraph10pct_gatortron_0/model
cp -r /PATH_TO/models/rales/dygiepp/radgraph10pct_gatortron_0/vocabulary /PATH_TO/models/rales/dygiepp/radgraph10pct_gatortron_0/model
tar -czvf /PATH_TO/models/rales/dygiepp/radgraph10pct_gatortron_0/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radgraph10pct_gatortron_0/model . 
rm -r /PATH_TO/models/rales/dygiepp/radgraph10pct_gatortron_0/model

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radgraph10pct_gatortron_0/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_10pct_mimiccxr_test_gatortron.json 

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radgraph10pct_gatortron_0/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_10pct_chexpert_test_gatortron.json 

mkdir /PATH_TO/models/rales/dygiepp/radgraph10pct_bertbase_2/model
tar -xf /PATH_TO/models/rales/dygiepp/radgraph10pct_bertbase_2/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radgraph10pct_bertbase_2/model
cp -r /PATH_TO/models/rales/dygiepp/radgraph10pct_bertbase_2/vocabulary /PATH_TO/models/rales/dygiepp/radgraph10pct_bertbase_2/model
tar -czvf /PATH_TO/models/rales/dygiepp/radgraph10pct_bertbase_2/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radgraph10pct_bertbase_2/model . 
rm -r /PATH_TO/models/rales/dygiepp/radgraph10pct_bertbase_2/model

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radgraph10pct_bertbase_2/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_10pct_mimiccxr_test_bertbase.json 

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radgraph10pct_bertbase_2/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_10pct_chexpert_test_bertbase.json 

mkdir /PATH_TO/models/rales/dygiepp/radgraph10pct_pubmedbert_0/model
tar -xf /PATH_TO/models/rales/dygiepp/radgraph10pct_pubmedbert_0/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radgraph10pct_pubmedbert_0/model
cp -r /PATH_TO/models/rales/dygiepp/radgraph10pct_pubmedbert_0/vocabulary /PATH_TO/models/rales/dygiepp/radgraph10pct_pubmedbert_0/model
tar -czvf /PATH_TO/models/rales/dygiepp/radgraph10pct_pubmedbert_0/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radgraph10pct_pubmedbert_0/model . 
rm -r /PATH_TO/models/rales/dygiepp/radgraph10pct_pubmedbert_0/model

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radgraph10pct_pubmedbert_0/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_10pct_mimiccxr_test_pubmedbert.json 

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radgraph10pct_pubmedbert_0/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_10pct_chexpert_test_pubmedbert.json 

mkdir /PATH_TO/models/rales/dygiepp/radgraph10pct_debertav3large_0/model
tar -xf /PATH_TO/models/rales/dygiepp/radgraph10pct_debertav3large_0/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radgraph10pct_debertav3large_0/model
cp -r /PATH_TO/models/rales/dygiepp/radgraph10pct_debertav3large_0/vocabulary /PATH_TO/models/rales/dygiepp/radgraph10pct_debertav3large_0/model
tar -czvf /PATH_TO/models/rales/dygiepp/radgraph10pct_debertav3large_0/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radgraph10pct_debertav3large_0/model . 
rm -r /PATH_TO/models/rales/dygiepp/radgraph10pct_debertav3large_0/model

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radgraph10pct_debertav3large_0/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_10pct_mimiccxr_test_debertav3large.json 

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radgraph10pct_debertav3large_0/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_10pct_chexpert_test_debertav3large.json 

mkdir /PATH_TO/models/rales/dygiepp/radgraph10pct_radbert1_0/model
tar -xf /PATH_TO/models/rales/dygiepp/radgraph10pct_radbert1_0/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radgraph10pct_radbert1_0/model
cp -r /PATH_TO/models/rales/dygiepp/radgraph10pct_radbert1_0/vocabulary /PATH_TO/models/rales/dygiepp/radgraph10pct_radbert1_0/model
tar -czvf /PATH_TO/models/rales/dygiepp/radgraph10pct_radbert1_0/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radgraph10pct_radbert1_0/model . 
rm -r /PATH_TO/models/rales/dygiepp/radgraph10pct_radbert1_0/model

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radgraph10pct_radbert1_0/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_10pct_mimiccxr_test_radbert1.json 

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radgraph10pct_radbert1_0/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_10pct_chexpert_test_radbert1.json 

mkdir /PATH_TO/models/rales/dygiepp/radgraph10pct_bioclinicalbert_2/model
tar -xf /PATH_TO/models/rales/dygiepp/radgraph10pct_bioclinicalbert_2/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radgraph10pct_bioclinicalbert_2/model
cp -r /PATH_TO/models/rales/dygiepp/radgraph10pct_bioclinicalbert_2/vocabulary /PATH_TO/models/rales/dygiepp/radgraph10pct_bioclinicalbert_2/model
tar -czvf /PATH_TO/models/rales/dygiepp/radgraph10pct_bioclinicalbert_2/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radgraph10pct_bioclinicalbert_2/model . 
rm -r /PATH_TO/models/rales/dygiepp/radgraph10pct_bioclinicalbert_2/model

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radgraph10pct_bioclinicalbert_2/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_MIMIC-CXR_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_10pct_mimiccxr_test_bioclinicalbert.json 

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radgraph10pct_bioclinicalbert_2/model.tar.gz \
	/PATH_TO//data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radgraph_10pct_chexpert_test_bioclinicalbert.json 

