# AudioMG: MATCH GOOD!
# @module: adder
# @description: The Adder module, moves all validated files to tmp folders
#               and then adds them to the database.

# -----------------------------------------------------------------------------
# imports
from os          import listdir
from os.path     import isfile, join
from processor   import process
from copyconvert import copyFile, convertFile
from sndhdr      import what
from os          import makedirs

# -----------------------------------------------------------------------------
# add()
# @description: Adds all the files in the user directory to the tmp directory
#               converts them and then adds them to the Database.
def add( core ):
  result = core

  # generate directories
  makedirs('./tmp/User/')
  makedirs('./tmp/Ads/')

  # sets the stage to user mode.
  result['Stage'] = 0

  # adds fft data from tmp/user audio files via subAdd()
  for i in listdir(result['U_Dir']):
    result['database']['user'].append( subAdd(i, result) )

  # sets the stage to advertisement mode.
  result['Stage'] = 1

  # adds fft data from tmp/Ads audio files via subAdd()
  for i in listdir(result['A_Dir']):
    result['database']['advertisements'].append( subAdd(i, result) )

  return result, ''

# -----------------------------------------------------------------------------
# subAdd()
# @description: copies over file, converts that file, fft's that file
# @return: fft'd audio data
def subAdd( fileName, core ):
  # if we are in user stage
  if ( core['Stage'] == 0 ):
    fullFile = os.path.join( core['U_Dir'], fileName )
    # if file is mp3, convert it
    if ( what( fullFile ) == 'mp3' ):
      convertFile( fileName, core )
    # else, just copy it over
    else:
      copyFile( fileName, core )
    data = process( fileName, core )
    return data
  # else we are in ad stage
  else:
    fullFile = os.path.join( core['A_Dir'], fileName )
    # if file is mp3, convert it
    if ( what( fullFile ) == 'mp3' ):
      convertFile( fileName, core )
    # else, just copy it over
    else:
      copyFile( fileName, core )
    data = process( fileName, core )
    return data


