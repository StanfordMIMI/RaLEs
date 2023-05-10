from omegaconf import OmegaConf
import argparse
from eval_rales_ner import do_ner_rales
from eval_rales_doc_classification import do_document_classification_rales


def parse_config():
    parser = argparse.ArgumentParser(description='RaLEs Evaluation')
    parser.add_argument('--config', type=str, default='configs/config.yaml', help='config file path')
    args = parser.parse_args()
    
    return OmegaConf.load(args.config)

def main():
    config = parse_config()
    if 'mimiciii_ct_procedure' in config.eval_datasets:
        config.dataset_text_col = 'indication'
        do_document_classification_rales(task='mimiciii_ct_procedure', config=config)
    if 'radgraph_ner' in config.eval_datasets:
        do_ner_rales(task='radgraph_ner', config=config)
    if 'stanza_ner' in config.eval_datasets:
        do_ner_rales(task='stanza_ner', config=config)
if __name__=='__main__':
    main()