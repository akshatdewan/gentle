#!/bin/bash

# Prepare Kaldi
cd kaldi-5.4/tools
#make clean
make blas all -j 48
cd ../src
make clean
 ./configure --shared --cudatk-dir=/usr/local/cuda-8.0
make depend -j 48
cd ../../
