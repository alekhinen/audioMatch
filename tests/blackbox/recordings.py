from nose.tools import *

import sys
sys.path.append('../../src/recordings')

from recording import Recording

# -----------------------------------------------------------------------------
# tests all modules in recordings
class TestRecordings:

  rec1 = Recording('../assets/D1/bad0616.wav', 'bad0616.wav')
  rec2 = Recording('../assets/D1/z03.wav', 'z03.wav')

  # reset()
  # @description: resets fixtures
  def reset( self ):
    self.rec1 = Recording('../assets/D1/bad0616.wav', 'bad0616.wav')
    self.rec2 = Recording('../assets/D1/z03.wav', 'z03.wav')
  
  # testAppendFragment()
  # @description: tests the appendFragment() method on fixtures
  def testAppendFragment( self ):
    self.reset()
    assert_equal( self.rec1.appendFragment([0, 1, 2, 3]), 
                  [ [0, 1, 2, 3] ] )
    assert_equal( self.rec1.appendFragment([4, 5, 6]), 
                  [ [0, 1, 2, 3], [4, 5, 6] ] )

  # testGetFragment()
  # @description: tests the getFragment() method on fixtures
  def testGetFragment( self ):
    self.reset()

    self.rec1.appendFragment([0, 1, 2, 3])
    self.rec1.appendFragment([4, 5, 6])
    self.rec1.appendFragment([9, 9, 9, 9, 9])

    assert_equal( self.rec1.getFragment(0), [0, 1, 2, 3 ] )
    assert_equal( self.rec1.getFragment(1), [4, 5, 6] )
    assert_equal( self.rec1.getFragment(2), [9, 9, 9, 9, 9] )
    assert_equal( self.rec1.getFragment(3), None )
    assert_equal( self.rec1.getFragment(-1), None )

  # testRemoveFragment()
  # @description: tests the removeFragment() method on fixtures
  def testRemoveFragment( self ):
    self.reset()

    assert_equal( self.rec1.removeFragment(0), [] )
    assert_equal( self.rec1.removeFragment(-1), [] )

    self.rec1.appendFragment([0, 1, 2, 3])
    self.rec1.appendFragment([4, 5, 6])
    self.rec1.appendFragment([9, 9, 9, 9, 9])

    assert_equal( self.rec1.removeFragment(1), [[0, 1, 2, 3], [9, 9, 9, 9, 9]] )
    assert_equal( self.rec1.removeFragment(1), [[0, 1, 2, 3]] )