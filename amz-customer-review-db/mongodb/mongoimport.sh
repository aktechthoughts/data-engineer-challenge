#!/bin/bash

mongoimport -u admin \
            -p secret \
            --jsonArray \
            --db admin \
            --collection $1 \
            --file input/temp.json        
