# AudioMG: MATCH GOOD!
# @module: copyConvert
# @description: Copies and converts files over to some folder.

# -----------------------------------------------------------------------------
# imports

from os import path
from os import remove
import subprocess

# -----------------------------------------------------------------------------
# methods

# copyConvert()
# @param filepath - the filepath of the file to be copied/converted.
# @param folder - the folder in which to place the converted file.
# @description copies and converts the supplied file into the supplied folder.
# @returns - VOID
# @author Nick Alekhine
# @version 10-11-2014
def copyConvert( filepath, folder ):

  # break apart supplied filepath
  basename = path.basename(filepath)
  filename = path.splitext(basename)[0]
  fileExtension = path.splitext(basename)[1]

  # if file is an ogg
  if ( fileExtension == '.ogg' ):
    convertOgg( filepath, folder, filename, fileExtension )
  # else file is either an mp3 or wav
  else:
    convertWavMp3( filepath, folder, filename, fileExtension )

def convertOgg( filepath, folder, filename, fileExtension ):
  # create a decoded ogg file in WAV format.
  ffWav = folder + filename + '_ogg.wav'
  subProcess0 = ['oggdec', '-Q', filepath, '-b', '16', '-o', ffWav]
  # converts ogg file to a 16-bit, little-endian, wav file.
  subprocess.call( subProcess0 )

  # pass the converted ogg file as the "original" filepath
  convertWavMp3( ffWav, folder, filename, fileExtension )
  # remove converted file after it has been converted to canonical form.
  remove(ffWav)

def convertWavMp3( filepath, folder, filename, fileExtension ):
  # create the future filepath
  futureFile = folder + filename + fileExtension
  ffMono = futureFile + '_mono.mp3'
  ffResampled = futureFile + '_resampled.mp3'
  
  # path to lame
  lame = '/course/cs4500f14/bin/lame'
  # initialize subprocess calls
  subProcess1 = [lame, '--silent', '-a', filepath, ffMono] 
  subProcess2 = [lame, '--silent', '--resample', '8.192',  ffMono, ffResampled]
  subProcess3 = [lame, '--silent', '--decode', ffResampled, futureFile]
  
  # convert original to mono
  subprocess.call( subProcess1 )
  # convert mono to 8192 samples/sec
  subprocess.call( subProcess2 )
  # convert resampled to wav (maintaining original extension)
  subprocess.call( subProcess3 )
  
  # remove extraneous files
  remove(ffMono)
  remove(ffResampled)
