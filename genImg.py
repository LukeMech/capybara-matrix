import sdkit
from sdkit.models import download_models, resolve_downloaded_model_path, load_model
from sdkit.generate import generate_images
from sdkit.utils import save_images

context = sdkit.Context()

download_models(context, models={'stable-diffusion': '2.1-768-ema-pruned'}) # downloads the known "SD 1.5-pruned-emaonly" model

context.model_paths['stable-diffusion'] = resolve_downloaded_model_path(context, 'stable-diffusion', '1.5-pruned-emaonly')
load_model(context, 'stable-diffusion')

images = generate_images(context, width=512, height=512, prompt='very professional capybara photo', seed=42)
save_images(images, dir_path='./tmpImages')