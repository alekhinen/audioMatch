#AudioMG: MATCH GOOD!
# Header ::: TODO :::
# Parser

import argparse
# from comparator import parseAndCompare
# from validator import validateFiles
import sys as SYS

# checks a Tag and returns what the corresponding OCore
#should be set to.
def checkTag( tag ):
  if tag == '-f':
    return 0
  elif tag == '-d':
    return 1
  else:
    print "ERROR: bad flag"

# parses the CMD line and changes the OCores flags accordingly
def parse( core ):
  result = core

  # pull args from command-line
  tag1 = SYS.argv[1]
  tag2 = SYS.argv[3]
  dir1 = SYS.argv[2]
  dir2 = SYS.argv[4]

  # check the tags and set the OCore accordingly
  result['Mode1'] = checkTag(tag1)
  result['Mode2'] = checkTag(tag2)
  # update the directories
  result['U_Dir'] = dir1
  result['U_Dir'] = dir2

  # return the modified core object
  return result



