# AudioMG: MATCH GOOD!

# The Comparator Module: Compares segments in the check phase

#Imports:
from os import listdir
from math import fabs as absval

#def subCompare( fileName, core, data, fileNameU, index ):
 # iDat = 0
  # i must be a List of fragments(Ordered Lists of floats)
 # for uFrag in core['DBase'][index]: #For each fragment in User
 #   aFrag = data[iDat]          #Grab corresponding frag from Ad data
 #   iDat = iDat + 1
    #compare number to number against threshold
    
 #   eCount = 0 #Allows for some bits to be allowed togo horribly wrong
 #   fCount = 0 #Allows accuracy to be maintained in the face of eCount
 #   for index in range(0, len(i)):
 #     anum1 = absval(uFrag[index].real)
 #     anum2 = absval(aFrag[index].real)
 #     if (core['Threshold'] < math.absval(anum1 - anum2)):
 #       eCount = eCount + 1
 #       fCount = 0
 #     else:           # Ends when 5bits dont match in an area without 10
 #       fCount = fCount + 1   #matching bits in a row
 #     if eCount >= 5: # change here to add or reduce err.bits allowed
 #       return "test"#No Match
 #     elif fCount >= 10: #change here to alter err.reset sensitivity
 #       eCount = 0   
  #For Loop Completion Indicates thorough match
#  return "MATCH " + fileName + fileNameU 
  
#Compares the Given data fro given fileName against all data in the database.
def compare(userData, adData):
  i = 0
  j = 0
  while ( i < 5 and j < len(userData)):
    if (userData[j].hash() == adData[j].hash()):
      i += 1
      j += 1
    else:
      return False
  if i == 5:
    return True 
  else: 
    return False
  




