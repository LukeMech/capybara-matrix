mkdir -p ./images/capy/
cp ./tmp/*/*.jpeg ../../../data/images/capy/
cp ./tmp/*/prompt.txt ./prompt.txt
python push.py $CONFIGPATH
rm -rf ./tmp

git config --global user.name image-gen
git config --global user.email github-actions@github.com
git add .
git commit -m "Next capy photos"