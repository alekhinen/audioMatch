# AudioMatch Testing Suite
# @description glassbox tests for src/copyconvert
# @author Nick Alekhine
# @version 10-11-2014 (DD-MM-YYYY)

# -----------------------------------------------------------------------------
# IMPORTS
# -----------------------------------------------------------------------------

from nose.tools import *
import os.makedirs
import os.rmdir
import os.path
import sys
sys.path.append('../../src')
from copyconvert import copyConvert

# -----------------------------------------------------------------------------
# TESTS
# -----------------------------------------------------------------------------

# tests copyConvert() method
class TestCopyConvert:

  # files
  f1 = '../assets/D1/bad0616.wav'
  f2 = '../assets/D2/curieuse.wav'
  f3 = '../assets/D1/rimsky.mp3'

  # destination directories
  d1 = '../assets/tmp/D1'
  d2 = '../assets/tmp/D2'

  # initialize destination directories
  os.makedirs(d1)
  os.makedirs(d2)
  
  # testCopyConvert()
  # @description: tests the copyConvert() method from copyconvert
  def testEquals( self ):
    copyConvert(f1, d1)
    assert_equal(os.path.exists('../assets/tmp/D1/bad0616.wav'), True)
 