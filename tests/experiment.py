import os.path
import subprocess

inputFile = './assets/D1.wav'
subprocess.call(['../vendor/lame', '--resample', '22.05', inputFile])

# CANONICAL
# set to wav
# resample to 22.05
# set bitrate to 16
# low-pass filter (50khz)
# high-pass filter (15,000 khz)
# set channel to mono

# FINGERPRINTS
# chunk every 4096 samples
# FFT each sample
# logarithmically bin each sample (add up amplitudes for each bin)
# frequency bins: (50, 100, 200, 400, 800, 1600, 3200, 6400, 12800)
# this creates a fingerprint (reduces into some constant set of bins)

# HASHING
# scales the bin values (real numbers (0 - ????)) to some small range
#   converts them into ints
# hash function: continuous function. 
#   (small constant * bin value) + (rest of bins * small constant)