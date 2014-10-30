#AudioMG: MATCH GOOD!

#The Adder module, moves all validated files to tmp folders
# and then adds them to the database.
from os import listdir
from os.path import isfile, join
from processor import process
from copyconvert import copyFile, convertFile
def add ( core ) :
  filesUser = [ i for i in listdir(core['U_Dir']) if isfile(i) ]
  core['Stage'] = 0
  # generates the list of user files to be added  
  for i in filesUser subAdd(i, core)


  


#Preforms individual additions.
def subAdd ( fieName, core ):
  copyFile(fileName, core )
  convertFile(fileName, core )
  data = process(fileName, core)
  core['DBase'].append(data)


