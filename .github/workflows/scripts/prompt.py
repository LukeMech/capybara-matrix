import json, sys, os, urllib.request

os.environ['RWKV_JIT_ON'] = '1'
os.environ["RWKV_CUDA_ON"] = '0'

from rwkv.model import RWKV
from rwkv.utils import PIPELINE, PIPELINE_ARGS

with open(sys.argv[1] + '/langModel.json', 'r') as file:
    data = json.load(file)

with urllib.request.urlopen(data["model"]) as response, open('$HOME/tmp/model.pth', 'wb') as output_file:
    output_file.write(response.read())

# 20B_tokenizer.json is in https://github.com/BlinkDL/ChatRWKV
with urllib.request.urlopen(data["tokenizer"]) as response, open('$HOME/tmp/chattokenizer.json', 'wb') as output_file:
    output_file.write(response.read())

# download models: https://huggingface.co/BlinkDL
model = RWKV(model='$HOME/tmp/model.pth', strategy='cpu fp32')
pipeline = PIPELINE(model, "$HOME/tmp/chattokenizer.json") 

with open(sys.argv[1] + '/prompts.json', 'r') as file:
    usedPrompts = json.load(file)

ctx = data["prompt"] + '\n' + '\n'.join(usedPrompts)

def callback(s):
    print(s, end='', flush=True)

    with open('$HOME/prompt.txt', 'w') as file:
        file.write(s)

args = PIPELINE_ARGS(temperature = 1.0, top_p = 0.7, top_k = 100, # top_k = 0 then ignore
                     alpha_frequency = 0.25,
                     alpha_presence = 0.25,
                     alpha_decay = 0.996, # gradually decay the penalty
                     token_ban = [0], # ban the generation of some tokens
                     token_stop = [], # stop generation whenever you see any token here
                     chunk_len = 256) # split input into chunks to save VRAM (shorter -> slower)

pipeline.generate(ctx, token_count=200, args=args, callback=callback)