local template = import "custom_template.libsonnet";

template.DyGIE {
  bert_model: "StanfordAIMI/RadBERT",
  cuda_device: 0,
  data_paths: {
    train: "/PATH_TO//data/radgraph/1.0.0/train_dygiepp_jsonl.json",
    validation: "/PATH_TO//data/radgraph/1.0.0/dev_dygiepp_jsonl.json",
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
    checkpointer +:{
      keep_most_recent_by_count: 1,
    },
    optimizer +:{
      type: 'adamw',
      lr: 5e-3,
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
