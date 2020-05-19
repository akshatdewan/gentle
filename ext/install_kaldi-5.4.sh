#!/bin/bash

jobs=$1
# Prepare Kaldi
cd kaldi-5.4/tools
#make clean
make -j $jobs openfst OPENFST_VERSION=1.6.7
make -j $jobs openblas 
cd ../src
make clean
 ./configure --static --static-math=yes --static-fst=yes --use-cuda=no
make depend -j $jobs
cd ../../
 #./configure --shared --cudatk-dir=/usr/local/cuda-8.0
