class OperationsCore:

  # directory of original audio files
  usersDirectory = './'
  adsDirectory = './'

  # various constants used for processing + comparison
  threshold = 75000
  fragmentSize = 2.5

  # links to database of fragments of recordings
  userRecordings =
  adRecordings =

  # ---------------------------------------------------------------------------
  # methods
  def __init__( self, fragmentSize, threshold ):
    self.fragmentSize = fragmentSize
    self.threshold = threshold
