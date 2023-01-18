Contains dataset preprocessing code.

Inputs:
- paths to raw datasets (see ##instructions for downloading raw datasets)

Outputs:
- prepared datasets in RaLEs format

# Data Download Instructions

## RadGraph (NLU)

## RadSpRL (NLU)

## MIMIC procedure selection (NLU)

## Critical abnormality detection (NLU)

## Stanza NER (NLU)

## MEDIQA 2021 (NLG)

## RaLEs Radiology Report Generation (NLG)

#### Reports
You must a physionet account with permissions to download MIMIC-CXR Database. 

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
#### Images
You must a physionet account with permissions to download MIMIC-CXR Database. 
Download images from https://physionet.org/content/mimic-cxr-jpg/2.0.0/ 

The downloaded `files` folder must be stored in a `mimic-cxr-images` folder. 
You are free to resize the images using the following transform:
``` 
transforms.Compose([transforms.Resize(512)])        
```

**Warning: do not use `transforms.Resize(512,512)`**        


# Data Preprocessing Instructions

## RadGraph (NLU)

## RadSpRL (NLU)

## MIMIC procedure selection (NLU)

## Critical abnormality detection (NLU)

## Stanza NER (NLU)

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

