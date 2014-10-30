#AudioMG: MATCH GOOD!

#Processor Module:

import math
from scipy.fftpack import fft


# Extracts data and sampling rate from file
def process( fileName, core ):
  if ( core['Stage'] == 0 ):
    dirr = "./tmp/User/"
  else:
    dirr = "./tmp/Ads/"

  srate, data = wavefile.read( dirr + fileName )

  a = data.T[0]
  b = [(e / 256)*2-1 for e in a ]
  #Setting up chunking process
  fragSize = srate*core['Fsize']
  start = 0
  end = fragSize
  primList = []

  #Seperating the data into chunks of consistent audio length
  i = 0
  while (end < len(b) + fragSize):
    subList = []
    while (i < len(b) and i < end):
      subList.append(b[i])
      i++
    primList.append(subList)
    start = end
    end = end + fragSize
  
 return for e in primList fft(e)
	
 
  




