# Adder 
# 

#imports

from os import listdir, path
import sys
from recordings.recording import Recording
import processor


#


def add( core ):

  aMode = core.getAdsMode()
  aDir  = core.getAdsDir()
  taDir = core.getTmpAdsDir()

  #file mode
  if ( aMode == 0 ):
    basename = path.basename(aDir)
    subAdd( core, aDir, basename, taDir )

  # directory mode
  if ( aMode == 1 ):
    for f in listdir(aDir):
       subAdd(core, aDir, f, taDir)

# subAdd()
#
def subAdd(core, filePath, fileName, tempPath):
  #
  tmpF = path.join( tempPath, fileName )

  rec = Recording( fileName, filePath )
  for i in processor.process(tmpF):
    rec.appendFragment(i)

  core.recDB.addRecording(rec)

