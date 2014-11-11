# Adder 
# 

#imports

from os import listdir, path



#

taDir = './tmp/adRecs/'


def add( core ):

  aMode = core.getAdMode()
  aDir  = core.getAdDir()

  #file mode
  if ( aMode == 0 ):
    subAdd( core, aDir, "", taDir )

  # directory mode
  if ( aMode == 1 ):
    for f in listdir(aDir):
       subAdd(core, aDir, f, taDir)

# subAdd()
#
def subAdd(core, filePath, fileName, tempPath):
  #
  tmpF = join( tempPath, fileName )

  rec = recording( fileName, filePath )
  for i in process(tmpF) rec.appendFragment(i)

  core.recDB.addRecording(rec)

  return none
  
