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
  result = {
    'filename': os.path.basename(filepath),
    'fileExtension': os.path.basename(filepath).split('.')[1],
    'samplingRate': 0,
    'channels': 0,
    'bitsPerSamp': 0,
    'fft': []
  }

  samplingRate, data = wavfile.read( filepath )
  # collect metadata
  metadata = what( filepath )
  channels = metadata[2]
  bitsPerSamp = metadata[4]

  # get audio track data
  if ( channels > 1 ):
    a = data.T[0]
  else:
    a = data.T

  # normalize audio track over [-1, 1)
  b = []
  i = 0
  aLength = len(a)
  # either hit 800 thousand iterations or go through entire data set.
  while (i < aLength) and (i < 800000):
    b.append( (a[i] / 256)*2-1 )
    i += 1

  #Setting up chunking process
  fragSize = samplingRate * 2.5
  start    = 0
  end      = fragSize
  primList = []

  # separating the data into chunks of consistent audio length
  i = 0
  while (end < len(b) + fragSize):
    subList = []
    while (i < len(b) and i < end):
      subList.append(b[i])
      i += 1
    primList.append(subList)
    start = end
    end = end + fragSize

  for e in primList:
    result['fft'].append(fft(e))

  # update result
  result['samplingRate'] = samplingRate
  result['channels'] = channels
  result['bitsPerSamp'] = bitsPerSamp

  return result






