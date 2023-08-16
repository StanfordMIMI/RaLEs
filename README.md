# Overview
This repository contains code and results for RaLEs: Radiology Language Evaluations (manuscript under consideration).

# Contents
The repository is organized in 5 modules, each contained within its own directory: 
| Module  | Purpose |
| ------------- | ------------- |
| [datasets](datasets)  | Provides instructions for RaLEs dataset download and preprocessing  |
| [fine_tuning](fine_tuning)  | Contains command-line interface code for fine-tuning a model for a given RaLEs task  |
| [inference](inference) | Provides code for performing inference on RaLEs tasks given a pre-trained model |
| [evaluation](evaluation) | Provides code for obtaining evaluation metrics based on model predictions for RaLEs tasks |
| [results](results) | Includes summary of results of current RaLEs benchmark 

# Install instructions
First create and activate a conda environment:
```
conda create -n rales python=3.8.13
conda activate rales
```

Once created, we recommend first installing pytorch with your [appropriate cuda version](https://pytorch.org/get-started/previous-versions/) e.g.:
```
pip install torch torchvision torchaudio 
```

Finally, install additional requirements:
```
while read requirement; do conda install --yes $requirement || pip install $requirement; done < requirements.txt
```

# FAQs
Yes, you can create a FAQs section with collapsible dropdowns using GitHub-flavored Markdown combined with a bit of HTML. 

Here's an example of how you can structure a FAQs section with collapsible dropdowns:

---

## Frequently Asked Questions (FAQs)

<details>
  <summary>1. What is the purpose of the RaLEs benchmark?</summary>
  
  The RaLEs benchmark is designed to evaluate models on various radiology language tasks. It provides a standardized dataset and evaluation metrics to compare the performance of different models in a consistent manner.
  
</details>

<details>
  <summary>2. How can I submit my model to the leaderboard?</summary>
  
  To submit your model to the leaderboard, follow the submission process detailed in the [results README](results/README.md). Ensure you provide all the required details in the submission form.
  
</details>

<details>
  <summary>3. Where can I find the datasets used in the benchmark?</summary>
  
  The datasets can be accessed from the [datasets directory](datasets/README.md). Detailed instructions on downloading and preprocessing each dataset are provided there.
  
</details>

<details>
  <summary>4. I'd like to contribute a dataset, how can I do that?</summary>
  
  New dataset submissions are more than welcome. Full instructions for how to format and submit a dataset can be found in the [datasets directory](datasets/README.md). 
  
</details>
