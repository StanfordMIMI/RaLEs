"""
Converts RadGraph dataset to dygiepp 

Radgraph dataset:
https://physionet.org/content/radgraph/1.0.0/

dygiepp format:
https://github.com/dwadden/dygiepp/blob/4420bf990cc9f7bcba38dde5861d62727d0109ab/doc/data.md

Used for relationship extraction task
"""

import json 

from convert_radgraph_to_json import write_jsonl

def parse_file(fpath):
    with open(fpath, 'r') as fin:
        contents = json.load(fin)
    data = []
    for ID, dataset in contents.items():
        if 'entities' in dataset: #train, dev
            parsed_dataset = convert_dict_to_plmarker(dataset, two_labelers=False)
            parsed_dataset['doc_key'] = ID
            parsed_dataset['dataset'] = 'radgraph'
            data.append(parsed_dataset)
        else: #test, two labelers, treated independently
            parsed_datasets = convert_dict_to_plmarker(dataset, two_labelers=True)
            parsed_datasets[0]['doc_key'] = ID + '_labeler_1'
            parsed_datasets[0]['dataset'] = 'radgraph'
            parsed_datasets[1]['doc_key'] = ID + '_labeler_2'
            parsed_datasets[1]['dataset'] = 'radgraph'
            data.append(parsed_datasets[0])
            data.append(parsed_datasets[1])
    return data

def convert_dict_to_plmarker(radgraph_dataset, two_labelers, save_source=False):
    """
    
    """
    if two_labelers:
        labeler1 = radgraph_dataset['labeler_1']
        labeler2 = radgraph_dataset['labeler_2']
        labeler1['text'] = radgraph_dataset['text']
        labeler2['text'] = radgraph_dataset['text']
        return [convert_dict_to_plmarker(labeler1, two_labelers=False,save_source=True), convert_dict_to_plmarker(labeler2, two_labelers=False, save_source=True)]
    #get text
    text_list = radgraph_dataset['text'].split() #assume report is a sentence, given that newlines have been stripped and .'s don't always represent sentences

    #get ner labels, cache relationships
    entity_dict = radgraph_dataset['entities']
    entity_list = []
    relations_cache = []
    for k, entity in entity_dict.items():
        entity_list.append([entity['start_ix'], entity['end_ix'], entity['label']])
        if 'relations' in entity:
            for r in entity['relations']:
                relations_cache.append((k, r[0], r[1])) #(head, relationship, tail)
    
    #get relations
    relations_list = []
    for head, relationship, tail in relations_cache:
        head_start_ix, head_end_ix = entity_dict[head]['start_ix'], entity_dict[head]['end_ix']
        tail_start_ix, tail_end_ix = entity_dict[tail]['start_ix'], entity_dict[tail]['end_ix']
        relations_list.append([head_start_ix, head_end_ix, tail_start_ix, tail_end_ix, relationship])
    
    #add data source for test set (two labelers)
    if save_source:
        return {"sentences":[text_list], "ner":[entity_list], "relations":[relations_list], "data_source":radgraph_dataset['data_source']}
    return {"sentences":[text_list], "ner":[entity_list], "relations":[relations_list]}


def main():

    radgraph_dir = '/DEIDPATH/data/radgraph/1.0.0/' #TODO: fix relative import 
    for fname in ['train','dev','test']:
        parsed_contents = parse_file(f'{radgraph_dir}{fname}.json')
        
        if fname != 'test':            
            write_jsonl(parsed_contents, f'{radgraph_dir}{fname}_dygiepp_jsonl.json')
        else:
            for data_source in ['MIMIC-CXR','CheXpert']:
                relevant_contents = []
                for c in parsed_contents:
                    if 'data_source' in c and c['data_source'] == data_source:
                        c.pop('data_source')
                        relevant_contents.append(c)
                write_jsonl(relevant_contents, f'{radgraph_dir}{fname}_{data_source}_dygiepp_jsonl.json')

if __name__ == '__main__':
    main()

