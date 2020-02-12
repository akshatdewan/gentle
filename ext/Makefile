KALDI_BASE = kaldi/src/

all:
EXTRA_CXXFLAGS = -Wno-sign-compare
include $(KALDI_BASE)kaldi.mk

BINFILES = k3 m3

OBJFILES =

CXXFLAGS += -I$(KALDI_BASE) -O3 -DNDEBUG

ADDLIBS = $(KALDI_BASE)online2/kaldi-online2.a $(KALDI_BASE)ivector/kaldi-ivector.a \
          $(KALDI_BASE)nnet3/kaldi-nnet3.a $(KALDI_BASE)chain/kaldi-chain.a \
          $(KALDI_BASE)nnet2/kaldi-nnet2.a $(KALDI_BASE)lat/kaldi-lat.a \
          $(KALDI_BASE)decoder/kaldi-decoder.a  $(KALDI_BASE)cudamatrix/kaldi-cudamatrix.a \
          $(KALDI_BASE)feat/kaldi-feat.a $(KALDI_BASE)transform/kaldi-transform.a $(KALDI_BASE)gmm/kaldi-gmm.a \
          $(KALDI_BASE)thread/kaldi-thread.a $(KALDI_BASE)hmm/kaldi-hmm.a $(KALDI_BASE)tree/kaldi-tree.a \
          $(KALDI_BASE)matrix/kaldi-matrix.a $(KALDI_BASE)fstext/kaldi-fstext.a \
          $(KALDI_BASE)util/kaldi-util.a $(KALDI_BASE)base/kaldi-base.a

include $(KALDI_BASE)makefiles/default_rules.mk

#fr:
#KALDI_BASE_FR = kaldi-5.4/src/
#
#EXTRA_CXXFLAGS = -Wno-sign-compare
#include $(KALDI_BASE_FR)kaldi.mk
#
#BINFILES = k3-kaldi-5.4
#
#OBJFILES = 
#
#CXXFLAGS += -I$(KALDI_BASE_FR) -O3 -DNDEBUG
#
#ADDLIBS = $(KALDI_BASE_FR)online2/kaldi-online2.a $(KALDI_BASE_FR)ivector/kaldi-ivector.a \
#          $(KALDI_BASE_FR)nnet3/kaldi-nnet3.a $(KALDI_BASE_FR)chain/kaldi-chain.a \
#          $(KALDI_BASE_FR)nnet2/kaldi-nnet2.a $(KALDI_BASE_FR)lat/kaldi-lat.a \
#          $(KALDI_BASE_FR)decoder/kaldi-decoder.a  $(KALDI_BASE_FR)cudamatrix/kaldi-cudamatrix.a \
#          $(KALDI_BASE_FR)feat/kaldi-feat.a $(KALDI_BASE_FR)transform/kaldi-transform.a $(KALDI_BASE_FR)gmm/kaldi-gmm.a \
#          $(KALDI_BASE_FR)hmm/kaldi-hmm.a $(KALDI_BASE_FR)tree/kaldi-tree.a \
#          $(KALDI_BASE_FR)matrix/kaldi-matrix.a $(KALDI_BASE_FR)fstext/kaldi-fstext.a \
#          $(KALDI_BASE_FR)util/kaldi-util.a $(KALDI_BASE_FR)base/kaldi-base.a
#
#include $(KALDI_BASE_FR)makefiles/default_rules.mk
