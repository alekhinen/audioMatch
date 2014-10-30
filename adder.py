#AudioMG: MATCH GOOD!

#The Adder module, moves all validated files to tmp folders
# and then adds them to the database.
from os import listdir
from os.path import isfile, join
from processor import process
from copyconvert import copyFile, convertFile
from sndhdr import what

# Adds all the files in the user directory to the tmp directory
# converts them and then adds them to the Database.
def add ( core ) :
  # Generates the list of files in the user directory
  filesUser = [ i for i in listdir(core['U_Dir']) if isfile(i) ]
  # Sets the stage to User Mode.
  core['Stage'] = 0
  # Adds the files via SubAdd 
  subAdd(i, core) for i in filesUser 
  return core, ""

#Preforms individual additions.
def subAdd ( fieName, core ):
  copyFile( fileName, core )
  if what("./tmp/User/" + fileName) == "mp3":
    convertFile( fileName, core )
  data = process( fileName, core )
  core['DBase'].append( data )


