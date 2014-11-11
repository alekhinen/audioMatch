# AudioMG: MATCH GOOD!
#
# Validator!

# -----------------------------------------------------------------------------
# IMPORTS 
# -----------------------------------------------------------------------------

import sys
import os.path as path
import os, os.path
import glob
import sndhdr

# -----------------------------------------------------------------------------
# METHODS 
# -----------------------------------------------------------------------------

# isValid()
# @param: parsedArgs - an array, e.g. [userMode, userDir, adMode, adDir]
# @description: validates parsed arguments
# @returns: boolean value for validity
# @throws: SystemExit if invalid parsed arguments
# @author: Nick Alekhine, Charles Perrone
# @version: 11-11-2014
def isValid( pArgs ):
  isValid = True

  # check if the directories actually exist
  isValid = isValid and os.path.exists( pArgs[1] )
  isValid = isValid and os.path.exists( pArgs[3] )

  if ( not isValid ):
    print 'ERROR: Supplied pathname(s) does not exist.'
    sys.exit(3)

  # check if supplied directories follow the format of the modes
  if pArgs[0] == 1:
    if pArgs[2] == 1:
      isValid = path.isdir( pArgs[1] ) and path.isdir( pArgs[3] )
    elif pArgs[2] == 0:
      isValid = path.isdir( pArgs[1] ) and path.isfile( pArgs[3] )
  elif pArgs[0] == 0:
    if pArgs[2] == 1:
      isValid = os.path.isfile( pArgs[1] ) and os.path.isdir( pArgs[3] )
    elif pArgs[2] == 0:
      isValid = os.path.isfile( pArgs[1] ) and os.path.isfile( pArgs[3] )
  else:
    isValid = False

  if ( not isValid ):
    print 'ERROR: flagged a dir that\'s not a dir OR flagged a file that\'s not a file'
    sys.exit(4)

  # if directories exist, validate all the files in each directories
  if ( isValid ):
    # validation for users directory
    if ( pArgs[0] == 0 ):
      isValid = isValid and validateFile( pArgs[1] )
    elif ( pArgs[0] == 1 ):
      isValid = isValid and validateDir( pArgs[1] )
    # validation for ads directory
    if ( pArgs[3] == 0 ):
      isValid = isValid and validateFile( pArgs[3] )
    elif( pArgs[3] == 1 ):
      isValid = isValid and validateDir( pArgs[3] )

  # if directories or files are not valid, update errMsg
  if ( not isValid ):
    print 'ERROR: Supplied file(s) are not valid.'
    sys.exit(5)

  return isValid



def validateDir( dirPath ):
  result = False

  for subdir, dirs, files in os.walk( dirPath ):
    if ( files ):
      result = True
    for f in files:
      f = os.path.join( dirPath, f )
      result = result and validateFile( f )

  return result


def validateFile( f ):
  isValid = False

  # if file is a .wav
  if f.endswith('.wav'):
    #kind of file
    kind = sndhdr.what( f )[0]
    isValidKind = kind == 'wav'

    #sample rate
    sampRate = sndhdr.what( f )[1]
    isValidSample = (sampRate == 44100
      or sampRate == 11025
      or sampRate == 22050
      or sampRate == 48000)

    #number of channels (mono or stereo)
    numChan = sndhdr.what( f )[2]
    isValidChan = numChan == 1 or numChan == 2

    #bit rate
    bitRate = sndhdr.what( f )[4]
    isValidBitRate = bitRate == 8 or bitRate == 16

    isValid = (isValidKind
      and isValidSample
      and isValidChan
      and isValidBitRate)

  # if file is a .mp3
  elif f.endswith('.mp3'):
    # TODO: read this
    # https://stackoverflow.com/questions/3503879/assign-output-of-os-system-to-a-variable-and-prevent-it-from-being-displayed-on
    fMeta = os.popen('file %s' % f ).read()
    # check if it is 'MPEG'
    isValid = 'MPEG' in fMeta
    # check if it is 'layer III'
    isValid = isValid and 'layer III' in fMeta
    # check if it is 'v1'
    isValid = isValid and 'v1' in fMeta

  return isValid


