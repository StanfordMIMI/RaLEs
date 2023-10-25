## RaLEs Datasets

**NOTE**: Users with appropriate Physionet credentials (requires MIMIC-III and MIMIC-CXR DUA agreement) can directly download preprocessed datasets from [Vilmedic Datasets](https://vilmedic.app/datasets/text).

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

#### 1. MEDIQA 2021 CXR Report Summarization
- **Download**: Follow the instructions for dataset download on [GitHub](https://github.com/abachaa/MEDIQA2021/tree/main/Task3).

#### 2. BioNLP 2023 Radiology Report Summarization
- **Download**: You must create a Physionet account with permissions to download the MIMIC-CXR Database. Get the `mimic-cxr-reports.zip` and related files from [Physionet](https://physionet.org/content/mimic-cxr/2.0.0/mimic-cxr-reports.zip) and organize them as mentioned.
- **Preprocessing**: Navigate to `datasets/rrg_rrs/mimic-cxr` and run the provided commands to preprocess the dataset.


## Adding a Dataset to the RaLEs Benchmark

We encourage the community to contribute and expand the RaLEs benchmark by adding new datasets. If you have a dataset that can be valuable for radiology language tasks, please follow the instructions below:

### Submission Process:

1. **Prepare Your Dataset Details**: Ensure you have all the details about your dataset ready as per the guidelines below.
2. **Pull Request**: Submit a pull request to this repository with the dataset details.
3. **Review**: Your dataset will be reviewed based on the provided information. The review process typically takes up to 10 business days. If your dataset is accepted, it will be added to the RaLEs benchmark.

### Dataset Details Guidelines:

- **Name**: The official name of the dataset.
- **Description**: A brief description of the dataset.
- **Task**: Specify the NLP task (e.g., NLU, NLG, Classification, Relation Extraction, Summarization, etc.).
- **Clinical/Scientific Relevance**: Explain the clinical or scientific relevance of the dataset.
- **Format**: Describe the format of the dataset (e.g., CSV, JSON, etc.).
- **Size**: Provide the size details such as the number of patients, reports, and images.
- **Download Instructions**: Step-by-step instructions or links for downloading the dataset.
- **Preparation Scripts**: If applicable, provide scripts or instructions for preprocessing or preparing the dataset.
- **Labeling Method**: Explain how the dataset was labeled (e.g., manual annotation, expert-reviewed, etc.).
- **Models Evaluated**: List the models that have been evaluated on the dataset and their performance metrics.
- **Preferred Metric**: Specify the main metric that should be used for evaluating models on this dataset.
- **Additional Relevant Metrics**: Mention any other metrics that can be used for evaluation.
- **Potential Biases**: Discuss any known biases in the dataset.
- **Related Existing Datasets**: If applicable, mention any datasets that are related or similar to yours.

### Important Note:

If your dataset addresses a task already present in the RaLEs benchmark, you should benchmark the best performing RaLEs models for that task. For example, if your dataset is for procedure selection, you should evaluate it using the best performing RaLEs procedure selection model.

### Pull Request Template:

```markdown
## Dataset Submission for RaLEs Benchmark

- **Name**: [Your Dataset Name]
- **Description**: [Brief Description]
- **Task**: [NLP Task]
- **Clinical/Scientific Relevance**: [Relevance Explanation]
- **Format**: [Dataset Format]
- **Size**: 
  - **Patients**: [Number]
  - **Reports**: [Number]
  - **Images**: [Number]
- **Download Instructions**: [Instructions or Links]
- **Preparation Scripts**: [Scripts or Instructions]
- **Labeling Method**: [Method Description]
- **Models Evaluated**: [Models and Performance Metrics]
- **Preferred Metric**: [Metric Name]
- **Additional Relevant Metrics**: [Other Metrics]
- **Potential Biases**: [Known Biases]
- **Related Existing Datasets**: [Related Datasets]

[Any additional information or notes]
```
