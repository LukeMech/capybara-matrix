mkdir -p ./images/capy/
cp $HOME/tmp/*/*.jpeg ./data/images/capy/
cp $HOME/tmp/*/prompt.txt $HOME/prompt.txt
python push.py $CONFIGPATH

git config --global user.name image-gen
git config --global user.email github-actions@github.com
git add .
git commit -m "Next capy photos"