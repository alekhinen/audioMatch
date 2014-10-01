import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile
from scipy.fftpack import fft

def parseFiles(f1, f2):
  samp_rate1, data1 = wavfile.read( f1 )
  samp_rate2, data2 = wavfile.read( f2 )

  ### data1 ####
  a = data1.T[0] # two channel soundtrack; get the first track
  b = [ (e/2**8)*2-1 for e in a] # this is 8-bit track, b is now normalized on [-1,1)
  c = fft(b) # create a list of complex number
  d = len(c) / 2    # you only need half of the fft list
  # plt.plot(abs(c[:(d-1)]),'r')
  # plt.show()

  ### data2 ####
  a2 = data2.T[0]
  b2 = [ (e / 2**8)*2 - 1 for e in a2 ]
  c2 = fft(b2)
  d2 = len(c2) / 2

  return (c, c2)
