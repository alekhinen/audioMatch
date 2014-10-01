# -----------------------------------------------------------------------------
# imports ---------------------------------------------------------------------
import numpy as np
import scipy as sp
import scipy.io.wavfile as wav
import matplotlib as mpl
import matplotlib.pyplot as plt

import wave
import struct

# simple print statement
print 'hello world!'

# -----------------------------------------------------------------------------
# using wave package ----------------------------------------------------------
# docs.python.org/2/library/wave.html
# open the wave file
z             = wave.open('audio/z01.wav', 'r')
z_channels    = z.getnchannels()
z_sampwidth   = z.getsampwidth()
z_samprate    = z.getframerate()
z_totalframes = z.getnframes()
z_totalsamps  = z.getnchannels() * z.getnframes()


# print out channels of audio file
print 'Channels:       ', z_channels
print 'Sampling Width: ', z_sampwidth
print 'Sampling Rate:  ', z_samprate
print 'Total Frames:   ', z_totalframes
print 'Total Samples:  ', z_totalsamps
print 'Total Samples (by hand): ', 10 * 44100 * 2
print '--------------------------------'

# -----------------------------------------------------------------------------
# using scipy.io.wavfile ------------------------------------------------------
# docs.scipy.org/doc/scipy/reference/generated/scipy.io.wavfile.read.html
z_v2 = wav.read('audio/z01.wav')
print z_v2[1]
