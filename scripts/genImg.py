properties = {
    "x": 1280,
    "y": 720,
}
 
import sdkit, json, random, sys, os, urllib.request
from sdkit.generate import generate_images
from sdkit.models import load_model
from sdkit.utils import log, save_images

context = sdkit.Context()
context.device = "cpu"

if len(sys.argv) != 2:
    print("Json prompts file path missing!")
    sys.exit(1)

# Choose prompt
with open(sys.argv[1] + '/prompts.json', 'r') as file:
    data = json.load(file)
if isinstance(data, list) and len(data) > 0:
    prompt = random.choice(data)

# Choose AI model
with open(sys.argv[1] + '/models.json', 'r') as file:
    data = json.load(file)
if isinstance(data, list) and len(data) > 0:
    model = random.choice(data)

with urllib.request.urlopen(model["repo_url"]+model["name"]) as response, open('./'+model["name"], 'wb') as output_file:
    output_file.write(response.read())

context.model_paths[model["sdkit_modeltype"]] = './' + model["name"]
load_model(context, model["sdkit_modeltype"])

log.info("| Starting generation with:")
log.info("Dimensions: " + str(properties["x"]) + "px x " + str(properties["y"]) + "px")
log.info("Request: " + prompt)

log.info("| Using:")
log.info("Model: " + model["name"])
log.info("Downloaded from: " + model["repo_url"])
log.info("Inference count: " + str(model["inference_count"]))

images = generate_images(context, width=properties["x"], height=properties["y"], prompt=prompt, seed=42, num_inference_steps=model["inference_count"])
save_images(images, dir_path="./tmp/images")

os.remove('./'+model["name"])

log.info("Generated images!")