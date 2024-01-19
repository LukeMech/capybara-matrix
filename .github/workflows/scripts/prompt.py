import json, sys, os, urllib.request
from tqdm import tqdm

os.environ['RWKV_JIT_ON'] = '1'
os.environ["RWKV_CUDA_ON"] = '0'

from rwkv.model import RWKV
from rwkv.utils import PIPELINE, PIPELINE_ARGS

with open(sys.argv[1] + '/langModel.json', 'r') as file:
    data = json.load(file)

with urllib.request.urlopen(data["model"]) as response, open('./tmp/model.pth', 'wb') as output_file:
    print('Downloading [' + data["model"] + "]...")
     # Get the total file size in bytes
    file_size = int(response.getheader('Content-Length', 0))
    # Initialize the tqdm progress bar
    progress_bar = tqdm(total=file_size, unit='B', unit_scale=True)
    # Download and write to the local file with progress update
    while True:
        buffer = response.read(8192)  # Adjust the buffer size as needed
        if not buffer:
            break
        output_file.write(buffer)
        progress_bar.update(len(buffer))
    # Close the progress bar
    progress_bar.close()

# 20B_tokenizer.json is in https://github.com/BlinkDL/ChatRWKV
with urllib.request.urlopen(data["tokenizer"]) as response, open('./tmp/chattokenizer.json', 'wb') as output_file:
    print('Downloading [' + data["tokenizer"] + "]...")
    # Get the total file size in bytes
    file_size = int(response.getheader('Content-Length', 0))
    # Initialize the tqdm progress bar
    progress_bar = tqdm(total=file_size, unit='B', unit_scale=True)
    # Download and write to the local file with progress update
    while True:
        buffer = response.read(8192)  # Adjust the buffer size as needed
        if not buffer:
            break
        output_file.write(buffer)
        progress_bar.update(len(buffer))
    # Close the progress bar
    progress_bar.close()

# download models: https://huggingface.co/BlinkDL
model = RWKV(model='./tmp/model.pth', strategy='cpu fp32')
pipeline = PIPELINE(model, "./tmp/chattokenizer.json") 

with open(sys.argv[1] + '/usedPrompts.json', 'r') as file:
    usedPrompts = json.load(file)

ctx = data["prompt"] + '\n' + '\n'.join(usedPrompts)

def callback(s):
    print(s, end='', flush=True)

    with open('./prompt.txt', 'a') as file:
        file.write(s)

args = PIPELINE_ARGS(temperature = 1.0, top_p = 0.7, top_k = 100, # top_k = 0 then ignore
                     alpha_frequency = 0.25,
                     alpha_presence = 0.25,
                     alpha_decay = 0.996, # gradually decay the penalty
                     token_ban = [0], # ban the generation of some tokens
                     token_stop = [], # stop generation whenever you see any token here
                     chunk_len = 256) # split input into chunks to save VRAM (shorter -> slower)

print('Generating output for question: ' + ctx)
pipeline.generate(ctx, token_count=1000, args=args, callback=callback)

print('\n')
out, state = model.forward([187, 510, 1563, 310, 247], None)
print(out.detach().cpu().numpy())                   # get logits
out, state = model.forward([187, 510], None)
out, state = model.forward([1563], state)           # RNN has state (use deepcopy to clone states)
out, state = model.forward([310, 247], state)
print(out.detach().cpu().numpy())                   # same result as above
print('\n')

print('Generated prompt.txt')