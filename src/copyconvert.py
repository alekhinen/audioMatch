# AudioMG: MATCH GOOD!
# @module: copyConvert
# @description: Copies and converts files over to some folder.

# -----------------------------------------------------------------------------
# imports

import os.path
import os.remove
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
  basename = os.path.basename(filepath)
  filename = os.path.splitext(basename)[0]
  fileExtension = os.path.splitext(basename)[1]
  
  # create the future filepath
  futureFile = folder + filename + fileExtension
  ffMono = futureFile + '_mono.mp3'
  ffResampled = futureFile + '_resampled.mp3'

  # initialize subprocess calls
  # convert original to mono
  subProcess1 = ['../vendor/lame', '-a', filepath, ffMono 
  # convert mono to 8192 samples/sec
  subProcess2 = ['../vendor/lame', '--resample', '8.192',  ffMono, ffResampled]
  # convert resampled to wav (maintaining original extension)
  subProcess3 = ['../vendor/lame', '--decode', ffResampled, futureFile]
  subprocess.call( subProcess1 )
  subprocess.call( subProcess2 )
  subprocess.call( subProcess3 )
  
  # remove extraneous files
  os.remove(ffMono)
  os.remove(ffResampled)