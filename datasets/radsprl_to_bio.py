from xml.dom import minidom

def getTokens(text, token_annotations):
    tokens = []
    for ta in token_annotations:
        tokens.append(text[ta[0]:ta[0]+ta[1]])
    return tokens

def getAnnotations(spatial_annotations, entity_names):
    annotations = []
    for elem in spatial_annotations:
        annotation = []
        annotation.append(('Indicator', int(elem.attributes['ts'].value), int(elem.attributes['tl'].value)))
        for name in entity_names:
            named_elems = elem.getElementsByTagName(name)
            for ne in named_elems:
                try:
                    annotation.append((name, int(ne.attributes['ts'].value), int(ne.attributes['tl'].value)))
                except:
                    token_starts = ne.attributes['ts'].value.split(',')
                    token_lengths = ne.attributes['tl'].value.split(',')
                    for i,ts in enumerate(token_starts):
                        annotation.append((name, int(ts), int(token_lengths[i])))
        annotations.append(annotation)
                    
    return annotations

def getNER(tokens, annotations):
    ner = ['O']*len(tokens)
    for a in annotations:
        ner[a[1]] = 'B-'+a[0]
        if a[2] > 1:
            for i in range(1, a[2]):
                ner[a[1]+i]= 'I-'+a[0]
    return ner

def getRelevantSentence(sentence_info, sprl_info, tokens):
    
    indicator_info = [x for x in sprl_info if x[0]=='Indicator'][0]
    sprl_start_loc = indicator_info[1]
    sprl_end_loc = sprl_start_loc + indicator_info[2]
    
    for i, (sentence_start, sentence_len) in enumerate(sentence_info):
        if sentence_start <= sprl_start_loc and sentence_start+sentence_len >= sprl_end_loc:
            return tokens[sentence_start: sentence_start+sentence_len], sentence_start
    
    return 
    # return tokens

def writeBIO(annotated_docs, write_path):
    with open(write_path, 'w') as fout:
        for doc in annotated_docs:
            for pair in doc:
                fout.write(pair[0]+'\t'+pair[1]+'\n')
                
            fout.write('\n')
if __name__=='__main__':
    radsprl_dat = minidom.parse('/bmrNAS/people/jmz/data/RadSpRL/Rad-SpRL.xml')
    docs = radsprl_dat.getElementsByTagName('Document')
    
    entity_names = ['Trajector', 'Landmark', 'Diagnosis', 'Hedge']
    docs_annotated = []
    
    for doc in docs:
        text = doc.getElementsByTagName('Text')[0].firstChild.wholeText
        token_info = [(int(elem.attributes['cs'].value), int(elem.attributes['cl'].value)) for elem in \
            doc.getElementsByTagName('Annotations')[0].getElementsByTagName('Token')]
        sentence_info = [(int(elem.attributes['ts'].value), int(elem.attributes['tl'].value)) for elem in \
            doc.getElementsByTagName('Annotations')[0].getElementsByTagName('Sentence')]
        entity_info = [elem for elem in \
                    doc.getElementsByTagName('Annotations')[0].getElementsByTagName('RadSpRLRelation')]
        if len(entity_info) <1:
            continue
        
        tokens = getTokens(text, token_info)
        annotations = getAnnotations(entity_info, entity_names)
        for sprl in annotations:
            
            sentence_tokens, sentence_start_idx = getRelevantSentence(sentence_info, sprl, tokens)
            sprl_reindexed = [(x[0], x[1]-sentence_start_idx, x[2]) for x in sprl]
            try:
                ner = getNER(sentence_tokens, sprl_reindexed)
            except:
                print(sentence_tokens)
                print(annotations)
                print(tokens)
                exit()
            docs_annotated.append(list(zip(sentence_tokens, ner)))

    writeBIO(docs_annotated, '/dataNAS/people/jmz/data/RadSpRL/Rad-SpRL.bio')
    #convert to jsonl with ../../utils/bio_to_json.py