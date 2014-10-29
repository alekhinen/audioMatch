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
      result = result and validateFile( f )

  return result

def validateFile( f ):
  # TODO check if f is mp3 or wav and is actually an mp3 or wav.



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

