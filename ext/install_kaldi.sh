#!/bin/bash

# Prepare Kaldi
cd kaldi/tools
make clean
make -j 32
./extras/install_openblas.sh
cd ../src
make clean
# make clean (sometimes helpful after upgrading upstream?)
./configure --static --static-math=yes --static-fst=yes --use-cuda=no --openblas-root=../tools/OpenBLAS/install
make -j 32 depend
make -j 32
cd ../../
