#AudioMG
#PostProcessor 11/11/14

import math

def mag (cnum):
  return math.sqrt(cnum.real**2 + cnum.imag**2)

def computeHash( frag ):
  #boundaries = [30,150,500,2500]
  #weights    = [1, 1, 1, 1]
  #binValues  = [0 ,0, 0, 0]
#2.0
#  boundaries = [28, 47, 84, 149, 233, 396, 745, 1050]
  boundaries = [20, 40, 80, 160, 320, 640, 1280]
  weights    = [1, 1, 1, 1, 1, 1, 1]
  binValues  = [0, 0, 0, 0, 0, 0, 0]


  avalue = 0
  for dat in frag:
    avalue = avalue + mag(dat)
  avalue = float(100/(avalue/len(frag)))

  j = 0
  for i in range(len(frag)):
    if (i >= boundaries[j]): 
      j += 1
    binValues[j] += int(mag(frag[i])*avalue)

  result = 0
  weightInterval = 0
  for el in binValues:
    result += weights[weightInterval] * el**2
    weightInterval += 1
  result = int( round( math.sqrt( result )))
  return result
