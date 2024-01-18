import sdkit
from sdkit.models import download_model, resolve_downloaded_model_path, load_model
from sdkit.generate import generate_images
from sdkit.utils import log, save_images

context = sdkit.Context()
context.device = "cpu"

download_model("stable-diffusion", "2.1-768-ema-pruned") # Downloads models

context.model_paths["2.1-768-ema-pruned"] = resolve_downloaded_model_path("stable-diffusion", "2.1-768-ema-pruned")
load_model(context, "2.1-768-ema-pruned")

images = generate_images(context, width=768, height=768, prompt="Very professional capybara photo", seed=42)
save_images(images, dir_path="./tmpImages")

log.info("Generated images!")