#!/usr/bin/env python
import argparse
from comparator import parseAndCompare
from validator import validateFiles

parser = argparse.ArgumentParser()
parser.add_argument('file1', help='include a file')
parser.add_argument('file2', help='include a second file')
args = parser.parse_args()

if ( validateFiles( args.file1, args.file2 )):
  parseAndCompare( args.file1, args.file2 )


# Shell script so that we can do this: dan -f z01.wav -f z02.wav
# Validation of user inputs
# Parse the inputted files (fourier transform -> ???)
# Comparison
# Output
