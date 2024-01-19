pip install --upgrade pip
pip install sdkit tqdm

mkdir -p ./tmp
python image.py $CONFIGPATH $MATRIXMODEL

mv ./tmp/*.jpeg ./tmp/image/$(date '+%Y%m%d%H%M%S')-$JOBINDEX.jpeg