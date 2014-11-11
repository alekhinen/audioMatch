# Database
#
# @description: A dictionary database for fragments of recordings
# @author: Nick Alekhine
# @version: 07-11-2014 (DD-MM-YYYY)

class RecordingsDatabase:

  # ---------------------------------------------------------------------------
  # ATTRIBUTES
  # ---------------------------------------------------------------------------

  recordingsDB = {}
  fragmentsDB = {}

  # ---------------------------------------------------------------------------
  # METHODS
  # ---------------------------------------------------------------------------

  # initialize
  def __init__( self ):
    self.recordingsDB = {}
    self.fragmentsDB = {}

  # addFragment()
  # @param: fragment - an instance of Fragment
  # @description: adds a fragment to the fragments database
  # @returns: list of values at key (from dictionary)
  def addFragment( self, fragment ):
    fHash = fragment.hash()
    if ( fHash in self.fragmentsDB ):
      self.fragmentsDB[fHash].append(fragment)
    else:
      self.fragmentsDB[fHash] = [fragment]
    return self.fragmentsDB[fHash]

  # getFragment()
  # @param: key - an integer key value
  # @description: gets the value at the supplied key from the fragments db
  # @returns: value (a list)
  def getFragment( self, key ):
    if ( key in self.fragmentsDB ):
      return self.fragmentsDB[ key ]
    else:
      return None

  # addRecording()
  # @param: fragment - an instance of Fragment
  # @description: adds a fragment to the fragments database
  # @returns: list of values at key (from dictionary)
  def addRecording( self, recording ):
    recHash = recording.hash()
    self.recordingsDB[recHash] = recording
    return self.recordingsDB[recHash]

  # getRecording()
  # @param: key - an integer key value
  # @description: gets the value at the supplied key from the recordings db
  # @returns: value (a Recording)
  def getRecording( self, key ):
    if ( key in self.recordingsDB ):
      return self.recordingsDB[ key ]
    else:
      return None


