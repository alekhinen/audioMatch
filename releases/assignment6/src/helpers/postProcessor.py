# @module: postProcessor
# @description: processes fft'd data.
# @version: 14-11-2014

# -----------------------------------------------------------------------------
# imports
import math


# -----------------------------------------------------------------------------
# mag()
# @description: calculates the magnitude of a given number
# @param: cnum - list of fragments
# @author: Michael Chadbourne
# @return: number
def mag( cnum ):
  return math.sqrt(cnum.real**2 + cnum.imag**2)


# -----------------------------------------------------------------------------
# computeHash()
# @description: calculates the hashvalue from an fft'd fragment
# @param: frag - a list of fft'd samples
# @author: Michael Chadbourne, Nick Alekhine
# @return: integer
def computeHash( frag ):
  boundaries = [20, 40, 80, 160, 320, 640, 1280]
  weights    = [0.25, 0.75, 1.1, 1.2, 1.1, .75, .25]
  binValues  = [0, 0, 0, 0, 0, 0, 0]


  avalue = 0
  maxMag = 0
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
