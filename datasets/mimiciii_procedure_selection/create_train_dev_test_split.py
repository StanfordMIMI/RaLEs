"""
This script
    -takes in the LOINC labels for MIMIC III autoprocedure selection
    -creates a train/dev/test split
    -saves split to json file
    -saves each split into a different file in rales format
"""

import os
import pandas as pd
from constants import DATASET_PATH, MIMIC_III_DIRPATH
from sklearn.model_selection import train_test_split
import json
def main():
    # get mapped procedure titles
    procedure_titles = pd.read_csv(os.path.join(DATASET_PATH, 'annotated_dataset.csv'))

    # create train/dev/test split
    train, test = train_test_split(procedure_titles, test_size=0.2, random_state=28102022, stratify=procedure_titles['procedure_label'])
    train, dev = train_test_split(train, test_size=0.25, random_state=28102022, stratify=train['procedure_label'])

    # save train/dev/test split
    train_ids = set(train['ROW_ID'].unique())
    dev_ids = set(dev['ROW_ID'].unique())
    test_ids = set(test['ROW_ID'].unique())
    rowid2split = {**{str(ID):'train' for ID in train_ids}, **{str(ID):'dev' for ID in dev_ids}, **{str(ID):'test' for ID in test_ids}}
    rowid2label = dict(zip(procedure_titles['ROW_ID'].astype(str), procedure_titles['procedure_label']))
    rowid2split_label = {k: {'split':v, 'label':rowid2label[k]} for k,v in rowid2split.items()}

    with open(os.path.join(DATASET_PATH, 'rowid_split_label.json'), 'w') as f:
        json.dump(rowid2split_label, f)

    # save each split into a different file in rales format
    for split, df in zip(['train', 'dev', 'test'], [train, dev, test]):

        # save as csv
        df.to_csv(os.path.join(DATASET_PATH, f'mimiciii_ct_procedure_{split}.csv'), index=False)



if __name__ == '__main__':
    main()