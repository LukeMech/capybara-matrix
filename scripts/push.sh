mkdir -p ../data/images/capy
cp ./tmp/*.jpg ../data/images/capy/
ls ../data/images/capy
ls ../
cp ./tmp/prompt.txt ./prompt.txt
python push.py $CONFIGPATH
rm -rf ./tmp
rm -rf ./prompt.txt

cd ..
git config --global user.name image-gen
git config --global user.email github-actions@github.com
git add .
git commit -m "Next capy photos"