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

Here's the updated `README.md` content:

---

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

## Usage

### 1. Setup
- **Environment Setup**: Create and activate a conda environment:
  ```bash
  conda create -n rales python=3.8.13
  conda activate rales
  ```
- **Install PyTorch**: Install pytorch 1.12.1 with the appropriate CUDA version. Check [PyTorch's previous versions](https://pytorch.org/get-started/previous-versions/) for compatibility:
  ```bash
  pip install torch==1.12.1+cu113 torchvision==0.13.1+cu113 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu113
  ```
- **Install Additional Dependencies**: Install other required Python packages:
  ```bash
  while read requirement; do conda install --yes $requirement || pip install $requirement; done < requirements.txt
  ```

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

---

You can copy and paste the above content directly into your repository's `README.md` file. Let me know if there's anything else you'd like assistance with!
