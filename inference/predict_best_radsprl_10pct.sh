cd ../fine_tuning/utils/dygiepp

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_bertlarge_0/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_bertlarge_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_bertlarge_0/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_bertlarge_0/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_bertlarge_0/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_bertlarge_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_bertlarge_0/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_bertlarge_0/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_bertlarge_0/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_test_bertlarge.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_bertlarge_0/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_chexpert_test_bertlarge.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_bioclinicalbert_0/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_bioclinicalbert_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_bioclinicalbert_0/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_bioclinicalbert_0/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_bioclinicalbert_0/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_bioclinicalbert_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_bioclinicalbert_0/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_bioclinicalbert_0/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_bioclinicalbert_0/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_test_bioclinicalbert.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_bioclinicalbert_0/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_chexpert_test_bioclinicalbert.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_biolinkbertlarge_1/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_biolinkbertlarge_1/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_biolinkbertlarge_1/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_biolinkbertlarge_1/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_biolinkbertlarge_1/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_biolinkbertlarge_1/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_biolinkbertlarge_1/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_biolinkbertlarge_1/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_biolinkbertlarge_1/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_test_biolinkbertlarge.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_biolinkbertlarge_1/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_chexpert_test_biolinkbertlarge.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_debertav3large_1/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_debertav3large_1/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_debertav3large_1/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_debertav3large_1/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_debertav3large_1/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_debertav3large_1/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_debertav3large_1/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_debertav3large_1/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_debertav3large_1/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_test_debertav3large.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_debertav3large_1/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_chexpert_test_debertav3large.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_electrabase_0/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_electrabase_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_electrabase_0/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_electrabase_0/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_electrabase_0/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_electrabase_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_electrabase_0/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_electrabase_0/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_electrabase_0/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_test_electrabase.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_electrabase_0/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_chexpert_test_electrabase.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_electralarge_2/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_electralarge_2/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_electralarge_2/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_electralarge_2/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_electralarge_2/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_electralarge_2/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_electralarge_2/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_electralarge_2/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_electralarge_2/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_test_electralarge.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_electralarge_2/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_chexpert_test_electralarge.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_gatortron_0/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_gatortron_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_gatortron_0/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_gatortron_0/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_gatortron_0/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_gatortron_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_gatortron_0/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_gatortron_0/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_gatortron_0/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_test_gatortron.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_gatortron_0/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_chexpert_test_gatortron.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_radbert1_2/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_radbert1_2/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_radbert1_2/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_radbert1_2/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_radbert1_2/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_radbert1_2/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_radbert1_2/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_radbert1_2/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_radbert1_2/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_test_radbert1.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_radbert1_2/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_chexpert_test_radbert1.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_robertalarge_0/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_robertalarge_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_robertalarge_0/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_robertalarge_0/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_robertalarge_0/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_robertalarge_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_robertalarge_0/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_robertalarge_0/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_robertalarge_0/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_test_robertalarge.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_robertalarge_0/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_chexpert_test_robertalarge.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_biolinkbertbase_0/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_biolinkbertbase_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_biolinkbertbase_0/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_biolinkbertbase_0/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_biolinkbertbase_0/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_biolinkbertbase_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_biolinkbertbase_0/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_biolinkbertbase_0/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_biolinkbertbase_0/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_test_biolinkbertbase.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_biolinkbertbase_0/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_chexpert_test_biolinkbertbase.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_pubmedbert_0/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_pubmedbert_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_pubmedbert_0/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_pubmedbert_0/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_pubmedbert_0/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_pubmedbert_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_pubmedbert_0/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_pubmedbert_0/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_pubmedbert_0/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_test_pubmedbert.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_pubmedbert_0/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_chexpert_test_pubmedbert.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_bertbase_0/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_bertbase_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_bertbase_0/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_bertbase_0/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_bertbase_0/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_bertbase_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_bertbase_0/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_bertbase_0/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_bertbase_0/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_test_bertbase.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_bertbase_0/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_chexpert_test_bertbase.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_debertav3base_1/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_debertav3base_1/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_debertav3base_1/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_debertav3base_1/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_debertav3base_1/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_debertav3base_1/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_debertav3base_1/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_debertav3base_1/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_debertav3base_1/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_test_debertav3base.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_debertav3base_1/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_chexpert_test_debertav3base.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_electrasmall_2/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_electrasmall_2/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_electrasmall_2/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_electrasmall_2/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_electrasmall_2/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_electrasmall_2/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_electrasmall_2/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_electrasmall_2/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_electrasmall_2/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_test_electrasmall.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_electrasmall_2/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_chexpert_test_electrasmall.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_radbert2_0/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_radbert2_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_radbert2_0/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_radbert2_0/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_radbert2_0/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_radbert2_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_radbert2_0/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_radbert2_0/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_radbert2_0/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_test_radbert2.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_radbert2_0/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_chexpert_test_radbert2.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_robertabase_0/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_robertabase_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_robertabase_0/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_robertabase_0/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_robertabase_0/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_robertabase_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_robertabase_0/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_robertabase_0/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_robertabase_0/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_test_robertabase.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl10pct_robertabase_0/model.tar.gz \
	/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /PATH_TO//jmz_code/radiology_nlp/rales/results/re/radsprl_1pct_chexpert_test_robertabase.json 

