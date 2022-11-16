## Inference for RaLEs Tasks

This directory provides scripts and utilities to perform inference (predictions) on the RaLEs tasks using trained models.

### Key Files & Descriptions:

1. **inference.py**: used for Stanza NER dataset.
    - Usage: `python inference.py --model_path [path_to_trained_model] --dataset_name [name_of_dataset] --data_split [train_val_test] --output_type [score_or_logits] --output_dir [path_to_inference_results_output_file]`
   
2. **[inference_procedure_2.py]**: used for MIMIC III protocoling dataset.
    - Usage: `python inference.py --model_path [path_to_trained_model] --dataset_name [name_of_dataset] --data_split [train_val_test] --output_type [score_or_logits] --output_dir [path_to_inference_results_output_file]`

3. **scripts** directory containing scripts used to evaluate best trained models for the original RaLEs benchmark.
   
4. **radiologygpt** Script for evaluating RadiologyGPT, see more details in [here](radiologygpt/README.md)

### Step-by-step Guide:

1. **Model Preparation**: Ensure you have a trained model ready for inference. This could be a model you trained using the `fine_tuning` directory or a pre-trained model compatible with the RaLEs tasks.

2. **Data Preparation**: Make sure your input data for inference is in the correct format as expected by the inference scripts. Remember you can find the appropriate data preparation instructions [here](../datasets/README.md).

3. **Perform Inference**: Use the provided scripts as described above to make predictions on your datasets of interest. The scripts will generate outputs (predictions) which can be further processed or analyzed as needed.
