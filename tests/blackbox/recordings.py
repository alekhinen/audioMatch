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

  # testHashAndEquals()
  # @description: tests the hash() and equals() method on fixtures
  def testHashAndEquals( self ):
    self.reset()

    rec3 = Recording('a', 'b')
    rec4 = Recording('aaa', '')
    assert_equal( rec3.hash(), 195 )
    assert_equal( rec3.equals(rec4), False )
    assert_equal( rec3.equals(None), False )
    assert_equal( rec3.equals(195), False )

    assert_equal( self.rec1.equals(self.rec2), False )
    assert_equal( self.rec2.equals(self.rec1), False )

    assert_equal( self.rec2.equals(self.rec2), True )


















