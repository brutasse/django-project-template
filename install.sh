#!/usr/bin/env bash

set -e

for template in $(find . -iname "*.template"); do 
    mv -v $template $(dirname $template)/$(basename $template .template)
done
pip install -r requirements.txt && pip freeze -l > requirements.txt
pip install -r requirements-dev.txt
comm -23 <(pip freeze -l | sort -n) <(cat requirements.txt | sort -n) > requirements-dev.txt
sed -i '1s/^/-r requirements.txt\n/' requirements-dev.txt
rm -f install.sh

