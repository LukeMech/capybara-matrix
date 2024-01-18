properties = {
    "x": 768,
    "y": 768,

    "modelType": "stable-diffusion",
    "modelNames": ["2.1-768-ema-pruned"],
    "inference_count": 25
}


import sdkit
from sdkit.generate import generate_images
from sdkit.models import download_models, load_model, resolve_downloaded_model_path
from sdkit.utils import log, save_images
import json
import random
import sys

context = sdkit.Context()
context.device = "cpu"

if len(sys.argv) != 2:
    print("Json prompts file path missing!")
    sys.exit(1)

with open(sys.argv[1], 'r') as file:
    data = json.load(file)

if isinstance(data, list) and len(data) > 0:
    # Randomly choose one element from the array
    prompt = random.choice(data)

download_models(
    models={
        properties["modelType"]: properties["modelNames"]
    }
) # Downloads models

context.model_paths[properties["modelType"]] = resolve_downloaded_model_path(properties["modelType"], properties["modelNames"][0])
load_model(context, properties["modelType"])

log.info("| Starting generation with:")
log.info("Dimensions: " + str(properties["x"]) + "px x" + str(properties["y"]) + "px")
log.info("Request: " + prompt)

log.info("| Using:")
log.info("Model type: " + properties["modelType"])
log.info("Model name: " + properties["modelNames"])
log.info("Inference count: " + properties["inference_count"])

images = generate_images(context, width=properties["x"], height=properties["y"], prompt=random_element, seed=42, num_inference_steps=properties["inference_count"])
save_images(images, dir_path="./tmpImages")

log.info("Generated images!")