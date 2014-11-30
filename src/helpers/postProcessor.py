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
# @Theta: (2)fragmentSize+10
def computeHash( frag ):

  # The upper-bounds for each band, binned logarithmically 
  boundaries = [20, 40, 80, 160, 320, 640, 1280]
  # The Weights applied to the other-wise euclidian distance function
  # Selected to highlight changes which occur in the relevant bands
  # While dampening the non-critical bands
  weights    = [0.25, 0.75, 1.1, 1.2, 1.1, .75, .25]
  # The Value in each band, initially should all be Zero
  binValues  = [0, 0, 0, 0, 0, 0, 0]
  
  magFrag = map(mag, frag)
  avalue = 0 #The Mean Value, used for magnitude normalizeation
  #for dat in frag:
  #  avalue += mag(dat)
  avalue = sum(magFrag)
  #Once all magnitudes have been summed, divide by total fragments
  #and multiply by 100 (an arbitrary constant)
  avalue = float(10/(avalue/len(frag)))

  band = 0 #The Index of the band being scanned
  for i in range(len(frag)): #For each data point in the fragment
    if (i >= boundaries[band]): #Check if the band changed
      band += 1
    binValues[band] += int(magFrag[i]*avalue) #Add to the current band

  result = 0  #Holder for the result as it is summed
  weightInterval = 0 #The index of the band, used to get its weight
  # Applies a weighed-euclidian distance function to the 
  # 7 Dimensional space created by the bands
  for el in binValues:
    result += weights[weightInterval] * el**2
    weightInterval += 1
  result = int(round(math.sqrt(result)))

  return result
