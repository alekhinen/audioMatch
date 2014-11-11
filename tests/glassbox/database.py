from nose.tools import *

import sys
sys.path.append('../../src/recordings')

from recording import Recording
from fragment import Fragment
from recordingsDatabase import RecordingsDatabase

# -----------------------------------------------------------------------------
# tests all methods in RecordingsDatabase
class TestRecordingsDatabase:

  # ---------------------------------------------------------------------------
  # FIXTURES
  # ---------------------------------------------------------------------------

  # Recordings
  rec1 = Recording('../assets/D1/bad0616.wav', 'bad0616.wav')
  rec2 = Recording('../assets/D1/z03.wav', 'z03.wav')

  # Fragments
  frag1 = Fragment( rec1.hash(), 123, 0 )
  frag2 = Fragment( rec1.hash(), 467, 1 )
  frag3 = Fragment( rec2.hash(), 123, 0 )
  frag4 = Fragment( rec2.hash(), 789, 1 )

  # Database
  db = RecordingsDatabase()

  # ---------------------------------------------------------------------------
  # METHODS
  # ---------------------------------------------------------------------------

  # reset()
  # @description: resets fixtures
  def reset( self ):
    self.rec1 = Recording('../assets/D1/bad0616.wav', 'bad0616.wav')
    self.rec2 = Recording('../assets/D1/z03.wav', 'z03.wav')

    self.frag1 = Fragment( self.rec1.hash(), 123, 0 )
    self.frag2 = Fragment( self.rec1.hash(), 467, 1 )
    self.frag3 = Fragment( self.rec2.hash(), 123, 0 )
    self.frag4 = Fragment( self.rec2.hash(), 789, 1 )

    self.db = RecordingsDatabase()
  
  # testAddFragment()
  # @description: tests the addFragment() method on db fixture
  def testAddFragment( self ):
    self.reset()

    assert_equal( self.db.addFragment( self.frag3 ), [self.frag3] )
    assert_equal( self.db.addFragment( self.frag1 ), [self.frag3, self.frag1] )
    assert_equal( self.db.addFragment( self.frag2 ), [self.frag2] )
    assert_equal( self.db.addFragment( self.frag4 ), [self.frag4] )

  # testAddRecording()
  # @description: tests the addRecording() method on db fixture
  def testAddRecording( self ):
    self.reset()

    assert_equal( self.db.addRecording( self.rec1 ), self.rec1 )
    assert_equal( self.db.addRecording( self.rec2 ), self.rec2 )

  # testGetFragment()
  # @description: tests the getFragment() method on db fixture
  def testGetFragment( self ):
    self.reset()

    assert_equal( self.db.getFragment(12345), None )

    self.db.addFragment( self.frag3 )
    self.db.addFragment( self.frag1 )
    self.db.addFragment( self.frag2 )
    self.db.addFragment( self.frag4 )

    assert_equal( self.db.getFragment(self.frag1.hash()), 
                  [self.frag3, self.frag1] )
    assert_equal( self.db.getFragment(self.frag3.hash()), 
                  [self.frag3, self.frag1] )
    assert_equal( self.db.getFragment(self.frag2.hash()), [self.frag2] )
    assert_equal( self.db.getFragment(self.frag4.hash()), [self.frag4] )

  # testGetRecording()
  # @description: tests the getRecording() method on db fixture
  def testGetRecording( self ):
    self.reset()

    assert_equal( self.db.getRecording(12345), None )

    self.db.addRecording( self.rec1 )
    self.db.addRecording( self.rec2 )

    assert_equal( self.db.getRecording(self.rec1.hash()), self.rec1 )
    assert_equal( self.db.getRecording(self.rec2.hash()), self.rec2 )

