#AudioMG
#PostProcessor 11/11/14

import math
def hCode( frag ):
  band1 = 300
  band2 = 1200
  band3 = 4000 
  bvalue = 0
  bvalue2 = 0
  bvalue3 = 0
  bvalue4 = 0  
  avalue = 0

  for i in range(len(frag)):
    if (i < band1):
      bvalue = bvalue + abs(frag[i])
      avalue = avalue + abs(frag[i])
    elif (i < band2):
      bvalue2 = bvalue2 + abs(frag[i])
      avalue = avalue + abs(frag[i])
    elif (i < band3):
      bvalue3 = bvalue3 + abs(frag[i])
      avalue = avalue + abs(frag[i])
    else:
      bvalue4 = bvalue4 + abs(frag[i])
      avalue = avalue + abs(frag[i])

return math.sqrt(bvalue**2 + bvalue2**2 + bvalue3**2 + bvalue4**2)

def addFragments( core ):
  for record in core.recDB.recordingsDB:
    for i in range(len(record.recordings[]))
      f = fragment(hCode(record.recordings[]), i)

