#!/bin/bash

docker run -p 27017:27017 -t -d \
           -e MONGO_INITDB_ROOT_USERNAME=admin \
           -e MONGO_INITDB_ROOT_PASSWORD=secret \
           -e MONGO_INITDB_DATABASE=amz_reviews \
                aktechthoughts/mongodb:latest

