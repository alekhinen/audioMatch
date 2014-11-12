# Database
#
# @description: A dictionary database for fragments of recordings
# @author: Nick Alekhine
# @version: 07-11-2014 (DD-MM-YYYY)

class RecordingsDatabase:

  # ---------------------------------------------------------------------------
  # ATTRIBUTES
  # ---------------------------------------------------------------------------

  recordings = {}
  fragments = {}

  # ---------------------------------------------------------------------------
  # METHODS
  # ---------------------------------------------------------------------------

  # initialize
  def __init__( self ):
    self.recordings = {}
    self.fragments = {}

  # addFragment()
  # @param: fragment - an instance of Fragment
  # @description: adds a fragment to the fragments database
  # @returns: list of values at key (from dictionary)
  def addFragment( self, fragment ):
    fHash = fragment.hash()
    if ( fHash in self.fragments ):
      self.fragments[fHash].append(fragment)
    else:
      self.fragments[fHash] = [fragment]
    return self.fragments[fHash]

  # getFragment()
  # @param: key - an integer key value
  # @description: gets the value at the supplied key from the fragments db
  # @returns: value (a list)
  def getFragment( self, key ):
    if ( key in self.fragments ):
      return self.fragments[ key ]
    else:
      return None

  # addRecording()
  # @param: fragment - an instance of Fragment
  # @description: adds a fragment to the fragments database
  # @returns: list of values at key (from dictionary)
  def addRecording( self, recording ):
    recHash = recording.hash()
    self.recordings[recHash] = recording
    return self.recordings[recHash]

  # getRecording()
  # @param: key - an integer key value
  # @description: gets the value at the supplied key from the recordings db
  # @returns: value (a Recording)
  def getRecording( self, key ):
    if ( key in self.recordings ):
      return self.recordings[ key ]
    else:
      return None


