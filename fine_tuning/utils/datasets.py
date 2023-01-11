"""
Implements RadGraph and RadSpRL datasets for relationship extraction based on PLMarker implementation
(https://github.com/thunlp/PL-Marker/blob/07fde08d868134ced1d861d17d263d6c782bb420/run_re.py; class ACEDataset)
"""

from torch.utils.data import Dataset

class RadGraphREDataset(Dataset):
    def __init__(self, tokenizer, args=None, evaluate=False, do_test=False, max_pair_length=None):

        if not evaluate:
            file_path = os.path.join(args.data_dir, args.train_file)
        else:
            if do_test:
                if args.test_file.find('models')==-1:
                    file_path = os.path.join(args.data_dir, args.test_file)
                else:
                    file_path = args.test_file
            else:
                if args.dev_file.find('models')==-1:
                    file_path = os.path.join(args.data_dir, args.dev_file)
                else:
                    file_path = args.dev_file

        assert os.path.isfile(file_path)

        self.file_path = file_path
                
        self.tokenizer = tokenizer
        self.max_seq_length = args.max_seq_length
        self.max_pair_length = max_pair_length
        self.max_entity_length = self.max_pair_length*2

        self.evaluate = evaluate
        self.use_typemarker = args.use_typemarker
        self.local_rank = args.local_rank
        self.args = args
        self.model_type = args.model_type
        self.no_sym = args.no_sym
        self.ner_label_list = ['ANAT-DP','OBS-DA','OBS-DP','OBS-U']
        relationship_label_list = ['located_at','suggestive_of','modify']
        self.sym_labels = ['NIL']
        self.label_list = self.sym_labels + relationship_label_list
        self.global_predicted_ners = {}
        self.initialize()
 
    def initialize(self):
        tokenizer = self.tokenizer
        vocab_size = tokenizer.vocab_size
        max_num_subwords = self.max_seq_length - 4  # for two markers
        label_map = {label: i for i, label in enumerate(self.label_list)}
        ner_label_map = {label: i for i, label in enumerate(self.ner_label_list)}

        def tokenize_word(text):
            if (
                isinstance(tokenizer, RobertaTokenizer)
                and (text[0] != "'")
                and (len(text) != 1 or not self.is_punctuation(text))
            ):
                return tokenizer.tokenize(text, add_prefix_space=True)
            return tokenizer.tokenize(text)

        f = open(self.file_path, "r", encoding='utf-8')
        self.ner_tot_recall = 0
        self.tot_recall = 0
        self.data = []
        self.ner_golden_labels = set([])
        self.golden_labels = set([])
        self.golden_labels_withner = set([])
        maxR = 0
        maxL = 0
        for l_idx, line in enumerate(f):
            data = json.loads(line)

            if self.args.output_dir.find('test')!=-1:
                if len(self.data) > 100:
                    break

            sentences = data['sentences']
            if 'predicted_ner' in data:       # e2e predict
               ners = data['predicted_ner']               
            else:
               ners = data['ner']

            std_ners = data['ner']

            relations = data['relations']

            for sentence_relation in relations:
                for x in sentence_relation:
                    if x[4] in self.sym_labels[1:]:
                        self.tot_recall += 2
                    else: 
                        self.tot_recall +=  1

            sentence_boundaries = [0]
            words = []
            L = 0
            for i in range(len(sentences)):
                L += len(sentences[i])
                sentence_boundaries.append(L)
                words += sentences[i]

            tokens = [tokenize_word(w) for w in words]
            subwords = [w for li in tokens for w in li]
            maxL = max(maxL, len(subwords))
            subword2token = list(itertools.chain(*[[i] * len(li) for i, li in enumerate(tokens)]))
            token2subword = [0] + list(itertools.accumulate(len(li) for li in tokens))
            subword_start_positions = frozenset(token2subword)
            subword_sentence_boundaries = [sum(len(li) for li in tokens[:p]) for p in sentence_boundaries]

            for n in range(len(subword_sentence_boundaries) - 1):

                sentence_ners = ners[n]
                sentence_relations = relations[n]
                std_ner = std_ners[n]

                std_entity_labels = {}
                self.ner_tot_recall += len(std_ner)

                for start, end, label in std_ner:
                    std_entity_labels[(start, end)] = label
                    self.ner_golden_labels.add( ((l_idx, n), (start, end), label) )

                self.global_predicted_ners[(l_idx, n)] = list(sentence_ners)

                doc_sent_start, doc_sent_end = subword_sentence_boundaries[n : n + 2]

                left_length = doc_sent_start
                right_length = len(subwords) - doc_sent_end
                sentence_length = doc_sent_end - doc_sent_start
                half_context_length = int((max_num_subwords - sentence_length) / 2)

                if sentence_length < max_num_subwords:

                    if left_length < right_length:
                        left_context_length = min(left_length, half_context_length)
                        right_context_length = min(right_length, max_num_subwords - left_context_length - sentence_length)
                    else:
                        right_context_length = min(right_length, half_context_length)
                        left_context_length = min(left_length, max_num_subwords - right_context_length - sentence_length)


                doc_offset = doc_sent_start - left_context_length
                target_tokens = subwords[doc_offset : doc_sent_end + right_context_length]
                target_tokens = [tokenizer.cls_token] + target_tokens[ : self.max_seq_length - 4] + [tokenizer.sep_token] 
                assert(len(target_tokens) <= self.max_seq_length - 2)
                
                pos2label = {}
                for x in sentence_relations:
                    pos2label[(x[0],x[1],x[2],x[3])] = label_map[x[4]]
                    self.golden_labels.add(((l_idx, n), (x[0],x[1]), (x[2],x[3]), x[4]))
                    self.golden_labels_withner.add(((l_idx, n), (x[0],x[1], std_entity_labels[(x[0], x[1])]), (x[2],x[3], std_entity_labels[(x[2], x[3])]), x[4]))
                    if x[4] in self.sym_labels[1:]:
                        self.golden_labels.add(((l_idx, n),  (x[2],x[3]), (x[0],x[1]), x[4]))
                        self.golden_labels_withner.add(((l_idx, n), (x[2],x[3], std_entity_labels[(x[2], x[3])]), (x[0],x[1], std_entity_labels[(x[0], x[1])]), x[4]))

                entities = list(sentence_ners)

                for x in sentence_relations:
                    w = (x[2],x[3],x[0],x[1])
                    if w not in pos2label:
                        if x[4] in self.sym_labels[1:]:
                            pos2label[w] = label_map[x[4]]  # bug
                        else:
                            pos2label[w] = label_map[x[4]] + len(label_map) - len(self.sym_labels)

                if not self.evaluate:
                    entities.append((10000, 10000, 'NIL')) # only for NER

                for sub in entities:    
                    cur_ins = []

                    if sub[0] < 10000:
                        sub_s = token2subword[sub[0]] - doc_offset + 1
                        sub_e = token2subword[sub[1]+1] - doc_offset
                        sub_label = ner_label_map[sub[2]]

                        if self.use_typemarker:
                            l_m = '[unused%d]' % ( 2 + sub_label )
                            r_m = '[unused%d]' % ( 2 + sub_label + len(self.ner_label_list) )
                        else:
                            l_m = '[unused0]'
                            r_m = '[unused1]'
                        
                        sub_tokens = target_tokens[:sub_s] + [l_m] + target_tokens[sub_s:sub_e+1] + [r_m] + target_tokens[sub_e+1: ]
                        sub_e += 2
                    else:
                        sub_s = len(target_tokens)
                        sub_e = len(target_tokens)+1
                        sub_tokens = target_tokens + ['[unused0]',  '[unused1]']
                        sub_label = -1

                    if sub_e >= self.max_seq_length-1:
                        continue
                    # assert(sub_e < self.max_seq_length)
                    for start, end, obj_label in sentence_ners:
                        if self.model_type.endswith('nersub'):
                            if start==sub[0] and end==sub[1]:
                                continue

                        doc_entity_start = token2subword[start]
                        doc_entity_end = token2subword[end+1]
                        left = doc_entity_start - doc_offset + 1
                        right = doc_entity_end - doc_offset

                        obj = (start, end)
                        if obj[0] >= sub[0]:
                            left += 1
                            if obj[0] > sub[1]:
                                left += 1

                        if obj[1] >= sub[0]:   
                            right += 1
                            if obj[1] > sub[1]:
                                right += 1
    
                        label = pos2label.get((sub[0], sub[1], obj[0], obj[1]), 0)

                        if right >= self.max_seq_length-1:
                            continue

                        cur_ins.append(((left, right, ner_label_map[obj_label]), label, obj))


                    maxR = max(maxR, len(cur_ins))
                    dL = self.max_pair_length
                    if self.args.shuffle:
                        np.random.shuffle(cur_ins)

                    for i in range(0, len(cur_ins), dL):
                        examples = cur_ins[i : i + dL]
                        item = {
                            'index': (l_idx, n),
                            'sentence': sub_tokens,
                            'examples': examples,
                            'sub': (sub, (sub_s, sub_e), sub_label), #(sub[0], sub[1], sub_label),
                        }                
                        
                        self.data.append(item)                    
        logger.info('maxR: %s', maxR)
        logger.info('maxL: %s', maxL)
                
    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        entry = self.data[idx]
        sub, sub_position, sub_label = entry['sub']
        input_ids = self.tokenizer.convert_tokens_to_ids(entry['sentence'])

        L = len(input_ids)
        input_ids += [self.tokenizer.pad_token_id] * (self.max_seq_length - len(input_ids))

        attention_mask = torch.zeros((self.max_entity_length+self.max_seq_length, self.max_entity_length+self.max_seq_length), dtype=torch.int64)
        attention_mask[:L, :L] = 1
        
        if self.model_type.startswith('albert'):
            input_ids = input_ids + [30002] * (len(entry['examples'])) + [self.tokenizer.pad_token_id] * (self.max_pair_length - len(entry['examples']))
            input_ids = input_ids + [30003] * (len(entry['examples'])) + [self.tokenizer.pad_token_id] * (self.max_pair_length - len(entry['examples'])) # for debug
        else:
            input_ids = input_ids + [3] * (len(entry['examples'])) + [self.tokenizer.pad_token_id] * (self.max_pair_length - len(entry['examples']))
            input_ids = input_ids + [4] * (len(entry['examples'])) + [self.tokenizer.pad_token_id] * (self.max_pair_length - len(entry['examples'])) # for debug

        labels = []
        ner_labels = []
        mention_pos = []
        mention_2 = []
        position_ids = list(range(self.max_seq_length)) + [0] * self.max_entity_length 
        num_pair = self.max_pair_length

        for x_idx, obj in enumerate(entry['examples']):
            m2 = obj[0]
            label = obj[1]

            mention_pos.append((m2[0], m2[1]))
            mention_2.append(obj[2])

            w1 = x_idx  
            w2 = w1 + num_pair

            w1 += self.max_seq_length
            w2 += self.max_seq_length
            
            position_ids[w1] = m2[0]
            position_ids[w2] = m2[1]

            for xx in [w1, w2]:
                for yy in [w1, w2]:
                    attention_mask[xx, yy] = 1
                attention_mask[xx, :L] = 1

            labels.append(label)
            ner_labels.append(m2[2])

            if self.use_typemarker:
                l_m = '[unused%d]' % ( 2 + m2[2] + len(self.ner_label_list)*2 )
                r_m = '[unused%d]' % ( 2 + m2[2] + len(self.ner_label_list)*3 )
                l_m = self.tokenizer._convert_token_to_id(l_m)
                r_m = self.tokenizer._convert_token_to_id(r_m)
                input_ids[w1] = l_m
                input_ids[w2] = r_m


        pair_L = len(entry['examples'])
        if self.args.att_left:
            attention_mask[self.max_seq_length : self.max_seq_length+pair_L, self.max_seq_length : self.max_seq_length+pair_L] = 1
        if self.args.att_right:
            attention_mask[self.max_seq_length+num_pair : self.max_seq_length+num_pair+pair_L, self.max_seq_length+num_pair : self.max_seq_length+num_pair+pair_L] = 1

        mention_pos += [(0, 0)] * (num_pair - len(mention_pos))
        labels += [-1] * (num_pair - len(labels))
        ner_labels += [-1] * (num_pair - len(ner_labels))

        item = [torch.tensor(input_ids),
                attention_mask,
                torch.tensor(position_ids),
                torch.tensor(sub_position),
                torch.tensor(mention_pos),
                torch.tensor(labels, dtype=torch.int64),
                torch.tensor(ner_labels, dtype=torch.int64),
                torch.tensor(sub_label, dtype=torch.int64)
        ]

        if self.evaluate:
            item.append(entry['index'])
            item.append(sub)
            item.append(mention_2)

        return item

    @staticmethod
    def collate_fn(batch):
        fields = [x for x in zip(*batch)]

        num_metadata_fields = 3
        stacked_fields = [torch.stack(field) for field in fields[:-num_metadata_fields]]  # don't stack metadata fields
        stacked_fields.extend(fields[-num_metadata_fields:])  # add them as lists not torch tensors

        return stacked_fields