#AudioMG: MATCH GOOD!

#The Checker 
# checks files against the database. and compares them to matches

#Imports
from os import listdir
from os.path import isfile, join
from processor import process
from copyconvert import copyFile, convertFile
from comparator import compare

#Runs Subcheck on all files in A_Dir after setting the stage
def check ( core ) :
  #Sets the Stage to Ad mode
  core['Stage'] = 1
  filesAd = [ i for i in listdir(core['A_Dir']) if isfile(i) ]
  # generates the list of user files to be added 
  for i in filesAd subCheck(i, core)
  return core, ""
  
#Preforms individual checks.
def subCheck ( fieName, core ):
  copyFile(fileName)
  convertFile(fileName)
  compare(fileName, core, process(fileName, core))
  


