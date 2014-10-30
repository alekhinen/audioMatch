# AudioMG: MATCH GOOD!

# The Comparator Module: Compares segments in the check phase

#Imports:
from os import listdir

def subCompare( fileName, core, data, fileNameU, index ):
  # i must be a List of fragments(Ordered Lists of floats)
  for i in core['DBase'][index]:
    if 

#Compares the Given data fro given fileName against all data in the database.
def compare( fileName, core, data ):
  j = 0
  for i in listdir("./tmp/User/"): 
    subCompare(fileName, core, data, i, j )
    j = j + 1

