#AudioMatch Testing Suite
# @description glassbox tests for src/copyconvert
# @author Nick Alekhine
# @version 10-11-2014 (DD-MM-YYYY)

# -----------------------------------------------------------------------------
# IMPORTS
# -----------------------------------------------------------------------------

from nose.tools import *
from os import makedirs
from shutil import rmtree
import os.path
import sys
sys.path.append('../../src')
import copyconvert

# -----------------------------------------------------------------------------
# TESTS
# -----------------------------------------------------------------------------

# tests copyConvert() method
class TestCopyConvert:

  # TODO: unit tests on every single file in D1 & D2. (to check running time)

  # files
  f1 = '../assets/D1/bad0616.wav'
  f2 = '../assets/D2/curieuse.wav'
  f3 = '../assets/D1/rimsky.mp3'

  # destination directories
  d1 = '../assets/tmp/D1/'
  d2 = '../assets/tmp/D2/'

  # initialize destination directories
  def reset( self ):
    self.implode() 
    makedirs(self.d1)
    makedirs(self.d2)
 
  # destroys destination directories (if they exist)
  def implode( self ):
    if (os.path.exists(self.d1)):
      rmtree(self.d1)
    if (os.path.exists(self.d2)):
      rmtree(self.d2)

  # testCopyConvert()
  # @description: tests the copyConvert() method from copyconvert
  def testEquals( self ):
    self.reset()
    
    # conversion 1
    copyconvert.copyConvert(self.f1, self.d1)
    assert_equal(os.path.exists('../assets/tmp/D1/bad0616.wav'), True)
    # conversion 2
    copyconvert.copyConvert(self.f2, self.d2)
    assert_equal(os.path.exists('../assets/tmp/D2/curieuse.wav'), True)
    # conversion 3
    copyconvert.copyConvert(self.f3, self.d2)
    assert_equal(os.path.exists('../assets/tmp/D2/rimsky.mp3'), True)
    
    self.implode()

