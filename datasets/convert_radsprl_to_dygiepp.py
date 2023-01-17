"""
Converts RadSpRL dataset to dygiepp 

RadSpRL dataset:
https://data.mendeley.com/datasets/yhb26hfz8n/1 

dygiepp format:
https://github.com/dwadden/dygiepp/blob/4420bf990cc9f7bcba38dde5861d62727d0109ab/doc/data.md

Used for relationship extraction task
"""

import json 
from xml.dom import minidom
from collections import Counter
from numpy.random import choice, seed
import os


def flatten(l):
    return [item for sublist in l for item in sublist]

def getTokens(text, token_annotations):
    tokens = []
    for ta in token_annotations:
        tokens.append(text[ta[0]:ta[0]+ta[1]])
    return tokens

def getAnnotations(spatial_annotations, entity_names):
    entities = []
    relations = []
    for elem in spatial_annotations:
        elem_entities = []
        elem_relations = []
        indicator = ('Indicator', int(elem.attributes['ts'].value), int(elem.attributes['tl'].value))
        elem_entities.append(indicator)
        for name in entity_names:
            named_elems = elem.getElementsByTagName(name)
            for ne in named_elems:
                try:
                    elem_entities.append((ne.attributes['type'].value, int(ne.attributes['ts'].value), int(ne.attributes['tl'].value)))
                    elem_relations.append((indicator, (name, int(ne.attributes['ts'].value), int(ne.attributes['tl'].value))))
                except:
                    token_starts = ne.attributes['ts'].value.split(',')
                    token_lengths = ne.attributes['tl'].value.split(',')
                    for i,ts in enumerate(token_starts):
                        elem_entities.append((ne.attributes['type'].value, int(ts), int(token_lengths[i])))
                        elem_relations.append((indicator, (name, int(ts), int(token_lengths[i]))))
        entities.append(elem_entities)
        relations.append(elem_relations)
    return entities, relations

def getPositiveSentenceAnnotations(sentences, sentence_info, entities, relations):
    
    # keep only sentences that contain entities

    sentence_start_stops = []
    for sentence_loc in sentence_info:
        sentence_start_stops.append((sentence_loc[0], sentence_loc[0]+sentence_loc[1])) #sentence stop is noninclusive
    
    sentences_with_entities = set()
    for entity_set in entities:
        entity_set_remapped = []
        for entity in entity_set:
            entity_start = entity[1]
            for i, (s_start, s_stop) in enumerate(sentence_start_stops):
                if entity_start >= s_start and entity_start < s_stop:
                    sentences_with_entities.add(i)
                    break
    
    entity_sentence_start_stop = [x for i,x in enumerate(sentence_start_stops) if i in sentences_with_entities]
    pos_sentences = [x for i,x in enumerate(sentences) if i in sentences_with_entities]
    
    
    # get sentence location per entity
    sentence2entities = {k:[] for k in range(len(entity_sentence_start_stop))}
    for entity_set in entities:
        entity_set_remapped = []
        for entity in entity_set:
            entity_start = entity[1]
            for i, (s_start, s_stop) in enumerate(entity_sentence_start_stop):
                if entity_start >= s_start and entity_start < s_stop:
                    sentence2entities[i].append([entity_start, entity_start+entity[2]-1, entity[0]])
                    break
        
    # get sentence location per relation
    sentence2relations = {k:[] for k in range(len(entity_sentence_start_stop))}
    
    for relation_set in relations:
        relation_set_remapped = []
        for head, tail in relation_set:
            entity_start = head[1]
            for i, (s_start, s_stop) in enumerate(entity_sentence_start_stop):
                if entity_start >= s_start and entity_start < s_stop:
                    sentence2relations[i].append([head[1], head[1]+head[2]-1, tail[1], tail[1]+tail[2]-1, tail[0]])
                    break
        
    return pos_sentences, entity_sentence_start_stop, sentence2entities, sentence2relations

