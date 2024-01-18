import sdkit
from sdkit.models import download_model, resolve_downloaded_model_path, load_model
from sdkit.generate import generate_images
from sdkit.utils import log, save_images

context = sdkit.Context(device="cpu")

download_model("stable-diffusion", "sd-xl-refiner-1.0") # Downloads models

context.model_paths["sd-xl-refiner"] = resolve_downloaded_model_path("stable-diffusion", "sd-xl-refiner-1.0")
load_model(context, "sd-xl-refiner")

images = generate_images(context, width=768, height=768, prompt="Very professional capybara photo", seed=42)
save_images(images, dir_path="./tmpImages")

log.info("Generated images!")