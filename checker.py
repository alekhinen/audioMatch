#AudioMG: MATCH GOOD!

#The Checker 
# checks files against the database.
from os import listdir
from os.path import isfile, join
from processor import process

def check ( core ) :
  filesAd = [ i for i in listdir(core['A_Dir']) if isfile(i) ]
  # generates the list of user files to be added 
  for i in filesAd subCheck(i, core)

#Preforms individual additions.
def subCheck ( fieName, core ):
  copyFile(fileName)
  convertFile(fileName)
  process(fileName, core)
  
def compare ():


