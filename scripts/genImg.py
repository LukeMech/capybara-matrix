properties = {
    "x": 1280,
    "y": 720,
}
 
import sdkit, json, random, sys, os, urllib.request, shutil
from sdkit.generate import generate_images
from sdkit.models import load_model
from sdkit.utils import log, save_images

context = sdkit.Context()
context.device = "cpu"

if len(sys.argv) != 3:
    print("Json config file path or model name missing!")
    sys.exit(1)

# Choose prompt
with open(sys.argv[1] + '/prompt.txt', 'r') as file:
    prompt = file.read()

# Choose AI model

with open(sys.argv[1] + '/models.json', 'r') as file:
    data = json.load(file)
    model = data[sys.argv[2]]
    model["name"] = sys.argv[2]

with urllib.request.urlopen(model["repo_url"]) as response, open('./tmp/imggenmodel', 'wb') as output_file:
    output_file.write(response.read())

context.model_paths[model["sdkit_modeltype"]] = './tmp/imggenmodel'
load_model(context, model["sdkit_modeltype"])

log.info("| Starting generation with:")
log.info("Dimensions: " + str(properties["x"]) + "px x " + str(properties["y"]) + "px")
log.info("Request: " + prompt)

log.info("| Using:")
log.info("Model: " + model["name"])
log.info("Downloaded from: " + model["repo_url"])
log.info("Inference count: " + str(model["inference_count"]))

images = generate_images(context, width=properties["x"], height=properties["y"], prompt=prompt, seed=42, num_inference_steps=model["inference_count"])
save_images(images, dir_path="./out/images")

shutil.rmtree('./tmp')
os.remove(sys.argv[1] + '/prompt.txt')

with open(sys.argv[1] + '/usedPrompts.json', 'r') as file:
    data = json.load(file)
data.append(prompt)
with open(sys.argv[1] + '/usedPrompts.json', 'w') as file:
    json.dump(data, file, indent=2) 

log.info("Generated images!")