#AudioMG: MATCH GOOD!

#The Checker 
# checks files against the database. and compares them to matches

#Imports
from os import listdir
from os.path import isfile, join
from processor import process
from copyconvert import copyFile, convertFile

#Runs Subcheck on all files in A_Dir after setting the stage
def check ( core ) :
  core['Stage'] = 1
  filesAd = [ i for i in listdir(core['A_Dir']) if isfile(i) ]
  # generates the list of user files to be added 
  for i in filesAd subCheck(i, core)

#Compares a single dataBase entry against the given data
def subCompare( fileName, data, data2):

#Compares processed data og one Ad against the entire dataBase
def compare( fileName, core, data ):
  subCompare( fileName, data, i ) for i in core['DBase']


#Preforms individual checks.
def subCheck ( fieName, core ):
  copyFile(fileName)
  convertFile(fileName)
  compare(fileName, core, process(fileName, core))
  


