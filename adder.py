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

  # TODO: unnecessary
  # # generates the list of files in the user directory
  # filesUser = []
  # for i in listdir(result['U_Dir']):
  #   filesUser.append( i )

  # sets the stage to user mode.
  result['Stage'] = 0

  # adds fft data from tmp/user audio files via subAdd()
  for i in listdir(result['U_Dir']):
    result['database']['user'].append( subAdd(i, result) )

  # adds fft data from tmp/Ads audio files via subAdd()
  for i in listdir(result['A_Dir']):
    result['database']['advertisements'].append( subAdd(i, result) )

  return result, ''

# -----------------------------------------------------------------------------
# subAdd()
# @description: convert supplied file, fft that file
# @return: fft'd audio data
def subAdd( fileName, core ):
  copyFile( fileName, core )
  if ( what('./tmp/User/' + fileName) == 'mp3' ):
    convertFile( fileName, core )
  data = process( fileName, core )
  return data


