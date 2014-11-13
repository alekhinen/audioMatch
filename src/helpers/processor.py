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
import postProcessor
import sys
sys.path.append('../')
from recordings.fragment import Fragment
import scipy.signal as signal

# COMMENTS TO DEVELOPER
# TODO: normalization and fft'ing the track take way too long
# see line 51 and line 63 onward for where things could be improved.


# -----------------------------------------------------------------------------
# process()
# @description: collects metadata and FFT's audio file
# @returns: dictionary with FFT and metadata
def process( filepath, rec_id, chunkSize ):
  # read the file
  samplingRate, data = wavfile.read( filepath )
  # get audio track data (mono)
  a = data.T
  # get length of amount of samples
  aLength = len(a)

  # setting up chunking process
  fragmentSize = int(samplingRate * chunkSize)
  amtFragments = math.floor( aLength / fragmentSize )
  fragments    = []
  

  start = 0
  end = fragmentSize
  i = 0
  # go through each chunk
  while ( i < amtFragments ):
    j = start
    rawData = []
    window = signal.hamming(fragmentSize)
    # go through each sample in chunk
    while ( j <= end ):
      # normalize sample on [-1, 1)
      normalizedSample = (a[j] / 256)*2-1
      # add to rawData
      rawData.append( normalizedSample )
      # increment j
      j += 1
    # process raw data
    processedData = fft( rawData )
    # compute hash of processed data
    hashValue = postProcessor.computeHash(processedData)
    # create a fragment
    fragment = Fragment( rec_id, hashValue, i * chunkSize )
    # add to list of fragments
    fragments.append( fragment )

    # increment!
    start = end
    end += fragmentSize
    i += 1

  return fragments






