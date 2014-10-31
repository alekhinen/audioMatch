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
  # generate directories
  makedirs('./tmp/User/')
  makedirs('./tmp/Ads/')

  # generates the list of files in the user directory
  filesUser = []
  for i in listdir(core['U_Dir']):
    filesUser.append( i )

  # sets the stage to user mode.
  core['Stage'] = 0

  # adds the files via SubAdd()
  for i in filesUser:
    subAdd(i, core)

  return core, ''

# -----------------------------------------------------------------------------
# add()
# @description: Performs individual additions.
def subAdd( fileName, core ):
  copyFile( fileName, core )
  if ( what('./tmp/User/' + fileName) == 'mp3' ):
    convertFile( fileName, core )
  data = process( fileName, core )
  core['DBase'].append( data )


