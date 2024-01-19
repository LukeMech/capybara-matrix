pip install -U pip
pip install -U xformers --index-url https://download.pytorch.org/whl/cu121
pip install -U sdkit tqdm realesrgan

mkdir -p ./tmp/image/gen
python image.py $CONFIGPATH $MATRIXMODEL
for file in ./tmp/image/gen/*.jpeg; do
    mv "$file" "${file%.jpeg}.jpg"
done

python upscale.py $CONFIGPATH

mv ./tmp/image/*.jpeg ./tmp/image/$(date '+%Y%m%d%H%M%S')-$JOBINDEX.jpeg
