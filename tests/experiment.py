import os.path
import subprocess

# TEST 1 (z03)
inputFile = './assets/D1/z03.wav'
outputFile = './assets/D1_modified/z03.mp3'
outputFile2 = './assets/D1_modified/z03_decoded.wav'
subprocess.call(['../vendor/lame', '-a', inputFile, outputFile])
subprocess.call(['../vendor/lame', '--resample', '8.192', outputFile])
subprocess.call(['../vendor/lame', '--decode', outputFile + '.mp3', outputFile2 ])

# TEST 2 (rimsky)
inputFile = './assets/D1/rimsky.mp3'
outputFile = './assets/D1_modified/rimsky.mp3'
outputFile2 = './assets/D1_modified/rimsky_decoded.wav'
subprocess.call(['../vendor/lame', '-a', inputFile, outputFile])
subprocess.call(['../vendor/lame', '--resample', '8.192', outputFile])
subprocess.call(['../vendor/lame', '--decode', outputFile + '.mp3', outputFile2])

# TEST 3 (WhoopeeTiYiYo)
inputFile = './assets/D1/WhoopeeTiYiYo.mp3'
outputFile ='./assets/D1_modified/WhoopeeTiYiYo.mp3'
outputFile2 = './assets/D1_modified/WhoopeeTiYiYo.wav'
subprocess.call(['../vendor/lame', '-a', inputFile, outputFile])
subprocess.call(['../vendor/lame', '--resample', '8.192', outputFile])
subprocess.call(['../vendor/lame', '--decode', outputFile + '.mp3', outputFile2])


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
