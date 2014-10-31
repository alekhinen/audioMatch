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
def copyFile( fileName, core ):
  if core['Stage'] == 0:
    fullFile = os.path.join( core['U_Dir'], fileName )
    UTIL.copy2( fullFile, "./tmp/User/" + fileName )

  elif core['Stage'] == 1:
    fullFile = os.path.join( core['A_Dir'], fileName )
    UTIL.copy2( fullFile, "./tmp/Ads/" + fileName )

def convertFile ( fileName, core ):
  if core['Stage'] == 0:
    mdir = core['U_Dir']
    tdir = "./tmp/User/"
  elif core['Stage'] == 1:
    mdir = core['A_Dir']
    tdir = "./tmp/Ads/"
  else:
    print "ERROR: bad stage value in Copy and Convert"

  # get the base name (os.path.basename returns FILENAME.FILEFORMAT)
  baseFileName = os.path.basename( fileName ).split('.')[0]
  # print baseFileName
  # fullFileName = tdir + baseFileName + '.wav'
  fullFileName = tdir + fileName
  subprocess.call(["lame", "--decode", mdir + fileName, fullFileName])


