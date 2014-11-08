#AudioMG: MATCH GOOD!
# @module: Copy And Convert
# @description: Copies and converts files over to tmp/

# -----------------------------------------------------------------------------
# imports
import os.path
import shutil as UTIL
import subprocess
from os import remove


# copyAndConvert()
def copyAndConvert( filepath, stage ):
  if stage == 0:
     tempdir = '../tmp/userRecs/'

  else:
     tempdir = '../tmp/adRecs/'

  basename = os.path.basename(filepath)
  filename = os.path.splitext(basename)[0]
  fileExtension = os.path.splitext(basename)[1]
  futureFile = tempdir + filename
  subprocess.call(['../vendor/lame', '-a', filepath, futureFile + '_mono.mp3' ])
  subprocess.call(['../vendor/lame', '--resample', '8.192', futureFile + '_mono.mp3', futureFile + '_resampled.mp3'])
  subprocess.call(['../vendor/lame', '--decode', futureFile + '_resampled.mp3', futureFile + fileExtension])
    
  remove(futureFile + '_mono.mp3')
  remove(futureFile + '_resampled.mp3')

# -----------------------------------------------------------------------------
# copyFile()
# @description: copies a file over to the specified tmp directory
def copyFile( filepath, stage ):
  if stage == 0:
    filename = os.path.splitext(os.path.basename(filepath))[0]
    futureFile = '../tmp/userRecs/' + filename
    subprocess.call(['../vendor/lame', '-a', filepath, futureFile + '_mono.mp3' ])
    subprocess.call(['../vendor/lame', '--resample', '8.192', futureFile + '_mono.mp3', futureFile + '_resampled.mp3'])
    # TODO: retain the original file extension (this forces everything to have a .wav extension)
    subprocess.call(['../vendor/lame', '--decode', futureFile + '_resampled.mp3', futureFile + '.wav'])
    
    remove(futureFile + '_mono.mp3')
    remove(futureFile + '_resampled.mp3')

  else:
    futureFile = './tmp/adRecs/' + os.path.basename(filepath)
    UTIL.copy2( filepath, futureFile )

# -----------------------------------------------------------------------------
# convertFile()
# @description: converts an MP3 file to a WAV file and places it inside
#               the tmp/ directory.
#               (note: filename is retained, including .mp3 extension)
def convertFile ( filepath, stage ):
  if stage == 0:
    tempDir = './tmp/userRecs/'
  else:
    tempDir = './tmp/adRecs/'

  futureFile = tempDir + os.path.basename(filepath)
  subprocess.call(['./lame', '--silent', '--decode', filepath, futureFile])
