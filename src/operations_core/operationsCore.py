class OperationsCore:

  # directory of original audio files
  usersDirectory = './'
  adsDirectory = './'

  # various constants used for processing + comparison
  threshold = 75000
  fragmentSize = 2.5

  userMode = 0
  adMode   = 0
  stage    = 0

  recDB    = 0
 

  # ---------------------------------------------------------------------------
  # methods
  def __init__( self, fragmentSize, threshold ):
    self.fragmentSize = fragmentSize
    self.threshold = threshold
    self.recDB = recordingsDatabase()
  
  def setMode(self, uMode, aMode ):
    self.userMode = uMode
    self.adMode = aMode
  def setStage(self, stage):
    self.stage = stage
  def setUserDir(self, directory):
    self.userDirectory = directory
  def setAdDir(self, directory):
    self.adsDirectory = directory
  
