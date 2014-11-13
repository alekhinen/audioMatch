#AudioMG
#PostProcessor 11/11/14

import math
def computeHash( frag ):
  band1 = 31
  band2 = 150
  band3 = 500 
  bvalue = 0
  bvalue2 = 0
  bvalue3 = 0
  bvalue4 = 0  
  avalue = 0
  
  for dat in frag:
    avalue = avalue + abs(dat)
  avalue = float(1000/(avalue/len(frag)))
  


  for i in range(len(frag)):
    if (i < band1):
      bvalue = bvalue + int(abs(frag[i])*avalue)
    elif (i < band2):
      bvalue2 = bvalue2 + int(abs(frag[i])*avalue)
    elif (i < band3):
      bvalue3 = bvalue3 + int(abs(frag[i])*avalue)
    else:
      bvalue4 = bvalue4 + int(abs(frag[i])*avalue)

  return int( round( math.sqrt(bvalue**2 + bvalue2**2 + bvalue3**2 + bvalue4**2)))

