from nose.tools import *

import sys
sys.path.append('../../src/recordings')

from recording import Recording
from fragment import Fragment

# -----------------------------------------------------------------------------
# tests all methods in Fragment
class TestFragments:

  # Recordings
  rec1 = Recording('../assets/D1/bad0616.wav', 'bad0616.wav')
  rec2 = Recording('../assets/D1/z03.wav', 'z03.wav')

  # Fragments
  frag1 = Fragment( rec1.hash(), 123, 0 )
  frag2 = Fragment( rec1.hash(), 467, 1 )
  frag3 = Fragment( rec2.hash(), 123, 0 )
  frag4 = Fragment( rec2.hash(), 789, 1 )

  # reset()
  # @description: resets fixtures
  def reset( self ):
    self.rec1 = Recording('../assets/D1/bad0616.wav', 'bad0616.wav')
    self.rec2 = Recording('../assets/D1/z03.wav', 'z03.wav')

    self.frag1 = Fragment( self.rec1.hash(), 123, 0 )
    self.frag2 = Fragment( self.rec1.hash(), 467, 1 )
    self.frag3 = Fragment( self.rec2.hash(), 123, 0 )
    self.frag4 = Fragment( self.rec2.hash(), 789, 1 )
  
  # testEquals()
  # @description: tests the equals() method on fixtures
  def testEquals( self ):
    self.reset()
    assert_equal( self.frag1.equals(self.frag1), True )
    assert_equal( self.frag1.equals(self.frag2), False )
    assert_equal( self.frag2.equals(self.frag1), False )
    assert_equal( self.frag2.equals(self.frag2), True )

    assert_equal( self.frag1.equals(self.frag3), True )
    assert_equal( self.frag1.equals(self.frag4), False )
    assert_equal( self.frag2.equals(self.frag4), False )

 