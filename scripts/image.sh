pip install -U pip
pip install -U xformers --index-url https://download.pytorch.org/whl/cu121
pip install -U sdkit tqdm realesrgan

mkdir -p ./tmp/image/gen
python image.py $CONFIGPATH $MATRIXMODEL

mkdir -p ./out
python upscale.py $CONFIGPATH

mv ./out/*.png ./out/$(date '+%Y%m%d%H%M%S')-$JOBINDEX.png