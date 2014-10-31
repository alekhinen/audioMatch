#AudioMG: MATCH GOOD!
# Header ::: TODO :::
# Parser module, adapts the OCore according to the CMD line

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
# parses the CLI and changes OCore's modes and directories accordingly
def parse( core, sysArgs ):
  result = core
  outputText = ''

  # pull args from command-line
  if ( len(sysArgs) == 5 ):
    tag1 = sysArgs[1]
    tag2 = sysArgs[3]
    dir1 = sysArgs[2]
    dir2 = sysArgs[4]
  else:
    outputText = 'ERROR: Exactly two sets of flags and paths have to be specified.'
    return result, outputText

  # check the tags and set the OCore accordingly
  m1 = checkTag(tag1)
  m2 = checkTag(tag2)

  if ( m1 == -1 or m2 == -1 ):
    outputText = 'ERROR: improper flagtype supplied.'
  else:
    result['Mode1'] = checkTag(tag1)
    result['Mode2'] = checkTag(tag2)
    # update the directories
    result['U_Dir'] = dir1
    result['A_Dir'] = dir2

  # return the modified core object and output text.
  return result, outputText



