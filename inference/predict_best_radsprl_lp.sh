cd ../fine_tuning/utils/dygiepp

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_bertlarge_lp_0/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_bertlarge_lp_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_bertlarge_lp_0/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_bertlarge_lp_0/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_bertlarge_lp_0/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_bertlarge_lp_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_bertlarge_lp_0/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_bertlarge_lp_0/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl_bertlarge_lp_0/model.tar.gz \
	/dataNAS/people/jmz/data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/results/re/radsprl_lp_test_bertlarge.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl_bertlarge_lp_0/model.tar.gz \
	/dataNAS/people/jmz/data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/results/re/radsprl_lp_test_bertlarge.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_bioclinicalbert_lp_0/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_bioclinicalbert_lp_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_bioclinicalbert_lp_0/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_bioclinicalbert_lp_0/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_bioclinicalbert_lp_0/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_bioclinicalbert_lp_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_bioclinicalbert_lp_0/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_bioclinicalbert_lp_0/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl_bioclinicalbert_lp_0/model.tar.gz \
	/dataNAS/people/jmz/data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/results/re/radsprl_lp_test_bioclinicalbert.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl_bioclinicalbert_lp_0/model.tar.gz \
	/dataNAS/people/jmz/data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/results/re/radsprl_lp_test_bioclinicalbert.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_biolinkbertlarge_lp_0/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_biolinkbertlarge_lp_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_biolinkbertlarge_lp_0/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_biolinkbertlarge_lp_0/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_biolinkbertlarge_lp_0/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_biolinkbertlarge_lp_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_biolinkbertlarge_lp_0/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_biolinkbertlarge_lp_0/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl_biolinkbertlarge_lp_0/model.tar.gz \
	/dataNAS/people/jmz/data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/results/re/radsprl_lp_test_biolinkbertlarge.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl_biolinkbertlarge_lp_0/model.tar.gz \
	/dataNAS/people/jmz/data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/results/re/radsprl_lp_test_biolinkbertlarge.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_debertav3base_lp_0/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_debertav3base_lp_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_debertav3base_lp_0/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_debertav3base_lp_0/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_debertav3base_lp_0/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_debertav3base_lp_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_debertav3base_lp_0/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_debertav3base_lp_0/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl_debertav3base_lp_0/model.tar.gz \
	/dataNAS/people/jmz/data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/results/re/radsprl_lp_test_debertav3base.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl_debertav3base_lp_0/model.tar.gz \
	/dataNAS/people/jmz/data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/results/re/radsprl_lp_test_debertav3base.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_debertav3large_lp_0/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_debertav3large_lp_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_debertav3large_lp_0/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_debertav3large_lp_0/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_debertav3large_lp_0/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_debertav3large_lp_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_debertav3large_lp_0/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_debertav3large_lp_0/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl_debertav3large_lp_0/model.tar.gz \
	/dataNAS/people/jmz/data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/results/re/radsprl_lp_test_debertav3large.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl_debertav3large_lp_0/model.tar.gz \
	/dataNAS/people/jmz/data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/results/re/radsprl_lp_test_debertav3large.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_electrasmall_lp_0/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_electrasmall_lp_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_electrasmall_lp_0/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_electrasmall_lp_0/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_electrasmall_lp_0/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_electrasmall_lp_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_electrasmall_lp_0/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_electrasmall_lp_0/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl_electrasmall_lp_0/model.tar.gz \
	/dataNAS/people/jmz/data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/results/re/radsprl_lp_test_electrasmall.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl_electrasmall_lp_0/model.tar.gz \
	/dataNAS/people/jmz/data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/results/re/radsprl_lp_test_electrasmall.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_gatortron_lp_0/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_gatortron_lp_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_gatortron_lp_0/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_gatortron_lp_0/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_gatortron_lp_0/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_gatortron_lp_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_gatortron_lp_0/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_gatortron_lp_0/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl_gatortron_lp_0/model.tar.gz \
	/dataNAS/people/jmz/data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/results/re/radsprl_lp_test_gatortron.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl_gatortron_lp_0/model.tar.gz \
	/dataNAS/people/jmz/data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/results/re/radsprl_lp_test_gatortron.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_robertalarge_lp_0/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_robertalarge_lp_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_robertalarge_lp_0/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_robertalarge_lp_0/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_robertalarge_lp_0/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_robertalarge_lp_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_robertalarge_lp_0/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_robertalarge_lp_0/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl_robertalarge_lp_0/model.tar.gz \
	/dataNAS/people/jmz/data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/results/re/radsprl_lp_test_robertalarge.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl_robertalarge_lp_0/model.tar.gz \
	/dataNAS/people/jmz/data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/results/re/radsprl_lp_test_robertalarge.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_electrabase_lp_0/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_electrabase_lp_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_electrabase_lp_0/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_electrabase_lp_0/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_electrabase_lp_0/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_electrabase_lp_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_electrabase_lp_0/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_electrabase_lp_0/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl_electrabase_lp_0/model.tar.gz \
	/dataNAS/people/jmz/data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/results/re/radsprl_lp_test_electrabase.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl_electrabase_lp_0/model.tar.gz \
	/dataNAS/people/jmz/data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/results/re/radsprl_lp_test_electrabase.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_electralarge_lp_0/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_electralarge_lp_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_electralarge_lp_0/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_electralarge_lp_0/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_electralarge_lp_0/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_electralarge_lp_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_electralarge_lp_0/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_electralarge_lp_0/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl_electralarge_lp_0/model.tar.gz \
	/dataNAS/people/jmz/data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/results/re/radsprl_lp_test_electralarge.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl_electralarge_lp_0/model.tar.gz \
	/dataNAS/people/jmz/data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/results/re/radsprl_lp_test_electralarge.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_pubmedbert_lp_0/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_pubmedbert_lp_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_pubmedbert_lp_0/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_pubmedbert_lp_0/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_pubmedbert_lp_0/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_pubmedbert_lp_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_pubmedbert_lp_0/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_pubmedbert_lp_0/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl_pubmedbert_lp_0/model.tar.gz \
	/dataNAS/people/jmz/data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/results/re/radsprl_lp_test_pubmedbert.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl_pubmedbert_lp_0/model.tar.gz \
	/dataNAS/people/jmz/data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/results/re/radsprl_lp_test_pubmedbert.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_radbert2_lp_0/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_radbert2_lp_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_radbert2_lp_0/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_radbert2_lp_0/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_radbert2_lp_0/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_radbert2_lp_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_radbert2_lp_0/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_radbert2_lp_0/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl_radbert2_lp_0/model.tar.gz \
	/dataNAS/people/jmz/data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/results/re/radsprl_lp_test_radbert2.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl_radbert2_lp_0/model.tar.gz \
	/dataNAS/people/jmz/data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/results/re/radsprl_lp_test_radbert2.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_robertabase_lp_0/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_robertabase_lp_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_robertabase_lp_0/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_robertabase_lp_0/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_robertabase_lp_0/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_robertabase_lp_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_robertabase_lp_0/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_robertabase_lp_0/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl_robertabase_lp_0/model.tar.gz \
	/dataNAS/people/jmz/data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/results/re/radsprl_lp_test_robertabase.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl_robertabase_lp_0/model.tar.gz \
	/dataNAS/people/jmz/data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/results/re/radsprl_lp_test_robertabase.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_bertbase_lp_0/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_bertbase_lp_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_bertbase_lp_0/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_bertbase_lp_0/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_bertbase_lp_0/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_bertbase_lp_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_bertbase_lp_0/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_bertbase_lp_0/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl_bertbase_lp_0/model.tar.gz \
	/dataNAS/people/jmz/data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/results/re/radsprl_lp_test_bertbase.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl_bertbase_lp_0/model.tar.gz \
	/dataNAS/people/jmz/data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/results/re/radsprl_lp_test_bertbase.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_biolinkbertbase_lp_0/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_biolinkbertbase_lp_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_biolinkbertbase_lp_0/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_biolinkbertbase_lp_0/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_biolinkbertbase_lp_0/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_biolinkbertbase_lp_0/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_biolinkbertbase_lp_0/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_biolinkbertbase_lp_0/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl_biolinkbertbase_lp_0/model.tar.gz \
	/dataNAS/people/jmz/data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/results/re/radsprl_lp_test_biolinkbertbase.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl_biolinkbertbase_lp_0/model.tar.gz \
	/dataNAS/people/jmz/data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/results/re/radsprl_lp_test_biolinkbertbase.json 

mkdir /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_radbert1_lp_1/model
tar -xf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_radbert1_lp_1/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_radbert1_lp_1/model
cp -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_radbert1_lp_1/vocabulary /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_radbert1_lp_1/model
tar -czvf /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_radbert1_lp_1/model.tar.gz -C /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_radbert1_lp_1/model . 
rm -r /bmrNAS/people/jmz/models/rales/dygiepp/radsprl_radbert1_lp_1/model

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl_radbert1_lp_1/model.tar.gz \
	/dataNAS/people/jmz/data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/results/re/radsprl_lp_test_radbert1.json 

allennlp evaluate \
	/bmrNAS/people/jmz/models/rales/dygiepp/radsprl_radbert1_lp_1/model.tar.gz \
	/dataNAS/people/jmz/data/RadSpRL/radsprl_dygiepp_test.jsonl \
	--cuda-device 0 \
	--include-package dygie \
	--output-file /dataNAS/people/jmz/jmz_code/radiology_nlp/rales/results/re/radsprl_lp_test_radbert1.json 

