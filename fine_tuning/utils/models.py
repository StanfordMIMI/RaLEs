from transformers import AutoModel

class AutoPLMarkerModelForRE(AutoModel):
    """
    adapted from https://github.com/thunlp/PL-Marker/blob/9eb7b09ed3ce1e06764559c054c3fd76f74aeabe/transformers/src/transformers/modeling_bert.py
    (class BertForACEBothOneDropoutSub) 
    """
    def __init__(self, config, base_name):
        super().__init__(config)
        self.max_seq_length = config.max_seq_length
        self.num_labels = config.num_labels
        self.num_ner_labels = config.num_ner_labels

        self.base = AutoModel.from_pretrained(base_name)
        self.dropout = nn.Dropout(config.hidden_dropout_prob)

        self.ner_classifier = nn.Linear(config.hidden_size*2, self.num_ner_labels)

        self.re_classifier_m1 = nn.Linear(config.hidden_size*2, self.num_labels)
        self.re_classifier_m2 = nn.Linear(config.hidden_size*2, self.num_labels)

        self.alpha = torch.tensor([config.alpha] + [1.0] * (self.num_labels-1), dtype=torch.float32)

        self.init_weights()

    def forward(
        self,
        input_ids=None,
        attention_mask=None,
        mentions=None,
        token_type_ids=None,
        position_ids=None,
        head_mask=None,
        inputs_embeds=None,
        sub_positions=None,
        labels=None,
        ner_labels=None,
    ):
        
        outputs = self.base(
            input_ids,
            attention_mask=attention_mask,
            token_type_ids=token_type_ids,
            position_ids=position_ids,
            head_mask=head_mask,
            inputs_embeds=inputs_embeds,
        )
        hidden_states = outputs[0]
        hidden_states = self.dropout(hidden_states)
        seq_len = self.max_seq_length
        bsz, tot_seq_len = input_ids.shape
        ent_len = (tot_seq_len-seq_len) // 2

        e1_hidden_states = hidden_states[:, seq_len:seq_len+ent_len]
        e2_hidden_states = hidden_states[:, seq_len+ent_len: ]

        feature_vector = torch.cat([e1_hidden_states, e2_hidden_states], dim=2)

        ner_prediction_scores = self.ner_classifier(feature_vector)


        m1_start_states = hidden_states[torch.arange(bsz), sub_positions[:, 0]]
        m1_end_states = hidden_states[torch.arange(bsz), sub_positions[:, 1]]
        m1_states = torch.cat([m1_start_states, m1_end_states], dim=-1)

        m1_scores = self.re_classifier_m1(m1_states)  # bsz, num_label
        m2_scores = self.re_classifier_m2(feature_vector) # bsz, ent_len, num_label
        re_prediction_scores = m1_scores.unsqueeze(1) + m2_scores

        outputs = (re_prediction_scores, ner_prediction_scores) + outputs[2:]  # Add hidden states and attention if they are here

        if labels is not None:
            loss_fct_re = CrossEntropyLoss(ignore_index=-1,  weight=self.alpha.to(re_prediction_scores))
            loss_fct_ner = CrossEntropyLoss(ignore_index=-1)
            re_loss = loss_fct_re(re_prediction_scores.view(-1, self.num_labels), labels.view(-1))
            ner_loss = loss_fct_ner(ner_prediction_scores.view(-1, self.num_ner_labels), ner_labels.view(-1))

            loss = re_loss + ner_loss
            outputs = (loss, re_loss, ner_loss) + outputs

        return outputs  # (masked_lm_loss), prediction_scores, (hidden_states), (attentions)