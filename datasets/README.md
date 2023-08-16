
## RaLEs Datasets

**Note**: Users with appropriate Physionet credentials can directly download preprocessed datasets from [Vilmedic Datasets](https://vilmedic.app/datasets/text).

Alternatively, you can follow the following steps to obtain each dataset.

### Natural Language Understanding (NLU) Datasets

#### 1. RadGraph
- **Download**: Access the dataset on [Physionet](https://physionet.org/content/radgraph/1.0.0/).
- **Preprocessing**: Run the `convert_radgraph_to_dygiepp.py` script, specifying the location where the RadGraph dataset is saved.

#### 2. RadSpRL
- **Download**: Get the `Rad-SpRL.xml` file from [Mendeley](https://data.mendeley.com/datasets/yhb26hfz8n).
- **Preprocessing**: Run the `convert_radsprl_to_dygiepp.py` script, specifying the location where the RadSpRL dataset is saved.

#### 3. MIMIC Procedure Selection
- **Download**: Access the [MIMIC-III dataset](https://physionet.org/content/mimiciii/1.4/).
- **Preprocessing**: In the `mimiciii_procedure_selection` folder, run the `create_dataset.py` followed by the `create_train_dev_test_split.py` scripts, specifying the location where the MIMIC dataset is saved.

#### 4. Stanza NER
A link for access to this dataset will be provided upon institutional review board approval. The dataset will be provided without requiring further preprocessing.

### Natural Language Generation (NLG) Datasets

#### 1. MEDIQA 2021 Radiology Report Summarization
- **Download**: Follow the instructions for dataset download on [GitHub](https://github.com/abachaa/MEDIQA2021/tree/main/Task3).

#### 2. BioNLP2023 Radiology Report Summarization

- **ViLMedic download** You can download this directly from [ViLMedic](https://vilmedic.app/misc/bionlp23/sharedtask)

- **Download**: You must create a Physionet account with permissions to download the MIMIC-CXR Database. Get the `mimic-cxr-reports.zip` and related files from [Physionet](https://physionet.org/content/mimic-cxr/2.0.0/mimic-cxr-reports.zip) and organize them as mentioned.
- **Preprocessing**: Navigate to `datasets/rrg_rrs/mimic-cxr` and run the provided commands to preprocess the dataset.
