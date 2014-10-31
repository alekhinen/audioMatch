#AudioMG: MATCH GOOD!

#Processor Module: Processes files into fragmented FFT'd lists of numbers


import math
from scipy.fftpack import fft
from sndhdr import what
import scipy.io.wavfile as wavfile


# Extracts data and sampling rate from file
def process( fileName, core ):
  if ( core['Stage'] == 0 ):
    dirr = './tmp/User/'
  else:
    dirr = './tmp/Ads/'

  srate, data = wavfile.read( dirr + fileName )
  metadata = what( dirr + fileName )
  channels = metadata[2]

  if ( channels > 1 ):
    a = data.T[0]
  else:
    a = data.T
  # normalizing left-audio track over [-1, 1)
  # b = [ (e / 256)*2-1 for e in a ]
  b = []
  i = 0
  aLength = len(a)
  while (i < len(a)) and (i < 1000000):
    b.append( (a[i] / 256)*2-1 )
    i += 1
  #Setting up chunking process
  fragSize = srate*core['FSize']
  start = 0
  end = fragSize
  primList = []

  #Seperating the data into chunks of consistent audio length
  i = 0
  while (end < len(b) + fragSize):
    subList = []
    while (i < len(b) and i < end):
      subList.append(b[i])
      i += 1
    primList.append(subList)
    start = end
    end = end + fragSize

  result = []
  for e in primList:
    result.append(fft(e))
  return result






