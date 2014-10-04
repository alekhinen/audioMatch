# Prototype 1B for AudioMG.
# Written:
# 10/3/14 by ZiG

#IMPORTS:
import sys
import os.path
import sndhdr
#----
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile
from scipy.fftpack import fft


def compareFiles(f1, f2, val):
    result = 'MATCH'

    if ( len(f1) == len(f2) ):
        for i in range(0, len(f2) / 2):
            if ( (f1[i] - f2[i]) > val):
                result = 'NO MATCH'
            else:
            	result = 'NO MATCH'
            	print result

#Prep(file, file): Takes the files, prepares them, and then sends them to FFT
def prep(f1, f2):
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
    compare(c2, b2, 0.1)
    return None

#Parse(): Takes the command line arguments and feeds them
def parse():
    file1 = sys.argv[2]
    file2 = sys.argv[4]
    if (len(sys.argv) != 5):
        sys.stderr.write('ERROR: Incorrect number of arguments')
    elif (sys.argv[1] != "-f" or sys.argv[3] != "-f"):
        sys.stderr.write('ERROR: Incorrect arguments')
    elif (not os.path.isfile(file1)):
        sys.stderr.write('ERROR: first file could not be found')
    elif (not os.path.isfile(file2)):
        sys.stderr.write('ERROR: second file could not be found')
    elif (not sndhdr.what(file1)[0] == 'wav'):
        sys.stderr.write('ERROR: first file is not a .WAV')
    elif (not sndhdr.what(file2)[0] == 'wav'):
        sys.stderr.write('ERROR: second file is not a .WAV')
    else:
        prep(file1, file2)
        return None
