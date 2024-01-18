properties = {
    "prompt": "Very professional capybara photo",
    "x": 1920,
    "y": 1080,

    "models": {
        "codeformer": [],
        
        "controlnet": [],

        "gfpgan": [],

        "realesrgan": [],

        "stable_diffusion": [
            "d-xl-refiner-1.0",
        ],

        "vae": []
    },
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
        "codeformer": properties["models"]["codeformer"],
        "controlnet": properties["models"]["controlnet"],
        "gfpgan": properties["models"]["gfpgan"],
        "realesrgan": properties["models"]["realesrgan"],
        "stable_diffusion": properties["models"]["stable_diffusion"],
        "vae": properties["models"]["vae"]
    }
) # Downloads models

i = 0
for modelType in properties["models"]:
    for model in modelType:
        context.model_paths[modelType] = resolve_downloaded_model_path(modelType, model)
        load_model(context, modelType)

        images = generate_images(context, width=properties["x"], height=properties["y"], prompt=properties["prompt"], seed=42, num_inference_steps=properties["inference_count"])
        save_images(images, dir_path="./tmpImages/" + str(i))
        i += 1

log.info("Generated images!")