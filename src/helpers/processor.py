# @module: processor
# @description: processes files into fragmented FFT'd lists of numbers.
#               collects metadata.
# @version: 31-10-2014

# -----------------------------------------------------------------------------
# imports
import math
import os.path
import scipy.io.wavfile as wavfile
from scipy.fftpack import fft
from sndhdr        import what

# COMMENTS TO DEVELOPER
# TODO: normalization and fft'ing the track take way too long
# see line 51 and line 63 onward for where things could be improved.


# -----------------------------------------------------------------------------
# process()
# @description: collects metadata and FFT's audio file
# @returns: dictionary with FFT and metadata
def process( filepath ):
  # initialize result
  result = []
  
  samplingRate, data = wavfile.read( filepath )
  # collect metadata
  metadata = what( filepath )
  bitsPerSamp = metadata[4]

  # get audio track data
  a = data.T

  # normalize audio track over [-1, 1)
  b = []
  i = 0
  aLength = len(a)
  # either hit 800 thousand iterations or go through entire data set.
  while (i < aLength):
    b.append( (a[i] / 256)*2-1 )
    i += 1

  #Setting up chunking process
  fragSize = samplingRate * 2.5
  start    = 0
  end      = fragSize
  primList = []

  # separating the data into chunks of consistent audio length
  i = 0
  bLength = len(b)
  while (end < bLength + fragSize):
    subList = []
    while (i < bLength and i < end):
      subList.append(b[i])
      i += 1
    for i in subList:
      primList.append(i)
    start = end
    end = end + fragSize

  for e in primList:
   if ( e.size % 2 == 0 ):
     result.append( fft(e) )

  # update result
  
  print result
  return result






