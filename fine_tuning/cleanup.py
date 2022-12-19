"""
Removes model checkpoints except for best model for a collection of experiments.
"""

import os
import shutil
import json
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--cleanup_dir', type=str, required=True, default='./classification/')
    args = parser.parse_args()



def main():
    pass
    

    
if __name__=='__main__':
    main()