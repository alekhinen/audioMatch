# @module: comparator
# @description: compares segments in the check phase.
# @version: 13-11-2014

# -----------------------------------------------------------------------------
# imports
from os import listdir
from math import fabs as absval

# -----------------------------------------------------------------------------
# compare()
# @description: compares the user data against advertiser data
# @assumption: data comes as a list of fragments
# @param userData - list of fragments
# @param adData   - list of fragments
# @param threshold - an integer
# @author Zig
# @returns boolean
def compare( userData, adData, threshold ):
  i = 0
  j = 0
  z = 0
  while ( i < 40 and z <= 1 and j < len(userData) and j < len(adData) ):
    if ( absval( userData[j].hash() - adData[j].hash() ) < threshold ):
      i += 1
      j += 1
    else:
      z += 1
      #return False
  if i == 40:
    return True 
  else: 
    return False
  




