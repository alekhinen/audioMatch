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
  
  # create the future filepath
  futureFile = folder + filename + fileExtension
  ffMono = futureFile + '_mono.mp3'
  ffResampled = futureFile + '_resampled.mp3'

  # TODO: absolute filepath to lame. unsure if this is the right thing to do.
  
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
