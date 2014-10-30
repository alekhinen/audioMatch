#AudioMG: MATCH GOOD!

#Copy and Convert Module

import shutil as UTIL
import subprocess
import os.path

def copyFile ( fileName, core ):
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
    tdir = "./tmp/User/"
  else:
    print "ERROR: bad stage value in Copy and Convert"
  subprocess.call(["lame", "--decode", mdir + fileName, tdir + fileName])


