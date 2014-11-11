class OperationsCore:

  # ---------------------------------------------------------------------------
  # ATTRIBUTES
  # ---------------------------------------------------------------------------

  # directory of original audio files
  dirUsers = './'
  dirAds = './'
  # directory of temporary audio files
  tmpDirUsers = './'
  tmpDirAds = './'
  # modes for audio files (0 == file, 1 == directory)
  modeUsers = 0
  modeAds = 0
  # stage (0 == users, 1 == ads)
  stage = 0
  # various constants used for processing + comparison
  threshold = 75000
  fragmentSize = 2.5
  # database of recordings and fragments from users and ads
  recDB = RecordingsDatabase()

  # ---------------------------------------------------------------------------
  # METHODS
  # ---------------------------------------------------------------------------

  # init()
  def __init__( self, fragmentSize, threshold ):
    self.fragmentSize = fragmentSize
    self.threshold = threshold
  
  # setArguments()
  # @description: sets arguments based off of CLI arguments
  def setArguments( self, sysArgs ):
    parsedArgs = parser.parse( sysArgs )
    if ( validate.isValid( parsedArgs ) ):
      self.setModes( parsedArgs[0], parsedArgs[2] )
      self.setUsersDir( parsedArgs[1] )
      self.setAdsDir( parsedArgs[3] )


  # setModes()
  def setModes( self, uMode, aMode ):
    self.modeUsers = uMode
    self.modeAds = aMode
  
  # setStage()
  def setStage( self, stage ):
    self.stage = stage

  # setUsersDir()
  def setUsersDir( self, directory ):
    self.dirUsers = directory
  
  # setAdsDir()
  def setAdsDir( self, directory ):
    self.dirAds = directory
  
