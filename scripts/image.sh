pip install -U pip
pip install -U xformers --index-url https://download.pytorch.org/whl/cu121
pip install -U sdkit tqdm realesrgan

mkdir -p ./tmp/image/gen
python image.py $CONFIGPATH $MATRIXMODEL
rename 's/\.jpeg$/.jpg/' ./tmp/image/gen/*.jpeg
python upscale.py $MATRIXMODEL

mv ./tmp/image/*.jpeg ./tmp/image/$(date '+%Y%m%d%H%M%S')-$JOBINDEX.jpeg
