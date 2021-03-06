# Recording
#
# @description: A recording
# @author: Nick Alekhine
# @version: 06-11-2014 (DD-MM-YYYY)

class Recording:

  # ---------------------------------------------------------------------------
  # ATTRIBUTES
  # ---------------------------------------------------------------------------

  filename = ''
  filepath = ''
  fragments = []
  hashValue = -1

  # ---------------------------------------------------------------------------
  # METHODS
  # ---------------------------------------------------------------------------

  # initialize
  def __init__( self, filename, filepath ):
    self.filename = filename
    self.filepath = filepath
    self.fragments = []
    self.hashValue = self.computeHash()

  # appendFragment()
  # @param: fragment - an array of real number
  # @description: adds a fragment to fragments
  # @returns: the list of fragments
  def appendFragment( self, fragment ):
    self.fragments.append( fragment )
    return self.fragments

  # extractFragment()
  # @param: i - an index position
  # @description: get the fragment at the ith position
  # @returns: a fragment (array of real numbers)
  def getFragment( self, i ):
    if ( i < len(self.fragments) and i >= 0 ):
      return self.fragments[i]
    else:
      return None

  # removeFragment()
  # @param: i - an index position
  # @description: removes the fragment at the ith position
  # @returns: array of fragments
  def removeFragment( self, i ):
    if ( i < len(self.fragments) and i >= 0 ):
      self.fragments.pop( i )
    return self.fragments

  # computeHash()
  # @description: computes the hash value of this
  # @returns: this hash value (integer)
  def computeHash( self ):
    result = 0

    for char in self.filepath:
      result += ord(char)
    for char in self.filename:
      result += ord(char)

    self.hashValue = result
    return self.hashValue

  # hash()
  # @description: returns the hashvalue of self
  # @returns: a hashvalue (integer)
  def hash( self ):
    if self.hashValue == -1:
      return self.computeHash()
    else: 
      return self.hashValue
    
  # equals()
  # @param: obj - an object
  # @description: compares an object to this
  # @return: boolean
  def equals( self, obj ):
    if not isinstance(obj, Recording):
      return False
    else:
      return self.hash() == obj.hash()


