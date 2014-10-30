#AudioMG: MATCH GOOD!

#The Adder module, moves all validated files to tmp folders
# and then adds them to the database.
from os import listdir
from os.path import isfile, join
from processor import process
from copyconvert import copyFile, convertFile
from sndhdr import what
from os import makedirs
# Adds all the files in the user directory to the tmp directory
# converts them and then adds them to the Database.
def add ( core ) :
  mkdirs("./tmp/User/")
  mkdirs("./tmp/Ads/")
  # Generates the list of files in the user directory
  filesUser = []
  for i in listdir(core['U_Dir']):
    print '-------------------'
    print i, '\n'
    filesUser.append( i )

  # Sets the stage to User Mode.
  core['Stage'] = 0

  # Adds the files via SubAdd
  for i in filesUser:
    subAdd(i, core)

  return core, ''

#Preforms individual additions.
def subAdd ( fileName, core ):
  copyFile( fileName, core )
  if what("./tmp/User/" + fileName) == "mp3":
    convertFile( fileName, core )
  data = process( fileName, core )
  core['DBase'].append( data )


