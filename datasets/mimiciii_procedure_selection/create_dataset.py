"""
Code for creating the dataset, including manual annotation of groups of procedure titles
"""

import pandas as pd
from collections import Counter
import re
import os
from constants import DATASET_PATH, MIMIC_III_DIRPATH
from ast import literal_eval

def flatten(l=None, d=None):
    """
    Returns a flattened version of the list l or dict d
    """
    if l is not None:
        result = []
        for i in l:
            if isinstance(i,list):
                result.extend(flatten(l=i))
            else: result.append(i)
        return result
    elif d is not None:
        return dict(ChainMap(*d))
def getIndicationInfo(report_text):
    """
    Pre-processing of report_text to get section with medical condition/reason for examination
    """
    end=None
    start=report_text.find('Reason:')
    if start == -1:
        start = report_text.find('MEDICAL CONDITION')
    else:
        report_text = report_text[start+7:]
        end = report_text.find('\n')
        if end == -1:
            end = report_text.find('Admitting Diagnosis:')
        if end == -1:
            end = report_text.find('Field')
        if end == -1:
            end = report_text.find('____')
        return report_text[:end]
    if start == -1:
        start = report_text.find('CLINICAL INFORMATION & QUESTIONS TO BE ANSWERED')
    if start == -1:
        start = report_text.find('INDICATION')
        end = report_text.find('COMPARISON')
    if start == -1:
        start = report_text.find('HISTORY')
        end = report_text.find('TECHNIQUE')
    if start == -1:
        return None
    report_text = report_text[start:]
    if end is None:
        end = report_text.find('__________')
    return report_text[:end]

def get_ct_reports():
    iter_csv = pd.read_csv(os.path.join(MIMIC_III_DIRPATH,'NOTEEVENTS.csv.gz'), iterator=True, chunksize=10000)
    df = pd.concat([chunk[chunk['CATEGORY']=="Radiology"] for chunk in iter_csv])
    df = df[df['DESCRIPTION'].str.startswith("CT")]
    return df

def get_report_titles(report_text):
    """
    Parses each report to get the header, which should include the procedure title
    """
    start = report_text.find('CT')
    end = report_text.find('_____')
    
    #Remove reason/admitting diagnosis/field of view lines
    for text in ['Reason:', 'Admitting Diagnosis:', 'Field of view:']:
        text_idx = report_text.find(text)
        if text_idx != -1 and text_idx<end:
            end = text_idx

    report_header = report_text[start:end]
    report_header = report_header.replace('Clip #','')
    report_header = re.sub("[\[**].*?[**\]]", ";", report_header)
    report_header = re.sub(r'\n', ';', report_header)
    report_header = re.sub(r'\s{2, 100}', ';', report_header)
    report_header = re.sub(r'\t{1, 10}', ';', report_header)

    titles =[x.strip() for x in report_header.split(';') if x.strip().startswith('CT') and not bool(re.search(r'\d', x))] 
    titles = flatten(titles)
    
    return titles
def main():
    #Get all CT reports
    CT_notes = get_ct_reports()

    #Obtain indications for each report from the header
    CT_notes['indication'] = CT_notes['TEXT'].apply(getIndicationInfo)
    CT_notes = CT_notes[(~pd.isna(CT_notes['indication'])) & (CT_notes['indication'] != '')]
    
    #Obtain all headers from reports
    CT_notes['report_titles'] = CT_notes.apply(lambda x: get_report_titles(x['TEXT']), axis=1)
    CT_notes = CT_notes[(~pd.isna(CT_notes['report_titles'])) & (CT_notes['report_titles'].apply(lambda x: len(x)>0))]
    
    if not os.path.exists(os.path.join(DATASET_PATH, 'procedure_titles_mapped.csv')):
        #Save procedure titles with frequency for review
        procedure_counts = Counter([x for x in [frozenset(x) for x in CT_notes['report_titles']]])
        
    else:
        proc_counts = pd.read_csv(os.path.join(DATASET_PATH, 'procedure_titles_mapped.csv'))
        proc_titles2loinc = dict(zip(proc_counts['procedure_titles'], proc_counts['LOINC_NUM']))
        proc_titles2loinc = {frozenset(literal_eval(k)):v for k,v in proc_titles2loinc.items()}
        loinc2count = dict(zip(proc_counts['LOINC_NUM'], proc_counts['s']))
    
    #Map procedure titles to LOINC codes
    CT_notes['procedure_label'] = CT_notes['report_titles'].apply(lambda x: proc_titles2loinc[frozenset(x)] if frozenset(x) in proc_titles2loinc else None)
    
    annotated_dataset = CT_notes.loc[:,['ROW_ID','indication','procedure_label']][(~pd.isna(CT_notes['procedure_label'])) & (CT_notes['indication'] != '')]

    annotated_dataset.to_csv(os.path.join(DATASET_PATH, 'annotated_dataset.csv'), index=False)
    
if __name__=='__main__':
    main()