#!/bin/bash

docker run -it \
  -v `pwd`:/src \
  wbuchwalter/autoscaler-acs \
  /bin/bash