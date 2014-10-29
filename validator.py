# AudioMG: MATCH GOOD!
#
# Validator!

# -----------------------------------------------------------------------------
# imports
import os, os.path
import glob
import sndhdr


# -----------------------------------------------------------------------------
# validate()
def validate( OCore ):
  isValid = True
  outputText = ''

  # check if the directories actually exist
  isValid = isValid and os.path.exists( OCore['U_Dir'] )
  isValid = isValid and os.path.exists( OCore['A_Dir'] )

  # if directories exist, validate all the files in each directories
  if ( isValid ):
    isValid = isValid and validateDirFiles( OCore['U_Dir'] )
    isValid = isValid and validateDirFiles( OCore['A_Dir'] )

  # if directories or files are not valid, update outputText
  if ( not isValid ):
    outputText = 'ERROR: Some files are not valid.'

  return OCore, outputText


def validateDirFiles( dirPath ):
  result = True

  for subdir, dirs, files in os.walk( dirPath ):
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
    # TODO: parse this.
    os.system('file %s' % f )
    isValid = True

  return isValid


# -----------------------------------------------------------------------------
# OLD SHIT
# #Validates the given file, in the directory signified by dirr
# def Validate( core, f1, dirr ):
#   #f1 is the file name as a string
#   #dirr is 0 for the U_dir 1 for the A_Dir
#   if dirr == 0:  #may need backslash safety
#     full_dir = core['A_Dir'] + f1
#   elif dirr == 1:
#     full_dir = core['U_Dir'] + f1
#   else:
#     print "ERROR invalid core dir"

#   if ( not (os.path.isfile( full_dir))):
#     print "ERROR bad path name"

#   form = sndhdr.what(full_dir)
#   if form == 'wav':
#     #TODO
#   elif form == 'mp3':
#     #TODO
#   else:
#     print "ERROR unsupported format"


# def ValidateAll( core ):
#   #TODO a extra edit here

