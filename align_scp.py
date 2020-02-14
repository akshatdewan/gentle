import argparse
import logging
import multiprocessing
import os
import sys

import gentle

parser = argparse.ArgumentParser(
        description='Align a transcript to audio by generating a new language model.  Outputs JSON')
parser.add_argument(
        '--nthreads', default=multiprocessing.cpu_count(), type=int,
        help='number of alignment threads')
parser.add_argument(
        '-o', '--output', metavar='output', type=str,
        help='output filename')
parser.add_argument(
        '--conservative', dest='conservative', action='store_true',
        help='conservative alignment')
parser.set_defaults(conservative=False)
parser.add_argument(
        '--disfluency', dest='disfluency', action='store_true',
        help='include disfluencies (uh, um) in alignment')
parser.set_defaults(disfluency=False)
parser.add_argument(
        '--log', default="INFO",
        help='the log level (DEBUG, INFO, WARNING, ERROR, or CRITICAL)')
#parser.add_argument(
#        'audiofile', type=str,
#        help='audio file')
#parser.add_argument(
#        'txtfile', type=str,
#        help='transcript text file')
parser.add_argument(
        'scpfile', type=str,
         help='script input file')
args = parser.parse_args()

log_level = args.log.upper()
logging.getLogger().setLevel(log_level)

disfluencies = set(['uh', 'um'])

def on_progress(p):
    for k,v in p.items():
        logging.debug("%s: %s" % (k, v))


with open(args.scpfile,'r') as f:
    scp = f.readlines()

resources = gentle.Resources()
#logging.info("converting audio to 8K sampled wav")

for item in scp:
    try:
        txtfile,audiofile = item.split()
        with open(txtfile) as fh:
            transcript = fh.read()

        with gentle.resampled(audiofile) as wavfile:
            logging.info("starting alignment for %s" % (audiofile))
            aligner = gentle.ForcedAligner(resources, transcript, nthreads=args.nthreads, disfluency=args.disfluency, conservative=args.conservative, disfluencies=disfluencies)
            result = aligner.transcribe(wavfile, progress_cb=on_progress, logging=logging)

        with open(txtfile+'.align.json', 'w') as fh:
            fh.write(result.to_json(indent=2))
        if args.output:
            logging.info("output written to %s" % (args.output))
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        logging.info("{} failed".format(txtfile))
        logging.info(message)
        continue
