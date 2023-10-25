local template = import "custom_template.libsonnet";

template.DyGIE {
  bert_model: "emilyalsentzer/Bio_ClinicalBERT",
  cuda_device: 0,
  data_paths: {
    train: "/PATH_TO//data/RadSpRL/radsprl_dygiepp_train.jsonl",
    validation: "/PATH_TO//data/RadSpRL/radsprl_dygiepp_dev.jsonl",
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
    checkpointer +:{
      keep_most_recent_by_count: 1,
    },
    optimizer +:{
      type: 'adamw',
      lr: 1e-3,
      weight_decay:0.0,
      parameter_groups: [
          [
            ['_embedder'],
            {
              requires_grad: false,
            },
          ],
        ],
    }
  },
}
