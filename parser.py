from scipy.ndimage.filters import maximum_filter
import scipy.io.wavfile as wavfile
from scipy.fftpack import fft

def parseFiles(f1, f2):
  samp_rate1, data1 = wavfile.read( f1 )
  samp_rate2, data2 = wavfile.read( f2 )

  # d-1
  a = data1.T[0]
  # normalize on [-1,1)
  b = [ (e / 2**8)*2-1 for e in a ]
  # FFT (amplitude (unknown units) over frequency (Hz))
  c = fft(b)

  #d-2
  a2 = data2.T[0]
  # normalize on [-1,1)
  b2 = [ (e / 2**8)*2-1 for e in a2 ]
  # FFT (amplitude (unknown units) over frequency (Hz))
  c2 = fft(b2)

  return (c, c2)
