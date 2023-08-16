cd ../fine_tuning/utils/dygiepp

mkdir /PATH_TO/models/rales/dygiepp/radsprl1pct_bertbase_2/model
tar -xf /PATH_TO/models/rales/dygiepp/radsprl1pct_bertbase_2/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radsprl1pct_bertbase_2/model
cp -r /PATH_TO/models/rales/dygiepp/radsprl1pct_bertbase_2/vocabulary /PATH_TO/models/rales/dygiepp/radsprl1pct_bertbase_2/model
tar -czvf /PATH_TO/models/rales/dygiepp/radsprl1pct_bertbase_2/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radsprl1pct_bertbase_2/model . 
rm -r /PATH_TO/models/rales/dygiepp/radsprl1pct_bertbase_2/model

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radsprl1pct_bertbase_2/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_test_bertbase.json 

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radsprl1pct_bertbase_2/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_chexpert_test_bertbase.json 

mkdir /PATH_TO/models/rales/dygiepp/radsprl1pct_bioclinicalbert_2/model
tar -xf /PATH_TO/models/rales/dygiepp/radsprl1pct_bioclinicalbert_2/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radsprl1pct_bioclinicalbert_2/model
cp -r /PATH_TO/models/rales/dygiepp/radsprl1pct_bioclinicalbert_2/vocabulary /PATH_TO/models/rales/dygiepp/radsprl1pct_bioclinicalbert_2/model
tar -czvf /PATH_TO/models/rales/dygiepp/radsprl1pct_bioclinicalbert_2/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radsprl1pct_bioclinicalbert_2/model . 
rm -r /PATH_TO/models/rales/dygiepp/radsprl1pct_bioclinicalbert_2/model

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radsprl1pct_bioclinicalbert_2/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_test_bioclinicalbert.json 

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radsprl1pct_bioclinicalbert_2/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_chexpert_test_bioclinicalbert.json 

mkdir /PATH_TO/models/rales/dygiepp/radsprl1pct_biolinkbertlarge_2/model
tar -xf /PATH_TO/models/rales/dygiepp/radsprl1pct_biolinkbertlarge_2/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radsprl1pct_biolinkbertlarge_2/model
cp -r /PATH_TO/models/rales/dygiepp/radsprl1pct_biolinkbertlarge_2/vocabulary /PATH_TO/models/rales/dygiepp/radsprl1pct_biolinkbertlarge_2/model
tar -czvf /PATH_TO/models/rales/dygiepp/radsprl1pct_biolinkbertlarge_2/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radsprl1pct_biolinkbertlarge_2/model . 
rm -r /PATH_TO/models/rales/dygiepp/radsprl1pct_biolinkbertlarge_2/model

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radsprl1pct_biolinkbertlarge_2/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_test_biolinkbertlarge.json 

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radsprl1pct_biolinkbertlarge_2/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_chexpert_test_biolinkbertlarge.json 

mkdir /PATH_TO/models/rales/dygiepp/radsprl1pct_electrabase_2/model
tar -xf /PATH_TO/models/rales/dygiepp/radsprl1pct_electrabase_2/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radsprl1pct_electrabase_2/model
cp -r /PATH_TO/models/rales/dygiepp/radsprl1pct_electrabase_2/vocabulary /PATH_TO/models/rales/dygiepp/radsprl1pct_electrabase_2/model
tar -czvf /PATH_TO/models/rales/dygiepp/radsprl1pct_electrabase_2/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radsprl1pct_electrabase_2/model . 
rm -r /PATH_TO/models/rales/dygiepp/radsprl1pct_electrabase_2/model

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radsprl1pct_electrabase_2/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_test_electrabase.json 

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radsprl1pct_electrabase_2/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_chexpert_test_electrabase.json 

mkdir /PATH_TO/models/rales/dygiepp/radsprl1pct_electralarge_2/model
tar -xf /PATH_TO/models/rales/dygiepp/radsprl1pct_electralarge_2/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radsprl1pct_electralarge_2/model
cp -r /PATH_TO/models/rales/dygiepp/radsprl1pct_electralarge_2/vocabulary /PATH_TO/models/rales/dygiepp/radsprl1pct_electralarge_2/model
tar -czvf /PATH_TO/models/rales/dygiepp/radsprl1pct_electralarge_2/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radsprl1pct_electralarge_2/model . 
rm -r /PATH_TO/models/rales/dygiepp/radsprl1pct_electralarge_2/model

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radsprl1pct_electralarge_2/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_test_electralarge.json 

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radsprl1pct_electralarge_2/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_chexpert_test_electralarge.json 

