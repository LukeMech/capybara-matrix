pip install -U pip
pip install -U xformers --index-url https://download.pytorch.org/whl/cu121
pip install -U sdkit tqdm realesrgan

mkdir -p ./tmp/image/gen
python image.py $CONFIGPATH $MATRIXMODEL

i=1
for file in ./tmp/image/*.jpeg; do
    mv "$file" "./tmp/image/$i.jpg"
    i=$((i + 1))
done

mkdir -p ./out
python upscale.py $CONFIGPATH

mv ./out/*.jpg ./out/$(date '+%Y%m%d%H%M%S')-$JOBINDEX.jpeg