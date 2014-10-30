#AudioMG: MATCH GOOD!

#Copy and Convert Module

import shutil as UTIL
import subprocess
def copyFile ( fileName, core ):
  if core['Stage'] == 0:
    UTIL.copy2( fileName, "./tmp/User/" )
  elif core['Stage'] == 1:
    UTIL.copy2( fileName, "./tmp/Ads/" )

def convertFile ( fileName, core ):
  if core['Stage'] == 0:
    mdir = core['U_Dir']
    tdir = "./tmp/User/"
  elif core['Stage'] == 1:
    mdir = core['A_Dir']
    tdir = "./tmp/User/"
  else
    print "ERROR: bad stage value in Copy and Convert"
  subprocess.call(["lame", "--decode", mdir + fileName, tdir + fileName])

  
