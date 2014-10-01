#!/usr/bin/env python
import argparse
from dan_v2 import compareFiles

parser = argparse.ArgumentParser()
parser.add_argument('file1', help='include a file')
parser.add_argument('file2', help='include a second file')
args = parser.parse_args()

compareFiles( args.file1, args.file2 )
