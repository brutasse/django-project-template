#!/bin/sh

set -e

for template in $(find . -iname "*.template"); do 
    cp -v $template $(dirname $template)/$(basename $template .template)
done
pip install -r requirements.txt && pip freeze -l > requirements.txt
rm -f install.sh

