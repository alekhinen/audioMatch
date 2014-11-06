# Recording
#
# @description: A recording
# @author: Nick Alekhine
# @version: 06-11-2014

class Recording:

  # ---------------------------------------------------------------------------
  # ATTRIBUTES
  # ---------------------------------------------------------------------------

  filename = ''
  filepath = ''
  fragments = []

  # ---------------------------------------------------------------------------
  # METHODS
  # ---------------------------------------------------------------------------

  # initialize
  def __init__( self, filename, filepath ):
    self.filename = filename
    self.filepath = filepath

  # addFragment
  # @param: fragment - an array of real number
  # @description: adds a fragment to fragments
  def addFragment( fragment ):
    fragments.append( fragment )