def correctIndexing(sentence_start_end, sentence2entities, sentence2relations):
    entities = []
    relations = []
    old_start_end = {i:x for i,x in enumerate(sentence_start_end)}
    new_sent_start_end = {}
    
    for i, (sent_start, sent_end) in enumerate(sentence_start_end):
        if i == 0:
            new_sent_start_end[i] = (0, sent_end-sent_start-1)
        else:
            new_sent_start_end[i] = (new_sent_start_end[i-1][1]+1, sent_end-sent_start + new_sent_start_end[i-1][1]) #end is inclusive

    for k in sentence2entities:
        # print(f'{old_start_end[k]} \t -> \t {new_sent_start_end[k]}')
        sentence_entities = []
        for entity in sentence2entities[k]:
            
            new_entity = [entity[0]-old_start_end[k][0]+new_sent_start_end[k][0], entity[1]-old_start_end[k][0]+new_sent_start_end[k][0], entity[2]]
            # print(f'{entity} \t -> \t {new_entity}')
            sentence_entities.append(new_entity)
        entities.append(sentence_entities)
    
    for k in sentence2relations:
        sentence_relations = []
        for relation in sentence2relations[k]:
            new_relation = [relation[0]-old_start_end[k][0]+new_sent_start_end[k][0], relation[1]-old_start_end[k][0]+new_sent_start_end[k][0], 
                            relation[2]-old_start_end[k][0]+new_sent_start_end[k][0], relation[3]-old_start_end[k][0]+new_sent_start_end[k][0], 
                            relation[4]]
            # print(f'{relation} \t -> \t {new_relation}')
            sentence_relations.append(new_relation)
        relations.append(sentence_relations)
    return entities, relations

def get_sentences(text, token_info, sentence_info):
    sentences = []
    tokens = []
    for token_start, token_len in token_info:
        tokens.append(text[token_start: token_start+token_len])
    
    for token_start, token_len in sentence_info:
        sentences.append(tokens[token_start: token_start+token_len])
    return sentences

def get_sentence_entities_relations(radsprl_document):
    relation_names = ['Trajector', 'Landmark', 'Diagnosis', 'Hedge']
    text = radsprl_document.getElementsByTagName('Text')[0].firstChild.wholeText
    token_info = [(int(elem.attributes['cs'].value), int(elem.attributes['cl'].value)) for elem in \
        radsprl_document.getElementsByTagName('Annotations')[0].getElementsByTagName('Token')]
    sentence_info = [(int(elem.attributes['ts'].value), int(elem.attributes['tl'].value)) for elem in \
                radsprl_document.getElementsByTagName('Annotations')[0].getElementsByTagName('Sentence')]
    sentences = get_sentences(text, token_info, sentence_info)
    entity_info = [elem for elem in \
                radsprl_document.getElementsByTagName('Annotations')[0].getElementsByTagName('RadSpRLRelation')]
    if len(entity_info) > 0:
        entities, relations = getAnnotations(entity_info, relation_names)
        pos_sentences, pos_sentences_ixs, s2e, s2r = getPositiveSentenceAnnotations(sentences, sentence_info, entities, relations)
        pos_sentence_entities, pos_sentence_relations = correctIndexing(pos_sentences_ixs, s2e, s2r)
    else:
        return
    return (pos_sentences, pos_sentence_entities, pos_sentence_relations)
def main():
    radsprl_dir = '/dataNAS/people/jmz/data/RadSpRL/' #TODO: fix relative import
    radsprl_file = os.path.join(radsprl_dir, 'Rad-SpRL.xml')
    radsprl_docs = minidom.parse(radsprl_file).getElementsByTagName('Document')
    
    positive_documents = []
    for doc in radsprl_docs:
        formatted_ser = get_sentence_entities_relations(doc)
        if formatted_ser is not None:
            formatted_doc = {}
            formatted_doc['doc_key'] = doc.attributes['id'].value
            # if formatted_doc['doc_key'] == "01075":
            #     print(formatted_ser[0])
            #     print(formatted_ser[1])
            #     print(formatted_ser[2])
            #     exit()
            # if formatted_doc['doc_key'] == "00709":
            #     print(formatted_ser[0])
            #     print(formatted_ser[1])
            #     print(formatted_ser[2])
            #     exit()
            formatted_doc['dataset'] = "radsprl"
            formatted_doc['sentences'] = formatted_ser[0]
            formatted_doc['ner'] = formatted_ser[1]
            formatted_doc['relations'] = formatted_ser[2]
            positive_documents.append(formatted_doc)
    
    seed(2023)

    train_ixs = choice(len(positive_documents), int(len(positive_documents)*0.8), replace=False)
    devtest_ixs = [i for i in range(len(positive_documents)) if i not in train_ixs]
    dev_ixs = choice(devtest_ixs, int(len(devtest_ixs)/2), replace=False)
    test_ixs = [i for i in devtest_ixs if i not in dev_ixs]
    all_ixs = flatten([train_ixs, dev_ixs, test_ixs])
    
    for fname in ['train','dev','test']:
        contents = list(map(lambda x: positive_documents[x], train_ixs if fname == 'train' else dev_ixs if fname == 'dev' else test_ixs))
        with open(os.path.join(radsprl_dir, f'radsprl_dygiepp_{fname}.jsonl'), 'w') as f:
            f.write('\n'.join(map(json.dumps, contents)))

if __name__ == '__main__':
    main()

