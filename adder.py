#AudioMG: MATCH GOOD!

#The Adder module, moves all validated files to tmp folders
# and then adds them to the database.
from os import listdir
from os.path import isfile, join
from processor import process

def add ( core ) :
  filesUser = [ i for i in listdir(core['U_Dir']) if isfile(i) ]
  # generates the list of user files to be added  
  for i in filesUser subAdd(i, core)

def copyFile ( fileName ):
  
def convertFile ( fileName ):

#Preforms individual additions.
def subAdd ( fieName, core ):
  copyFile(fileName)
  convertFile(fileName)
  data = process(fileName, core)
  core['DBase'].append(data)