mkdir /PATH_TO/models/rales/dygiepp/radsprl1pct_robertalarge_2/model
tar -xf /PATH_TO/models/rales/dygiepp/radsprl1pct_robertalarge_2/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radsprl1pct_robertalarge_2/model
cp -r /PATH_TO/models/rales/dygiepp/radsprl1pct_robertalarge_2/vocabulary /PATH_TO/models/rales/dygiepp/radsprl1pct_robertalarge_2/model
tar -czvf /PATH_TO/models/rales/dygiepp/radsprl1pct_robertalarge_2/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radsprl1pct_robertalarge_2/model . 
rm -r /PATH_TO/models/rales/dygiepp/radsprl1pct_robertalarge_2/model

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radsprl1pct_robertalarge_2/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_test_robertalarge.json 

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radsprl1pct_robertalarge_2/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_chexpert_test_robertalarge.json 

mkdir /PATH_TO/models/rales/dygiepp/radsprl1pct_biolinkbertbase_2/model
tar -xf /PATH_TO/models/rales/dygiepp/radsprl1pct_biolinkbertbase_2/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radsprl1pct_biolinkbertbase_2/model
cp -r /PATH_TO/models/rales/dygiepp/radsprl1pct_biolinkbertbase_2/vocabulary /PATH_TO/models/rales/dygiepp/radsprl1pct_biolinkbertbase_2/model
tar -czvf /PATH_TO/models/rales/dygiepp/radsprl1pct_biolinkbertbase_2/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radsprl1pct_biolinkbertbase_2/model . 
rm -r /PATH_TO/models/rales/dygiepp/radsprl1pct_biolinkbertbase_2/model

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radsprl1pct_biolinkbertbase_2/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_test_biolinkbertbase.json 

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radsprl1pct_biolinkbertbase_2/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_chexpert_test_biolinkbertbase.json 

mkdir /PATH_TO/models/rales/dygiepp/radsprl1pct_bertlarge_2/model
tar -xf /PATH_TO/models/rales/dygiepp/radsprl1pct_bertlarge_2/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radsprl1pct_bertlarge_2/model
cp -r /PATH_TO/models/rales/dygiepp/radsprl1pct_bertlarge_2/vocabulary /PATH_TO/models/rales/dygiepp/radsprl1pct_bertlarge_2/model
tar -czvf /PATH_TO/models/rales/dygiepp/radsprl1pct_bertlarge_2/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radsprl1pct_bertlarge_2/model . 
rm -r /PATH_TO/models/rales/dygiepp/radsprl1pct_bertlarge_2/model

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radsprl1pct_bertlarge_2/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_test_bertlarge.json 

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radsprl1pct_bertlarge_2/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_chexpert_test_bertlarge.json 

mkdir /PATH_TO/models/rales/dygiepp/radsprl1pct_debertav3base_0/model
tar -xf /PATH_TO/models/rales/dygiepp/radsprl1pct_debertav3base_0/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radsprl1pct_debertav3base_0/model
cp -r /PATH_TO/models/rales/dygiepp/radsprl1pct_debertav3base_0/vocabulary /PATH_TO/models/rales/dygiepp/radsprl1pct_debertav3base_0/model
tar -czvf /PATH_TO/models/rales/dygiepp/radsprl1pct_debertav3base_0/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radsprl1pct_debertav3base_0/model . 
rm -r /PATH_TO/models/rales/dygiepp/radsprl1pct_debertav3base_0/model

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radsprl1pct_debertav3base_0/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_test_debertav3base.json 

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radsprl1pct_debertav3base_0/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_chexpert_test_debertav3base.json 

mkdir /PATH_TO/models/rales/dygiepp/radsprl1pct_electrasmall_2/model
tar -xf /PATH_TO/models/rales/dygiepp/radsprl1pct_electrasmall_2/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radsprl1pct_electrasmall_2/model
cp -r /PATH_TO/models/rales/dygiepp/radsprl1pct_electrasmall_2/vocabulary /PATH_TO/models/rales/dygiepp/radsprl1pct_electrasmall_2/model
tar -czvf /PATH_TO/models/rales/dygiepp/radsprl1pct_electrasmall_2/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radsprl1pct_electrasmall_2/model . 
rm -r /PATH_TO/models/rales/dygiepp/radsprl1pct_electrasmall_2/model

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radsprl1pct_electrasmall_2/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_test_electrasmall.json 

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radsprl1pct_electrasmall_2/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_chexpert_test_electrasmall.json 

mkdir /PATH_TO/models/rales/dygiepp/radsprl1pct_gatortron_2/model
tar -xf /PATH_TO/models/rales/dygiepp/radsprl1pct_gatortron_2/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radsprl1pct_gatortron_2/model
cp -r /PATH_TO/models/rales/dygiepp/radsprl1pct_gatortron_2/vocabulary /PATH_TO/models/rales/dygiepp/radsprl1pct_gatortron_2/model
tar -czvf /PATH_TO/models/rales/dygiepp/radsprl1pct_gatortron_2/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radsprl1pct_gatortron_2/model . 
rm -r /PATH_TO/models/rales/dygiepp/radsprl1pct_gatortron_2/model

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radsprl1pct_gatortron_2/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_test_gatortron.json 

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radsprl1pct_gatortron_2/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_chexpert_test_gatortron.json 

