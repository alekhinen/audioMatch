from recordings.database import RecordingsDatabase
import helpers.argParser as parser
import helpers.validator as validator
import helpers.copyconvert as copyconvert
from shutil import rmtree
from os import makedirs
import os.path
import helpers.processer as processer

class OperationsCore:

  # ---------------------------------------------------------------------------
  # ATTRIBUTES
  # ---------------------------------------------------------------------------

  # directory of original audio files
  dirUsers = './'
  dirAds = './'
  # directory of temporary audio files
  tmpDirUsers = './tmp/users/'
  tmpDirAds = './tmp/ads/'
  # modes for audio files (0 == file, 1 == directory)
  modeUsers = 0
  modeAds = 0
  # stage (0 == users, 1 == ads)
  stage = 0
  # various constants used for processing + comparison
  threshold = 75000
  fragmentSize = 2.5
  # database of recordings and fragments from ads
  recDB = RecordingsDatabase()

  # ---------------------------------------------------------------------------
  # METHODS
  # ---------------------------------------------------------------------------

  # init()
  def __init__( self, fragmentSize, threshold ):
    self.fragmentSize = fragmentSize
    self.threshold = threshold
  
  # ---------------
  # -   SETTERS   -
  # ---------------

  # setArguments()
  # @description: sets arguments based off of CLI arguments
  def setArguments( self, sysArgs ):
    parsedArgs = parser.parse( sysArgs )
    if ( validator.isValid( parsedArgs ) ):
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

  # ---------------
  # -   GETTERS   -
  # ---------------

  # getUsersDir()
  def getUsersDir( self ):
    return self.dirUsers
  # getAdsDir()
  def getAdsDir( self ):
    return self.dirAds
  # getUsersMode()
  def getUsersMode( self ):
    return self.modeUsers
  # getAdsMode()
  def getAdsMode( self ):
    return self.modeAds
  # getTmpAdsDir()
  def getTmpAdsDir( self ):
    return self.tmpDirAds
  # getTmpUsersDir()
  def getTmpUsersDir( self ):
    return self.tmpDirUsers

  # ----------------
  # -  CONVERSION  -
  # ----------------

  # convertFiles()
  # @description: copies and converts files from directories into tmp dirs
  def convertFiles( self ):
    self.createTmpDirectories()

    if self.modeUsers == 0:
      copyconvert.copyConvert(self.dirUsers, self.tmpDirUsers)
    else:
      for subdir, dirs, files in os.walk( self.dirUsers ):
        for f in files:
          copyconvert.copyConvert( os.path.join(self.dirUsers ,f), self.tmpDirUsers)

    if self.modeAds == 0:
      copyconvert.copyConvert(self.dirAds, self.tmpDirAds)
    else:
      for subdir, dirs, files in os.walk( self.dirAds ):
        for f in files:
          copyconvert.copyConvert( os.path.join(self.dirAds, f), self.tmpDirAds)

  # createTmpDirectories()
  # @description: creates tmp directories
  def createTmpDirectories( self ):
    # remove tmp directories if they exist.
    self.removeTmpDirectories()
    
    # create the tmp directories
    makedirs( self.tmpDirUsers )
    makedirs( self.tmpDirAds )

  # removeTmpDirectories()
  # @description: removes tmp directories
  def removeTmpDirectories( self ):
    # check if tmp directories exist. if so, delete them.
    if ( os.path.exists( self.tmpDirUsers ) ):
      rmtree( self.tmpDirUsers )
    if ( os.path.exists( self.tmpDirAds ) ):
      rmtree( self.tmpDirAds )

  # -----------------
  # -  COMPARISONS  -
  # -----------------

  # compareUsersAgainstAds()
  # @assumption: recDB contains all recordings + fragments from ads
  # @assumption: ./tmp/users contains all processed recordings
  def compareUsersAgainstAds( self ):
    # process a single user recording
    # store that recording + fragments inside recDB
    # do the comparisons
    #   - appends string results (e.g. "" or "MATCH ... ...") to RESULT
    # remove that user recording + fragments from recDB
    # repeat.
    # return RESULT
    
    # for subdir, dirs, files in os.walk( self.tmpDirUsers ):
    #   for f in files:
    #     # TODO: Add to recordings db
    #     #self.recDB = processer.process( f )


















