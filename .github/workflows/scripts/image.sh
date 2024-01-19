pip install --upgrade pip
pip install sdkit

mkdir -p $HOME/tmp
python image.py $CONFIGPATH $MATRIXMODEL

mv $HOME/tmp/*.jpeg $HOME/tmp/image/$(date '+%Y%m%d%H%M%S')-$JOBINDEX.jpeg