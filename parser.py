#AudioMG: MATCH GOOD!
# Header ::: TODO :::
# Parser

import argparse
from comparator import parseAndCompare
from validator import validateFiles
import sys as SYS

# checks a Tag and returns what the corresponding OCore
#should be set to.
def checkTag( tag ):
  if tag == '-f':
    return 0
  elif tag == '-d'
    return 1
  else:
    print "ERROR: bad flag" 
# Parses the CMD line and changes the OCores flags accordingly
def parse( core ):
  tag1 = SYS.argv[1]
  tag2 = SYS.argv[3]
  dir1 = SYS.argv[2]
  dir2 = SYS.argv[4]
  #Check the tags and set the OCore accordingly
  core['Mode1'] = checkTag(tag1)
  core['Mode2'] = checkTag(tag2)
  #Update the directories
  core['U_Dir'] = dir1
  core['U_Dir'] = dir2
  
  

