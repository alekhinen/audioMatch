# Fragment
#
# @description: A fragment associated with a recording
# @author: Nick Alekhine
# @version: 07-11-2014

class Fragment:

  # ---------------------------------------------------------------------------
  # ATTRIBUTES
  # ---------------------------------------------------------------------------

  recording_id = 0
  value = 0

  # ---------------------------------------------------------------------------
  # METHODS
  # ---------------------------------------------------------------------------

  def __init__( self, recording_id, value ):
    self.recording_id = recording_id
    self.value = value

  def setValue( self, value ):
    self.value = value
    return self.value

  def getValue( self ):
    return self.value

  def setRecordingId( self, recording_id ):
    self.recording_id = recording_id
    return self.recording_id