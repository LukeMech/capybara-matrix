properties = {
    "x": 1280,
    "y": 720,

    "model_name": "sd_xl_turbo_1.0.safetensors",
    "model_url": "https://huggingface.co/stabilityai/sdxl-turbo/resolve/main/",
    "inference_count": 5
}
 
import sdkit, json, random, sys, os, urllib.request
from sdkit.generate import generate_images
from sdkit.models import download_models, load_model, resolve_downloaded_model_path
from sdkit.utils import log, save_images

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

with urllib.request.urlopen(properties["model_url"]+properties["model_name"]) as response, open('.', 'wb') as output_file:
    output_file.write(response.read())

# context.model_paths[properties["modelType"]] = resolve_downloaded_model_path(properties["modelType"], properties["modelNames"][0])
context.model_paths[properties["modelType"]] = './' + properties["model_name"]
load_model(context, properties["modelType"])

log.info("| Starting generation with:")
log.info("Dimensions: " + str(properties["x"]) + "px x " + str(properties["y"]) + "px")
log.info("Request: " + prompt)

log.info("| Using:")
log.info("Model type: " + properties["modelType"])
log.info("Model name: " + properties["modelNames"][0])
log.info("Inference count: " + str(properties["inference_count"]))

images = generate_images(context, width=properties["x"], height=properties["y"], prompt=prompt, seed=42, num_inference_steps=properties["inference_count"])
save_images(images, dir_path="./tmp/images")

os.remove('./' + properties["model_name"])

log.info("Generated images!")