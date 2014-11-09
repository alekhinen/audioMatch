# Adder 
# 

#imports

from os import listdir, path



#
tuDir = './tmp/userRecs/'
taDir = './tmp/userRecs/'


def add( core ):

  makedirs(uDir)
  makedirs(aDir)

  uMode = core.getUserMode()
  aMode = core.getAdMode()
  uDir  = core.getUserDir()
  aDir  = core.get
  # file mode
  if ( uMode == 0 ):
    subAdd( core, uDir, "" tuDir)

  # directory mode
  elif ( uMode == 1 ):
    for f in listdir(uDir):
      subAdd(core, uDir, f, tuDir)

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
  convertFile( join(filePath, fileName), core.getStage() )
  tmpF = join( tempPath, fileName )

  rec = recording( fileName, filePath )
  for i in process(tmpF) rec.appendFragment(i)

  core.recDB.addRecording(rec)

  return none
  
