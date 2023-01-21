Contains dataset preprocessing code.

Inputs:
- paths to raw datasets (see ##instructions for downloading raw datasets)

Outputs:
- prepared datasets in RaLEs format

# Data Download Instructions

## RadGraph (NLU)
Access the dataset at https://physionet.org/content/radgraph/1.0.0/.

## RadSpRL (NLU)
Download the Rad-SpRL.xml file from https://data.mendeley.com/datasets/yhb26hfz8n.

## MIMIC procedure selection (NLU)
Access the MIMIC-III dataset at https://physionet.org/content/mimiciii/1.4/.

## Stanza NER (NLU)
A link for access to this dataset will be provided upon institutional review board approval.

## MEDIQA 2021 (NLG)
Follow the instructions for dataset download here https://github.com/abachaa/MEDIQA2021/tree/main/Task3.

## RaLEs Radiology Report Generation (NLG)

#### Reports
You must a create a physionet account with permissions to download MIMIC-CXR Database. 

Download `mimic-cxr-reports.zip` from https://physionet.org/content/mimic-cxr/2.0.0/mimic-cxr-reports.zip.
Place the extracted `mimic-cxr-reports` folder in the `datasets/rrg_rrs/mimic-cxr` folder. 

Download `mimic-cxr-2.0.0-split.csv.gz` and `mimic-cxr-2.0.0-metadata.csv.gz` from https://physionet.org/content/mimic-cxr-jpg/2.0.0/. Place the 
extracted files in the `datasets/rrg_rrs/mimic-cxr` folder.

``` 
datasets/rrg_rrs/mimic-cxr
├── mimic-cxr-reports
│   └── files
│       ├── p10
│       ├── p11
│       ├── p12
│       ├── p13
│       ├── p14
│       ├── p15
│       ├── p16
│       ├── p17
│       ├── p18
│       └── p19
├── create_section_files.py
├── make_mimic_cxr.py
├── get_chexbert_label.py
├── section_parser.py
├── mimic-cxr-2.0.0-split.csv
├── mimic-cxr-2.0.0-metadata.csv
└── README.md
```

# Data Preprocessing Instructions

## RadGraph (NLU)
Run the `convert_radgraph_to_dygiepp.py` in this folder, specifying the location where the RadGraph dataset is saved.

## RadSpRL (NLU)
Run the `convert_radsprl_to_dygiepp.py` script in this folder, specifying the location where the RadSpRL dataset is saved.

## MIMIC procedure selection (NLU)
Run the `create_dataset.py` followed by the `create_train_dev_test_split.py` scripts in the `mimiciii_procedure_selection` folder, specifying the location where the MIMIC dataset is saved.

## Stanza NER (NLU)
The dataset will be provided without requiring further preprocessing.

## MEDIQA 2021 (NLG)

## RaLEs Radiology Report Generation (NLG)

Go to `datasets/rrg_rrs/mimic-cxr` folder, then run the command:

```
python create_section_files.py --no_split --reports_path ./mimic-cxr-reports/files --output_path ./ 
```

Then:

```
python make_mimic_cxr.py --task rrg
```
The output will be in the current directory in RRG folder.

