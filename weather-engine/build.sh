#!/bin/bash

docker build . -t aktechthoughts/weather-engine:latest
# docker run --rm \
#     -v /home/abhishek/projects/python/weather-engine/tests-results:/app/tests-results \
#     -it aktechthoughts/weather-engine:latest \
    

docker create -ti --name dummy aktechthoughts/weather-engine:latest /bin/bash/bash
docker cp dummy:/app/tests-results/result.xml tests-results
docker rm -f dummy