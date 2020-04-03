#!/bin/bash

# Prepare Kaldi
cd kaldi-5.4/tools
#make clean
make -j 48 openfst OPENFST_VERSION=1.6.7
make -j 48 openblas 
cd ../src
make clean
 ./configure --static --static-math=yes --static-fst=yes --use-cuda=no
make depend -j 48
cd ../../
 #./configure --shared --cudatk-dir=/usr/local/cuda-8.0
