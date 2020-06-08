#!/bin/bash
# Designed to work on Ubuntu 18.04 LTS

set -x
tableconfig='config/tcon.json'

tablename=$(cat $tableconfig | \
    python3 -c "import sys, json; print(json.load(sys.stdin)['filenames'])" | \
    sed 's/\[//g' | sed 's/\]//g' )

for tname in $(echo $tablename | sed 's/,/ /g')
do
    tname=$(echo $tname | sed "s/'//g")

    url="https://s3.amazonaws.com/amazon-reviews-pds/tsv/amazon_reviews_us_"$tname".tsv.gz"


    wget  -O "input/"$tname".tsv.gz" $url
    mkdir -p "input/split/"

    gunzip "input/"$tname".tsv.gz"
    split -d -b 200M "input/"$tname".tsv" "input/split/"$tname
    rm "input/"$tname".tsv"

    ls input/split/"$tname"* | while read line
    do
    sudo python3 amz-review-test.py $tname $line
    sudo rm $line
    ne
    echo $line
    done

done
