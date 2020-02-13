import logging
import os

from util.paths import get_resource, ENV_VAR
from gentle import metasentence

class Resources():

    def __init__(self, lang):
        self.lang = lang
        if lang == "en":
            self.proto_langdir = get_resource('exp/langdir')
            self.nnet_gpu_path = get_resource('exp/tdnn_7b_chain_online/')
            self.full_hclg_path = get_resource('exp/tdnn_7b_chain_online/graph_pp/HCLG.fst')
        elif lang == "fr":
            self.proto_langdir= get_resource('exp/fr_exp/langdir')
            self.nnet_gpu_path = get_resource('exp/fr_exp/tdnn_6z_ceos_sp_online/')
            self.full_hclg_path = get_resource('exp/fr_exp/tdnn_6z_ceos_sp_online/graph_pp/HCLG.fst')
        else:
            raise RuntimeError("%s is not supported" %lang)

        def require_dir(path):
            if not os.path.isdir(path):
                raise RuntimeError("No resource directory %s.  Check %s environment variable?" % (path, ENV_VAR))


        require_dir(self.proto_langdir)
        require_dir(self.nnet_gpu_path)

        with open(os.path.join(self.proto_langdir, "words.txt")) as fh:
            self.vocab = metasentence.load_vocabulary(fh)


