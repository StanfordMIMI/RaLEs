## Evaluation Scripts for the RaLEs Benchmark

### Evaluation Scripts Usage

#### 1) NLU Metrics:

- **Evaluating MIMIC III Procedure Models**:
  - Script: `evaluate_procedure_models.py`
  - Arguments:
    - `--predictions_fpath`: Path to the predictions file.
    - `--dataset_name`: Name of the dataset being used.
    - `--data_split`: Data split (e.g., 'train', 'test').
    - `--bootstrap`: (Optional) Use bootstrapping for evaluations.
  - Example Usage:
    ```
    python evaluate_procedure_models.py --predictions_fpath path_to_predictions --dataset_name dataset_name --data_split test
    ```

- **Evaluating Stanza Models**:
  - Script: `evaluate_stanza_models.py`
  - Arguments:
    - `--predictions_fpath`: Path to the predictions file.
    - `--dataset_name`: Name of the dataset being used.
    - `--data_split`: Data split (e.g., 'train', 'test').
    - `--output_path`: Path to save the output.
    - `--bootstrap`: (Optional) Use bootstrapping for evaluations.
  - Example Usage:
    ```
    python evaluate_stanza_models.py --predictions_fpath path_to_predictions --dataset_name dataset_name --data_split test --output_path path_to_output
    ```

- **Complementary Metrics**:
  - Script: `complementary_metrics.py`
  - This script evaluates a set of additional metrics, which include SCE, MCE, ECE, NegLogLikelihood, and AccuracyAtK.

#### 2) NLG Metrics:

- **Report Generation Evaluator**:
  - Script: `report_generation_evaluator.py`
  - Arguments:
    - `--generations_filepath`: Path to the generated reports.
    - `--reference_filepath`: Path to the reference reports.
    - `--scorers`: List of scorers to use for evaluation.
  - Example Usage:
    ```
    python report_generation_evaluator.py --generations_filepath path_to_generations --reference_filepath path_to_references --scorers scorer1,scorer2
    ```

### Metric Descriptions

#### NLU Metrics:
- **SCE, MCE, ECE**: Calibration errors that measure the reliability of model predictions.
- **NegLogLikelihood**: Measures the log likelihood of the predicted probabilities. Lower values indicate better performance.
- **AccuracyAtK**: Checks if the true label is within the top K predicted labels.

#### NLG Metrics:
- **BLEU, ROUGE, F1radgraph, F1ChexBert, BERTscore**: Metrics used to evaluate the quality of machine-generated translations or summaries.

For detailed descriptions and usage of each metric, please refer to the RaLEs manuscript.