mkdir /PATH_TO/models/rales/dygiepp/radsprl1pct_radbert1_2/model
tar -xf /PATH_TO/models/rales/dygiepp/radsprl1pct_radbert1_2/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radsprl1pct_radbert1_2/model
cp -r /PATH_TO/models/rales/dygiepp/radsprl1pct_radbert1_2/vocabulary /PATH_TO/models/rales/dygiepp/radsprl1pct_radbert1_2/model
tar -czvf /PATH_TO/models/rales/dygiepp/radsprl1pct_radbert1_2/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radsprl1pct_radbert1_2/model . 
rm -r /PATH_TO/models/rales/dygiepp/radsprl1pct_radbert1_2/model

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radsprl1pct_radbert1_2/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_test_radbert1.json 

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radsprl1pct_radbert1_2/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_chexpert_test_radbert1.json 

mkdir /PATH_TO/models/rales/dygiepp/radsprl1pct_radbert2_2/model
tar -xf /PATH_TO/models/rales/dygiepp/radsprl1pct_radbert2_2/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radsprl1pct_radbert2_2/model
cp -r /PATH_TO/models/rales/dygiepp/radsprl1pct_radbert2_2/vocabulary /PATH_TO/models/rales/dygiepp/radsprl1pct_radbert2_2/model
tar -czvf /PATH_TO/models/rales/dygiepp/radsprl1pct_radbert2_2/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radsprl1pct_radbert2_2/model . 
rm -r /PATH_TO/models/rales/dygiepp/radsprl1pct_radbert2_2/model

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radsprl1pct_radbert2_2/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_test_radbert2.json 

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radsprl1pct_radbert2_2/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_chexpert_test_radbert2.json 

mkdir /PATH_TO/models/rales/dygiepp/radsprl1pct_pubmedbert_2/model
tar -xf /PATH_TO/models/rales/dygiepp/radsprl1pct_pubmedbert_2/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radsprl1pct_pubmedbert_2/model
cp -r /PATH_TO/models/rales/dygiepp/radsprl1pct_pubmedbert_2/vocabulary /PATH_TO/models/rales/dygiepp/radsprl1pct_pubmedbert_2/model
tar -czvf /PATH_TO/models/rales/dygiepp/radsprl1pct_pubmedbert_2/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radsprl1pct_pubmedbert_2/model . 
rm -r /PATH_TO/models/rales/dygiepp/radsprl1pct_pubmedbert_2/model

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radsprl1pct_pubmedbert_2/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_test_pubmedbert.json 

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radsprl1pct_pubmedbert_2/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_chexpert_test_pubmedbert.json 

mkdir /PATH_TO/models/rales/dygiepp/radsprl1pct_debertav3large_2/model
tar -xf /PATH_TO/models/rales/dygiepp/radsprl1pct_debertav3large_2/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radsprl1pct_debertav3large_2/model
cp -r /PATH_TO/models/rales/dygiepp/radsprl1pct_debertav3large_2/vocabulary /PATH_TO/models/rales/dygiepp/radsprl1pct_debertav3large_2/model
tar -czvf /PATH_TO/models/rales/dygiepp/radsprl1pct_debertav3large_2/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radsprl1pct_debertav3large_2/model . 
rm -r /PATH_TO/models/rales/dygiepp/radsprl1pct_debertav3large_2/model

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radsprl1pct_debertav3large_2/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_test_debertav3large.json 

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radsprl1pct_debertav3large_2/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_chexpert_test_debertav3large.json 

mkdir /PATH_TO/models/rales/dygiepp/radsprl1pct_robertabase_2/model
tar -xf /PATH_TO/models/rales/dygiepp/radsprl1pct_robertabase_2/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radsprl1pct_robertabase_2/model
cp -r /PATH_TO/models/rales/dygiepp/radsprl1pct_robertabase_2/vocabulary /PATH_TO/models/rales/dygiepp/radsprl1pct_robertabase_2/model
tar -czvf /PATH_TO/models/rales/dygiepp/radsprl1pct_robertabase_2/model.tar.gz -C /PATH_TO/models/rales/dygiepp/radsprl1pct_robertabase_2/model . 
rm -r /PATH_TO/models/rales/dygiepp/radsprl1pct_robertabase_2/model

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radsprl1pct_robertabase_2/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_test_robertabase.json 

allennlp evaluate \
	/PATH_TO/models/rales/dygiepp/radsprl1pct_robertabase_2/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_chexpert_test_robertabase.json 

