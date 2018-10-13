#!/bin/bash

find $1 -name "*.zip" > files.log
while IFS='' read -r line || [[ -n "$line" ]]; do
    #echo "Text read from file: $line"
    cp $line $2
done < files.log

#rm -rf files.log
