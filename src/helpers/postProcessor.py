#AudioMG
#PostProcessor 11/11/14

import math

def computeHash( frag ):
  boundaries = [30,150,500,2500]
  weights    = [1, 1, 1, 1]
  binValues  = [0 ,0, 0, 0]

  avalue = 0
  for dat in frag:
    avalue = avalue + abs(dat)
  avalue = float(1000/(avalue/len(frag)))

  j = 0
  for i in range(len(frag)):
    if (i >= boundaries[j]): 
      j += 1
    binValues[j] += int(abs(frag[i])*avalue)

  result = 0
  weightInterval = 0
  for el in binValues:
    result += weights[weightInterval] * el**2
    weightInterval += 1
  result = int( round( math.sqrt( result )))
  return result
