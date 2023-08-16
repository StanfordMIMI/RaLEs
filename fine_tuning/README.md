## Fine-tuning Models for RaLEs Tasks

This directory contains code and utilities for fine-tuning models on the RaLEs datasets using pre-trained models from the HuggingFace model zoo.

### Key Files & Descriptions:

1. **cli.py**: The primary command-line interface for fine-tuning models. 
    - Usage: `python cli.py --config [path_to_config.yaml]`
   
2. **constants.py**: Contains various constants and configurations used across the fine-tuning scripts.

3. **find_best_models.py**: Script to identify and select the best performing models after training.
    - Usage: `python find_best_models.py [additional_arguments]`

6. **configs**: A directory containing configuration files for different models and tasks. Provided are configurations used to evaluate models for RaLEs. Ensure you select the appropriate configuration for your task and model.

7. **utils**: A directory with utility functions and scripts to assist in the fine-tuning process.

### Step-by-step Guide:

1. **Prepare Data**: Make sure you've preprocessed the data (see instructions in the [datasets directory](../datasets/README.md)).
2. Update **constants.py** file with appropriate path to datasets.
3. **Fine-tuning**: Use `cli.py` to initiate the fine-tuning process. Specify the path to a config YAML file.
4. Next, use your model for [inference](../inference/README.md).
