local template = import "custom_template.libsonnet";

template.DyGIE {
  bert_model: "emilyalsentzer/Bio_ClinicalBERT",
  cuda_device: 0,
  data_paths: {
    train: "/PATH_TO//data/radgraph/1.0.0/train_1pct_dygiepp_jsonl.json",
    validation: "/PATH_TO//data/radgraph/1.0.0/dev_1pct_dygiepp_jsonl.json",
    test: "/PATH_TO//data/radgraph/1.0.0/test_CheXpert_dygiepp_jsonl.json",
  },
  loss_weights: {
    ner: 0.2,
    relation: 1.0,
    coref: 0.0,
    events: 0.0
  },
  target_task: "relation",
  trainer +: {
    optimizer +: {
      lr: 1e-4
    }
  },
}
