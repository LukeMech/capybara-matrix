import sdkit
from sdkit.generate import generate_images
from sdkit.models import download_models, load_model, resolve_downloaded_model_path
from sdkit.utils import log, save_images

context = sdkit.Context()
context.device = "cpu"

download_models(
    models={
        "stable-diffusion": ["2.1-768-ema-pruned"],
    }
) # Downloads models

context.model_paths["stable-diffusion"] = resolve_downloaded_model_path("stable-diffusion", "2.1-768-ema-pruned")
load_model(context, "stable-diffusion")

images = generate_images(context, width=768, height=768, prompt="Very professional capybara photo", seed=42)
save_images(images, dir_path="./tmpImages")

log.info("Generated images!")