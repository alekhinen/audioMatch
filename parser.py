#AudioMG: MATCH GOOD!
# Header ::: TODO :::
# Parser module, adapts the OCore according to the CMD line

# -----------------------------------------------------------------------------
# imports
import argparse
import sys as SYS

# -----------------------------------------------------------------------------
# checkTag()
# checks a Tag and returns what the corresponding OCore should be set to.
def checkTag( tag ):
  result = -1

  if tag == '-f':
    result = 0
  elif tag == '-d':
    result = 1

  return result

# -----------------------------------------------------------------------------
# parse()
# parses the CMD line and changes the OCores flags accordingly
def parse( core ):
  result = core
  outputText = ''

  # pull args from command-line
  if ( len(SYS.argv) == 5 ):
    tag1 = SYS.argv[1]
    tag2 = SYS.argv[3]
    dir1 = SYS.argv[2]
    dir2 = SYS.argv[4]
  else:
    outputText = 'ERROR: exactly two paths have to be specified.'
    return result, outputText

  # check the tags and set the OCore accordingly
  m1 = checkTag(tag1)
  m2 = checkTag(tag2)

  if ( m1 == -1 or m2 == -1 ):
    outputText = 'ERROR: improper flagtype.'
  else:
    result['Mode1'] = checkTag(tag1)
    result['Mode2'] = checkTag(tag2)
    # update the directories
    result['A_Dir'] = dir1
    result['U_Dir'] = dir2

  # return the modified core object and output text.
  return result, outputText



