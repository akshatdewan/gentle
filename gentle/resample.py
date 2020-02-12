import os
import subprocess
import tempfile

from contextlib import contextmanager


from util.paths import get_binary

FFMPEG = get_binary("ffmpeg")

def resample(infile, outfile, lang='en'):
    if not os.path.isfile(infile):
        raise IOError("Not a file: %s" % infile)

    '''
    Use FFMPEG to convert a media file to a wav file sampled at 8K
    '''
    if lang == 'en':
        return subprocess.call([FFMPEG,
                                '-loglevel', 'panic',
                                '-y',
                                '-i', infile,
                                '-ac', '1', '-ar', '8000',
                                '-acodec', 'pcm_s16le',
                                outfile])
    if lang == 'fr':
        return subprocess.call([FFMPEG,
                                '-loglevel', 'panic',
                                '-y',
                                '-i', infile,
                                '-ac', '1', '-ar', '16000',
                                '-acodec', 'pcm_s16le',
                                outfile])

@contextmanager
def resampled(infile, lang):
    with tempfile.NamedTemporaryFile(suffix='.wav') as fp:
        if resample(infile, fp.name, lang) != 0:
            raise RuntimeError("Unable to resample/encode '%s'" % infile)
        yield fp.name
