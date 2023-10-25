"""
Utillities to generate statistics for datasets in RaLEs
"""

import os
import json
from datasets import load_dataset
import statistics
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset_dir', type=str,  help='Dir containing dataset', default="/dataNAS/people/jmz/data/RRS/rales_rrs/BIONLP2023/")
    
    args = parser.parse_args()
    return args

def get_json_dataset_contents(dataset_path):
    """
    Returns the contents of a json dataset as a list of dictionaries
    """
    dataset = load_dataset('json', data_files={'data': dataset_path})['data']
    return dataset

def generate_length_stats(reports):
    
    lengths = [len(report.split()) for report in reports]
    print(f"Min length: {min(lengths)}")
    print(f"Max length: {max(lengths)}")
    print(f"Mean length: {sum(lengths)/len(lengths):.1f}")
    print(f"Standard deviation: {statistics.stdev(lengths):.1f}")

def main():
    args = parse_args()
    dataset_dir = args.dataset_dir

    for file in os.listdir(dataset_dir):
        if file.endswith('.json'):
            dataset_path = os.path.join(dataset_dir, file)
            print(f"Dataset: {dataset_path}")
            dataset = get_json_dataset_contents(dataset_path)
            
            if 'BIONLP2023' in dataset_path or 'MEDIQA2021' in dataset_path:
                print(f'Number of reports: {len(dataset)}')
                reports = ['\n'.join(item) for item in zip(dataset['findings'],dataset['impression'])]
                
                generate_length_stats(reports)

if __name__=='__main__':
    main()
