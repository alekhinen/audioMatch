#AudioMG: MATCH GOOD!
# @module: Copy And Convert
# @description: Copies and converts files over to tmp/

# -----------------------------------------------------------------------------
# imports
import os.path
import shutil as UTIL
import subprocess
import os.path

# -----------------------------------------------------------------------------
# copyFile()
# @description: copies a file over to the specified tmp directory
def copyFile( filepath, stage ):
  if stage == 0:
    futureFile = './tmp/userRecs/' + os.path.basename(filepath)
    UTIL.copy2( filepath, futureFile )
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
