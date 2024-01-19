pip install --upgrade pip
pip install sdkit tqdm xformers --index-url https://download.pytorch.org/whl/cu121

mkdir -p ./tmp/image
python image.py $CONFIGPATH $MATRIXMODEL

mv ./tmp/*.jpeg ./tmp/image/$(date '+%Y%m%d%H%M%S')-$JOBINDEX.jpeg
