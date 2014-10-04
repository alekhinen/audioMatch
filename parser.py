import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from scipy.ndimage.filters import maximum_filter
import scipy.io.wavfile as wavfile
from scipy.fftpack import fft

# def parseFiles(f1, f2):
#   samp_rate1, data1 = wavfile.read( f1 )
#   samp_rate2, data2 = wavfile.read( f2 )

#   ### data1 ####
#   a = data1.T[0] # two channel soundtrack; get the first track
#   # b = [ (e/2**8)*2-1 for e in a] # this is 8-bit track, b is now normalized on [-1,1)
#   # c = fft(b) # create a list of complex number
#   # d = len(c) / 2    # you only need half of the fft list
#   # plt.plot(abs(c[:(d-1)]),'r')
#   # plt.show()

#   # specgram(1D array of samples, window size, sampling rate, window, overlap)
#   c = mlab.specgram(a, 4096, 44100, window=mlab.window_hanning, noverlap=int(4096 * 0))[0]

#   # get indices for frequency and time
#   frequency_idx = [x[1] for x in c]
#   time_idx = [x[0] for x in c]

#   fig, ax = plt.subplots()
#   ax.imshow(c)
#   ax.scatter(time_idx, frequency_idx)
#   ax.set_xlabel('Time')
#   ax.set_ylabel('Frequency')
#   ax.set_title("Spectrogram")
#   plt.gca().invert_yaxis()
#   plt.show()

#   for el in c:
#     print el

#   # GET THE PEAKS




#   ### data2 ####
#   a2 = data2.T[0]
#   # b2 = [ (e / 2**8)*2 - 1 for e in a2 ]
#   # c2 = fft(b2)
#   # d2 = len(c2) / 2

#   # specgram(1D array of samples, window size, sampling rate, window, overlap)
#   c2 = mlab.specgram(a2, 4096, 44100, window=mlab.window_hanning, noverlap=int(4096 * 0))[0]

#   # GET THE PEAKS


#   return (c, c2)

def parseFiles(f1, f2):
  samp_rate1, data1 = wavfile.read( f1 )
  samp_rate2, data2 = wavfile.read( f2 )

  # d-1
  a = data1.T[0]
  # normalize on [-1,1)
  b = [ (e / 2**8)*2-1 for e in a ]
  # FFT (amplitude (unknown units) over frequency (Hz))
  c = fft(b)

  d = len(c) / 2

  plt.plot(abs(c[:(d-1)]),'r')
  plt.show()


  #d-2
  a2 = data2.T[0]
  # normalize on [-1,1)
  b2 = [ (e / 2**8)*2-1 for e in a2 ]
  # FFT (amplitude (unknown units) over frequency (Hz))
  c2 = fft(b2)

  return (c, c2)
