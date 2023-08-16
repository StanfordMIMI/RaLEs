Of course! Here's the revised `results/README.md`:

---

## RaLEs Benchmark Results

This directory contains results and utilities related to the RaLEs benchmark.

### Overview

The `results` directory holds the key outcomes and benchmarks of the RaLEs project. Within this directory, the `best_results_files` subdirectory houses the CSV files detailing the best results obtained for various tasks.

### Reproducing Paper Figures

The Jupyter notebook `make_paper_figures.ipynb` allows users to reproduce the figures presented in the RaLEs manuscript. To do this, simply execute the notebook in a Jupyter environment.

### RaLEs Benchmark Leaderboard

An active leaderboard showcasing the performance of various models on the RaLEs tasks is being maintained at [RaLEs Benchmark Leaderboard](https://ralesbenchmark.github.io). This leaderboard is regularly updated with new models and results.

### Submitting to the Leaderboard

Submissions to the RaLEs Benchmark Leaderboard are encouraged and welcomed for any dataset within the benchmark. Whether you've developed models specific to the RadGraph tasks, report summarization, or any other task, we'd love to showcase your results.

#### Submission Process:

1. **Prepare Your Results**: Ensure you have your model's results and metrics ready. At a minimum, provide the metrics reported on the benchmark website for models evaluated on the same task.
2. **Pull Request**: Submit a pull request to this repository with the following details.
3. **Review**: Once submitted, your results will be reviewed and, if approved, will be added to the leaderboard. Requests will be evaluated within 7 business days.

#### Submission Form:

```
- **Name of Model**: [Your Model Name]
- **Pre-training Data**: [Data used for pre-training]
- **Pre-training Strategy**: [Strategy or approach used for pre-training]
- **Fine-tuning Strategy**: [Strategy or approach used for fine-tuning, if any]
- **Link to Paper**: [URL to the related paper or manuscript]
- **Link to Code**: [URL to the public code repository, if available]
- **Link to Model**: [URL to the trained model, if publicly available]
- **Model Version**: [Version or identifier for the model]
- **Dataset(s) Evaluated**: [List of datasets the model was evaluated on]
- **Relevant Metrics**: [Metrics obtained on the above datasets]
- **Number of Parameters**: [Total number of parameters in the model]
- **External Data**: [Any external data sources used for training or fine-tuning]
- **Limitations**: [Known limitations or challenges with the model]
- **Contact Information**: [Email or other contact method for clarifications or collaborations]
- **Additional Information**: [Any other relevant details or notes]
```

