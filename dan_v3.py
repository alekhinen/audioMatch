import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile
from scipy.fftpack import fft
import numpy as np

sampling_rate, data = wavfile.read('audio/z01.wav')

channel_1 = data.T[0] # first track
channel_2 = data.T[1] # second track

def stereo_to_mono_conversion(c1, c2):
  result = [];
  for i in range(0, len(c1) / 100):
    # print c1[i], c2[i]
    # print ((c1[i] + c2[i]) / 2)
    # print '---------------------'
    result.append( ((c1[i] + c2[i]) / 2) )
  result = np.array(result);
  return result

mono_audio = stereo_to_mono_conversion(channel_1, channel_2)

b = [(ele/2**8.)*2-1 for ele in mono_audio] # this is 8-bit track, b is now normalized on [-1,1)
c = fft(b) # create a list of complex number
d = len(c) / 2    # you only need half of the fft list
plt.plot(abs(c[:(d-1)]),'r')
plt.show()
