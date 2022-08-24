# Converting PubTator format to BIO format for NER recognition. Mainly used for BC5CDR dataset
# Author: jmz

import argparse
import re

def parseargs():
    parser = argparse.ArgumentParser(description='convert PubTator to BIO format')
    parser.add_argument('-fname', type=str, default='/dataNAS/people/jmz/data/bc5cdr/CDR_Data/CDR.Corpus.v010516/CDR_TrainingSet.PubTator.txt')
    args = parser.parse_args()
    return args

def parse_pubtator(fpath):
    """
    Creates dictionary from Pubtator.txt file, keeping PubMed IDs, title, abstract, entity texts and labels
    """
    parsed = {}
    with open(fpath, 'r') as fin:
        contents = fin.readlines()
    
    for c in contents:
        if c[0].isnumeric():
            if '|t|' in c or '|a|' in c: #title or abstract
                line_content = c.strip().split('|')
                pmid = line_content[0]
                if pmid in parsed:
                    parsed[pmid][line_content[1]] = line_content[2]
                    parsed[pmid]['concept_start_end'] = []
                    parsed[pmid]['concept_text'] = []
                    parsed[pmid]['concept_label'] = []
                    parsed[pmid]['concept_identifier'] = []
                else:
                    parsed[pmid] = {line_content[1]:line_content[2]}

            elif '\t' in c:
                line_content = c.strip().split('\t')
                pmid = line_content[0]
                if pmid in parsed and line_content[1].isnumeric():
                    parsed[pmid]['concept_start_end'].append((int(line_content[1]), int(line_content[2])))
                    parsed[pmid]['concept_text'].append(line_content[3])
                    parsed[pmid]['concept_label'].append(line_content[4])
                    parsed[pmid]['concept_identifier'].append(line_content[5])
                else:
                    continue
    

    return parsed

def convert_parsed_pubtator_to_bio(parsed_dict):
    """
    Creates BIO format text output from a parsed Pubtator.txt file in a dictionary format
    """
    
    def split_chunk(chunk):
        chunk = re.sub('(?<! )(?=[!"#$%&\'()*+,./:;<=>?@[\\]^_`{|}~])|(?<=[!"#$%&\'()*+,./:;<=>?@[\\]^_`{|}~])(?! )', r' ', chunk)
        chunk = re.sub('(^-)', r'- ', chunk)
        chunk = re.sub('\s{2,}', ' ', chunk)
        return chunk.strip().split(' ')
    
    bio_dataset = []
    
    for v in parsed_dict.values():
        
        concept2label =  {}
        for i,concept in enumerate(v['concept_text']):
            label = v['concept_label'][i]
            concept2label[concept] = label

        merged_text = v['t'] + ' ' + v['a']
        
        split_text = []

        last_end = 0
        for i, (start, end) in enumerate(v['concept_start_end']):
            if start > last_end:
                split_text.append(merged_text[last_end:start])
            split_text.append(merged_text[start:end])
            if i == len(v['concept_start_end'])-1:
                split_text.append(merged_text[end:])
            last_end = end

        NER = []
        for word in split_text:
            if word in concept2label:
                NER.append(concept2label[word])
            else:
                NER.append('O')
        processed_text = []
        for txt, label in zip(split_text, NER):
            if label == 'O':
                split_txt = split_chunk(txt.strip())
                for s in split_txt:
                    processed_text.append((s, 'O'))
            else:
                if ' ' in txt:
                    split_txt = txt.split(' ')
                    processed_text.append((split_txt[0], 'B-'+label))
                    for remainder in split_txt[1:]:
                        processed_text.append((remainder, 'I-'+label))
                else:
                    processed_text.append((txt, 'I-'+label))
        bio_dataset.append(processed_text)
        
    return bio_dataset

def write_bio(bio_dataset, fpath):

    with open(fpath, 'w') as fout:
        for text in bio_dataset:
            for word, label in text:
                fout.write('\t'.join([word,label])+'\n')
                if word == '.':
                    fout.write('\n')

def main():
    args = parseargs()

    bc5cdr_pubtator = parse_pubtator(args.fname)
    bc5cdr_bio = convert_parsed_pubtator_to_bio(bc5cdr_pubtator)
    
    write_bio(bc5cdr_bio, args.fname.replace('.txt', '.bio'))
    
if __name__=='__main__':
    main()