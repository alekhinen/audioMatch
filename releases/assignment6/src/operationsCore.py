from recordings.fragment  import Fragment
from recordings.recording import Recording
from recordings.database  import RecordingsDatabase
import helpers.argParser   as parser
import helpers.validator   as validator
import helpers.copyconvert as copyconvert
import helpers.comparator  as comparator
import helpers.processor   as processor
from shutil import rmtree
from os     import makedirs
import os.path

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
  fragmentSize = 0.125
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
    if ( os.path.exists( './tmp' ) ):
      rmtree( './tmp' )

  # ------------------------
  # -  DATABASE ADDITIONS  -
  # ------------------------

  # addAdsToDB()
  # @description: adds processed recordings and fragments from the tmp/ 
  # directory for the ads 
  def addAdsToDB( self ):
    for subdir, dirs, files in os.walk( self.tmpDirAds ):
      for f in files:
        # create recording
        rec = Recording( f, os.path.join( self.tmpDirAds, f ) )
        rec_id = rec.hash()
        # process audio recording data
        fragments = processor.process( os.path.join( self.tmpDirAds, f ), rec_id, self.fragmentSize )
        # add all fragments to the recording + database
        for fragment in fragments:
          rec.appendFragment( fragment )
          self.recDB.addFragment( fragment )
        # add recording to database
        self.recDB.addRecording( rec )

  # -----------------
  # -  COMPARISONS  -
  # -----------------

  # compareUsersAgainstAds()
  # @assumption: recDB contains all recordings + fragments from ads
  # @assumption: ./tmp/users contains all processed recordings
  def compareUsersAgainstAds( self ):
    for subdir, dirs, files in os.walk( self.tmpDirUsers ):
      for f in files:
        # create recording for the current file
        rec = Recording( f, os.path.join( self.tmpDirUsers, f) )
        rec_id = rec.hash()
        # process audio recording data
        fragments = processor.process( os.path.join( self.tmpDirUsers, f), rec_id, self.fragmentSize )
        # add all fragments to the recording
        for fragment in fragments:
          rec.appendFragment( fragment )

        matchedRecordings = []
        # find similar fragments to this recording's fragments
        for fragment in fragments:
          fHash = fragment.hash()
          sameFrags = self.recDB.getSimilarFragments( fHash, self.threshold )
          
          # for all similar fragments, do a linear check.
          for sFrag in sameFrags:
            s_rec_id = sFrag.recording_id
            sRec = self.recDB.getRecording( s_rec_id )
            if ( not sRec in matchedRecordings ):
              sFragList = sRec.fragments[int(sFrag.timeOffset * 16):]
              curFragList = rec.fragments[int(fragment.timeOffset * 16):]

              isSimilar = comparator.compare( curFragList, sFragList, self.threshold )
            
              if ( isSimilar ):
                print 'MATCH', rec.filename, sRec.filename, fragment.timeOffset, sFrag.timeOffset
                matchedRecordings.append(sRec)


