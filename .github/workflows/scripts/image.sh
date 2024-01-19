pip install -U pip
pip install -U sdkit tqdm 
pip install -U xformers --index-url https://download.pytorch.org/whl/cu121

mkdir -p ./tmp/image
python image.py $CONFIGPATH $MATRIXMODEL

mv ./tmp/*.jpeg ./tmp/image/$(date '+%Y%m%d%H%M%S')-$JOBINDEX.jpeg
