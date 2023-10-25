local template = import "custom_template.libsonnet";

template.DyGIE {
  bert_model: "google/electra-large-discriminator",
  cuda_device: 0,
  data_paths: {
    train: "/PATH_TO//data/RadSpRL/radsprl_dygiepp_train.jsonl",
    validation: "/PATH_TO//data/RadSpRL/radsprl_dygiepp_dev.jsonl",
    test: "/PATH_TO//data/RadSpRL/radsprl_dygiepp_test.jsonl",
  },
  loss_weights: {
    ner: 2.0,
    relation: 1.0,
    coref: 0.0,
    events: 0.0
  },
  target_task: "relation",
  trainer +: {
    optimizer +: {
      lr: 1e-3,
      weight_decay:1,
      parameter_groups: [
          [
            ['_embedder'],
            {
              lr: 5e-5,
              weight_decay: 1,
              finetune: true,
            },
          ],
        ],
    }
  },
}
