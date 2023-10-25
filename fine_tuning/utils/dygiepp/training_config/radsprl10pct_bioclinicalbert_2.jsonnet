local template = import "custom_template.libsonnet";

template.DyGIE {
  bert_model: "emilyalsentzer/Bio_ClinicalBERT",
  cuda_device: 0,
  data_paths: {
    train: "/PATH_TO//data/RadSpRL/radsprl_dygiepp_train_10pct.jsonl",
    validation: "/PATH_TO//data/RadSpRL/radsprl_dygiepp_dev_10pct.jsonl",
    test: "/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl",
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
      lr: 5e-3
    }
  },
}
