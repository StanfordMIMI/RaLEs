"""
Script generated based on https://huggingface.co/spaces/allen-eric/radiology-gpt/blob/main/app.py commit 0a2af99
"""

import torch
from peft import PeftModel
from transformers import LlamaTokenizer, LlamaForCausalLM, GenerationConfig
import argparse
import os
import datasets
from datasets import load_dataset
from tqdm import tqdm
import json

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_file", type=str, required=True)
    parser.add_argument("--output_dir", type=str, required=True)
    parser.add_argument("--output_file_name", type=str, default="MEDIQA2021_test.json")
    
    args = parser.parse_args()

    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)
        print(f"Created output directory {args.output_dir}")
    args.output_file_name = args.output_file_name.replace("_out.json", f"{args.data_file.split('/')[-1].replace('.json', '')}_out.json")
    args.output_file_name = os.path.join(args.output_dir, args.output_file_name)

    return args

def get_model():
    tokenizer = LlamaTokenizer.from_pretrained("chavinlo/alpaca-native")
    BASE_MODEL = "chavinlo/alpaca-native"
    LORA_WEIGHTS = "allen-eric/lora-alpaca-7b-radiology-full"
    
    if torch.cuda.is_available():
            device = "cuda"
    elif torch.backends.mps.is_available():
            device = "mps"
    else:
            device = "cpu"    

    if device == "cuda":
        model = LlamaForCausalLM.from_pretrained(
            BASE_MODEL,
            load_in_8bit=False,
            torch_dtype=torch.float16,
            device_map="auto",
        )
        model = PeftModel.from_pretrained(
            model, LORA_WEIGHTS, torch_dtype=torch.float16, force_download=True
        )
    elif device == "mps":
        model = LlamaForCausalLM.from_pretrained(
            BASE_MODEL,
            device_map={"": device},
            torch_dtype=torch.float16,
        )
        model = PeftModel.from_pretrained(
            model,
            LORA_WEIGHTS,
            device_map={"": device},
            torch_dtype=torch.float16,
        )
    else:
        model = LlamaForCausalLM.from_pretrained(
            BASE_MODEL, device_map={"": device}, low_cpu_mem_usage=True
        )
        model = PeftModel.from_pretrained(
            model,
            LORA_WEIGHTS,
            device_map={"": device},
        )

    if device != "cpu":
        model.half()
    model.eval()
    if torch.__version__ >= "2":
        model = torch.compile(model)

    return model, tokenizer, device

def generate_prompt(instruction, input=None):
    if input:
        return f"""Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

                ### Instruction:
                {instruction}

                ### Input:
                {input}

                ### Response:"""
    else:
        return f"""Below is an instruction that describes a task. Write a response that appropriately completes the request.

                ### Instruction:
                {instruction}

                ### Response:"""






def evaluate(
    instruction,
    input=None,
    temperature=0.1,
    top_p=0.75,
    top_k=40,
    num_beams=4,
    max_new_tokens=128,
    **kwargs,
):
    prompt = generate_prompt(instruction, input)
    inputs = tokenizer(prompt, return_tensors="pt")
    input_ids = inputs["input_ids"].to(device)
    generation_config = GenerationConfig(
        temperature=temperature,
        top_p=top_p,
        top_k=top_k,
        num_beams=num_beams,
        **kwargs,
    )
    with torch.no_grad():
        generation_output = model.generate(
            input_ids=input_ids,
            generation_config=generation_config,
            return_dict_in_generate=True,
            output_scores=True,
            max_new_tokens=max_new_tokens,
        )
    s = generation_output.sequences[0]
    output = tokenizer.decode(s)
    return output.split("### Response:")[1].split("</s>")[0].strip()

if __name__=="__main__":
    args = parse_args()

    dataset = load_dataset("json", data_files={"data": args.data_file})

    model, tokenizer, device = get_model()
    
    model_predictions = []
    with tqdm(total=len(dataset['data']), unit="Findings->Impression") as pbar:
        for i, datapoint in enumerate(dataset['data']):
            if 'findings' in datapoint:
                findings = datapoint['findings']
            else:
                raise NotImplementedError("Datasets without findings not supported at this time.")
            if 'study_id' in datapoint:
                study_id = datapoint['study_id']
            else:
                raise NotImplementedError("Datasets without study_id not supported at this time.")
            
            predicted_impression = evaluate(f"Derive the impression from findings in the radiology report", f"Findings: {findings}")
            model_predictions.append({'study_id': study_id, 'predicted_impression': predicted_impression})
            pbar.update(1)
            
    with open(args.output_file_name, 'w') as f:
        f.write(json.dumps(model_predictions))
        
    #Test input, from RadiologyGPT arxiv preprint figure 5
    # print(evaluate("Derive the impression from findings in the radiology report", "Findings: PA and lateral views of the chest. The previously seen pericardial and pleural effusions have resolved. There is no pneumothorax. There is no consolidation. The cardiac, mediastinal, and hilar contours are normal."))
