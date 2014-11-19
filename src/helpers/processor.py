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


# -----------------------------------------------------------------------------
# process()
# @description: collects metadata and FFT's audio file
# @returns: dictionary with FFT and metadata
# @Theta: A(L+Llog(L)+computeHash(L)+5) 
#   Where A = amount of Fragments; L = length of fragment
def process( filepath, rec_id, chunkSize ):
  # read the file
  samplingRate, data = wavfile.read( filepath )
  # get audio track data (mono)
  a = data.T
  # get length of amount of samples
  aLength = len(a)

  # setting up chunking process
  fragmentSize = int(samplingRate * chunkSize)
  amtFragments = 2 * math.floor(aLength / fragmentSize) - 1
   # doubled for overlap
  fragments    = []
  
  #positions are held a fragment size apart from eachother throughout
  start = 0  # Holder for the start position of the current fragment
  end = fragmentSize #Holder for the end position in the full file
  i = 0
  window = signal.hamming(fragmentSize)
  # go through each chunk
  while ( i < amtFragments ):
    j = start # j tracks the offset in the full file
    rawData = [] # Holder for the data before its processed
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
    fragment = Fragment( rec_id, hashValue, i * (chunkSize/2) )
    # add to list of fragments
    fragments.append( fragment )

    # increment! to create overlapping fragments
    start += fragmentSize/2 # Both start and end now increment by
    end += fragmentSize/2   # only half a fragment length at a time
    i += 1                  

  return fragments








