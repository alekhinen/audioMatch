# AudioMG: MATCH GOOD!
#
# Validator!

import os.path
import sndhdr

#Validates the given file, in the directory signified by dirr
def Validate( core, f1, dirr ):
  #f1 is the file name as a string
  #dirr is 0 for the U_dir 1 for the A_Dir
  if dirr == 0:  #may need backslash safety
    full_dir = core['A_Dir'] + f1
  elif dirr == 1:
    full_dir = core['U_Dir'] + f1
  else:
    print "ERROR invalid core dir"

  if ( not (os.path.isfile( full_dir))):
    print "ERROR bad path name"

  form = sndhdr.what(full_dir)
  if (form == 'wav'):
    #TODO
  elif (form == 'mp3'):
    #TODO
  else:
    print "ERROR unsupported format"


def ValidateAll( core ): 
  #TODO a extra edit here
  
