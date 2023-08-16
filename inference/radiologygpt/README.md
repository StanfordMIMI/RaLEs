# Inference for RadiologyGPT model
This folder implements [RadiologyGPT](https://arxiv.org/pdf/2306.08666.pdf) inference. 

Note that RadiologyGPT was developed to support radiology report summarization. Further, it was trained using the MIMIC-CXR dataset.


## Instructions

Run the following command to run inference on MEDIQA 2021:

```bash
    python eval_radiologygpt.py \
        --data_file /PATH_TO/mediqa2021_test.jsonl \
        --output_dir /PATH_TO/OUTPUT_DIR
```
