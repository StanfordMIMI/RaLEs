# Overview
This repository contains code and results for RaLEs: Radiology Language Evaluations (manuscript under consideration).

# Contents
The repository is organized in 5 modules, each contained within its own directory: 
| Module  | Purpose |
| ------------- | ------------- |
| datasets  | Provides instructions for RaLEs dataset download and preprocessing  |
| fine_tuning  | Contains command-line interface code for fine-tuning a model for a given RaLEs task  |
| inference | Provides code for performing inference on RaLEs tasks given a pre-trained model |
| evaluation | Provides code for obtaining evaluation metrics based on model predictions for RaLEs tasks |
| results | Includes summary of results of current RaLEs benchmark 

# Install instructions
First create and activate a conda environment:
```
conda create -n rales python=3.8.13
conda activate rales
```

Once created, we recommend first installing pytorch 1.12.1 with your [appropriate cuda version](https://pytorch.org/get-started/previous-versions/) e.g.:
```
pip install torch==1.12.1+cu113 torchvision==0.13.1+cu113 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu113
```

Finally, install additional requirements:
```
while read requirement; do conda install --yes $requirement || pip install $requirement; done < requirements.txt
```

