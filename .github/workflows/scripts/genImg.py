properties = {
    "prompt": "Very professional capybara photo",
    "x": 1920,
    "y": 1080,

    "modelType": "stable-diffusion",
    "modelNames": ["sd-xl-refiner-1.0"],
    "inference_count": 5
}


import sdkit
from sdkit.generate import generate_images
from sdkit.models import download_models, load_model, resolve_downloaded_model_path
from sdkit.utils import log, save_images

context = sdkit.Context()
context.device = "cpu"

download_models(
    models={
        properties["modelType"]: properties["modelNames"]
    }
) # Downloads models

i = 0
context.model_paths[properties["modelType"]] = resolve_downloaded_model_path(properties["modelType"], properties["modelNames"][0])
load_model(context, properties["modelType"])

images = generate_images(context, width=properties["x"], height=properties["y"], prompt=properties["prompt"], seed=42, num_inference_steps=properties["inference_count"])
save_images(images, dir_path="./tmpImages/" + str(i))
 
i += 1

log.info("Generated images!")