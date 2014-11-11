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
# @description copies over and converts the supplied file into the supplied
# folder.
# @returns - ???
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
  # initialize subprocess calls
  # convert original to mono
  subProcess1 = ['/course/cs4500f14/bin/lame', '-a', filepath, ffMono] 
  # convert mono to 8192 samples/sec
  subProcess2 = ['/course/cs4500f14/bin/lame', '--resample', '8.192',  ffMono, ffResampled]
  # convert resampled to wav (maintaining original extension)
  subProcess3 = ['/course/cs4500f14/bin/lame', '--decode', ffResampled, futureFile]
  subprocess.call( subProcess1 )
  subprocess.call( subProcess2 )
  subprocess.call( subProcess3 )
  
  # remove extraneous files
  remove(ffMono)
  remove(ffResampled)
