# Overview
This repository contains code and results for RaLEs: Radiology Language Evaluations (manuscript under consideration). [Check out the leaderboard](https://ralesbenchmark.github.io)!

# Contents
The repository is organized in 5 modules, each contained within its own directory: 
| Module  | Purpose |
| ------------- | ------------- |
| [datasets](datasets)  | Provides instructions for RaLEs dataset download and preprocessing  |
| [fine_tuning](fine_tuning)  | Contains command-line interface code for fine-tuning a model for a given RaLEs task  |
| [inference](inference) | Provides code for performing inference on RaLEs tasks given a pre-trained model |
| [evaluation](evaluation) | Provides code for obtaining evaluation metrics based on model predictions for RaLEs tasks |
| [results](results) | Includes summary of results of current RaLEs benchmark 

## Usage

### 1. Install instructions

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

**Note:** RaLEs has been developed and tested using Ubuntu 22.04.3

### 2. Data Preparation
Navigate to the `datasets` directory and follow the instructions in the [datasets README](datasets/README.md) for downloading and preprocessing the RaLEs datasets.

### 3. Training
To fine-tune a model for a specific RaLEs task, navigate to the `fine_tuning` directory and use the command-line interface detailed in the [fine_tuning README](fine_tuning/README.md).

### 4. Inference
After training, you can perform inference on the RaLEs tasks using the pre-trained model. Go to the `inference` directory and refer to the [inference README](inference/README.md) for detailed instructions.

### 5. Evaluation
Evaluate the performance of your model using the scripts in the `evaluation` directory. More details can be found in the [evaluation README](evaluation/README.md).

### 6. Results
Check the `results` directory for a summary of benchmark results for the RaLEs tasks. The [results README](results/README.md) provides further insights.

For the current leaderboard, visit [RaLEs Benchmark Leaderboard](https://ralesbenchmark.github.io).

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
  
  New dataset submissions are more than welcome. Full instructions for how to format and submit a dataset can be found in the [datasets directory](datasets/README.md#adding-a-dataset-to-the-rales-benchmark). 
  
</details>


<details>
  <summary>5. I have a suggestion for a new feature, how can I share it?</summary>
  
  Please use the issues tab in github. Be sure to be specific about what you'd like to see implemented. If you'd like to implement it yourself, you can submit a pull request with the feature implementation, and a brief rationale motivating it. Thank you for your contributions! 
  
</details>

## Bibtex
```
@inproceedings{zambranochaves2023rales,
  author    = {Zambrano Chaves, Juan Manuel and Bhaskhar, Nandita and Attias, Maayane and Delbrouck, Jean-Benoit and Rubin, Daniel and Loening, Andreas Markus and Langlotz, Curtis and Chaudhari, Akshay S},
  title     = {RaLEs: a Benchmark for Radiology Language Evaluations},
  booktitle = {Advances in Neural Information Processing Systems},
  volume = {36},
  year = {2023}
}
```

