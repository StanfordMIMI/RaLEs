"""
Convert Radgraph Dataset into format for transformers run_NER.py

Currently using NER tags only
"""

import json

def parse_file(fpath):
    with open(fpath, 'r') as fin:
        contents = json.load(fin)

    data = []
    for dataset in contents.values():
        if 'entities' in dataset: #train, dev
            parsed_dataset = convert_dict_to_small_dict(dataset)
            data.append(parsed_dataset)
        else: #test
            parsed_datasets = convert_dict_to_two_small_dicts(dataset)
            data.append(parsed_datasets[0])
            data.append(parsed_datasets[1])
    return data

def convert_dict_to_small_dict(orig_dict):
    """
    Creates dict output from a *.json dictionary format from RadGraph with two lists, 
    corresponding to words and labels
    """

    concept2label = {x['tokens']:x['label'] for x in orig_dict['entities'].values()}

    text = orig_dict['text']
    tokens = text.split(' ')
    labels = ['O']*len(tokens)
   
    NER = []
    for token in tokens:
        if token in concept2label:
            NER.append(concept2label[token])
        else:
            NER.append('O')
        
    return {'words':tokens, 'ner':NER}

def convert_dict_to_two_small_dicts(dataset):
    """
    Creates list output containing two dicts (one for each labeler), includes dataset_source too
    """
    dicts = []
    for labeler in ['labeler_1','labeler_2']:
        new_dict = {}
        new_dict['text'] = dataset['text']
        new_dict['entities'] = dataset[labeler]['entities']
        parsed = convert_dict_to_small_dict(new_dict) 
        parsed['data_source'] = dataset['data_source']
        dicts.append(parsed)
    return dicts

def write_jsonl(json_dataset, fpath):
    with open(fpath, 'w') as fout:
        for data in json_dataset:
            json.dump(data, fout)
            fout.write('\n')

def main():
    radgraph_dir = '/DEIDPATH/data/radgraph/1.0.0/'
    for fname in ['train','dev','test']:
        parsed_contents = parse_file(f'{radgraph_dir}{fname}.json')
        if fname != 'test':
            write_jsonl(parsed_contents, f'{radgraph_dir}{fname}_jsonl.json')
        else:
            for data_source in ['MIMIC-CXR','CheXpert']:
                relevant_contents = []
                for c in parsed_contents:
                    if c['data_source'] == data_source:
                        relevant_contents.append(c)
                write_jsonl(relevant_contents, f'{radgraph_dir}{fname}_{data_source}_jsonl.json')

if __name__=='__main__':
    main()