#AudioMG: MATCH GOOD!
# Header ::: TODO :::
# Parser module, adapts the OCore according to the CMD line

# -----------------------------------------------------------------------------
# IMPORTS
# -----------------------------------------------------------------------------

import sys

# -----------------------------------------------------------------------------
# METHODS
# -----------------------------------------------------------------------------

# checkFlag()
# @param: flag - a string
# @description: checks a flag for correctness (either -f or -d)
# @returns: an int of either: 0, 1, -1
# @author: Nick Alekhine
# @version: 10-11-2014
def checkFlag( flag ):
  result = -1

  if flag == '-f':
    result = 0
  elif flag == '-d':
    result = 1

  return result

# parse()
# @param: sysArgs - system arguments from CLI
# @description: parses the CLI and returns modes and directories accordingly
# @returns: an array
# @author: Nick Alekhine, Michael Chadbourne, Charles Perrone
# @version: 10-11-2014
def parse( sysArgs ):
  result = []

  # pull args from command-line
  if ( len(sysArgs) == 5 ):
    flag1 = sysArgs[1]
    flag2 = sysArgs[3]
    dir1  = sysArgs[2]
    dir2  = sysArgs[4]
  else:
    print 'ERROR: Exactly two sets of flags and paths have to be specified.'
    sys.exit(1)

  # check the flags
  flag1 = checkFlag(flag1)
  flag2 = checkFlag(flag2)

  if ( flag1 == -1 or flag2 == -1 ):
    print 'ERROR: improper flagtype supplied.'
    sys.exit(2)
  else:
    result = [ flag1, dir1, flag2, dir2 ]
    
  return result


