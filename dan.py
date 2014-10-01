# imports
import wave

# simple print statement
print 'hello world!'

# open the wave file
z = wave.open('audio/z01.wav', 'r')

# print out channels of audio file
print 'Channels:       ', z.getnchannels()
print 'Sampling Width: ', z.getsampwidth()
print 'Sampling Rate:  ', z.getframerate()
print 'Total Frames:   ', z.getnframes()
print 'Total Samples:  ', z.getnchannels() * z.getnframes()
print 'Total Samples (by hand): ', 10 * 44100 * 2
print '--------------------------------'
print 'Reading first 100 frames'
print z.readframes(100)
