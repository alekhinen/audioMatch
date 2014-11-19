# Fragment
#
# @description: A fragment associated with a recording
# @author: Nick Alekhine
# @version: 07-11-2014 (DD-MM-YYYY)

class Fragment:

  # ---------------------------------------------------------------------------
  # ATTRIBUTES
  # ---------------------------------------------------------------------------

  # TODO: keep track of time-offset in audio track.
  # TODO: keep track of adjacent chunks

  # the parent recording for this fragment
  recording_id = 0
  # the hash value of the fft'd fragment
  hashValue = 0
  # the index value in the parent recording's list of fragments
  timeOffset = 0

  # ---------------------------------------------------------------------------
  # METHODS
  # ---------------------------------------------------------------------------

  # initialization
  def __init__( self, recording_id, hashValue, timeOffset ):
    self.recording_id = recording_id
    self.hashValue = hashValue
    self.timeOffset = timeOffset

  # setRecordingId()
  # @param: recording_id - the id to associate with this fragment
  # @description: sets the recording_id for this.
  # @returns: the recording id (integer)
  def setRecordingId( self, recording_id ):
    self.recording_id = recording_id
    return self.recording_id

  # hash()
  # @description: returns the hash value for this
  # @returns: hash value (integer)
  def hash( self ):
    return self.hashValue

  # equals()
  # @param: obj - an object
  # @description: determines if this is equal to an object
  # @returns: boolean
  def equals( self, obj ):
    if not isinstance(obj, Fragment):
      return False
    else:
      return self.hash() == obj.hash()