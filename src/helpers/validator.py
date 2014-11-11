# AudioMG: MATCH GOOD!
#
# Validator!

# -----------------------------------------------------------------------------
# imports
import sys
import os, os.path
import glob
import sndhdr


# -----------------------------------------------------------------------------
# validate()
def validate( sysArgs ):
  isValid = True
  errMsg = ''

  # TODO: check if supplied is directory or file.
  if core.getUserMode() == 1:
    if core.getAdMode() == 1:
      isValid = os.path.isdir(core.getUserDir()) and os.path.isdir(core.getAdDir())
    elif core.getAdMode() == 0:
      isValid = os.path.isdir(core.getUserDir()) and os.path.isfile(core.getAdDir)
  elif core.getUserMode == 0:
    if core.getAdMode == 1:
      isValid = os.path.isfile(core.getUserDir()) and os.path.isdir(core.getAdDir())
    elif core.getAdMode() == 0:
      isValid = os.path.isfile(core.getUserDir()) and os.path.isfile(core.getAdDir())
  else:
    isValid = False

  if ( not isValid ):
    errMsg = 'ERROR: flagged a directory that was not a directory OR flagged a file that was not a file'

  return errMsg

  # check if the directories actually exist
  isValid = isValid and os.path.exists( core.getUserDir() )
  isValid = isValid and os.path.exists( core.getAdDir() )

  if ( not isValid ):
    errMsg = 'ERROR: Supplied pathname(s) does not exist.'

  return errMsg

  # if directories exist, validate all the files in each directories
  if ( isValid ):
    isValid = isValid and validateDir( core.getUserDir() )
    isValid = isValid and validateDir( core.getAdDir() )

  # if directories or files are not valid, update errMsg
  if ( not isValid ):
    errMsg = 'ERROR: Supplied file(s) are not valid.'

  return errMsg


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


