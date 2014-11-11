#Tests for Processor.

from nose.tools import *
import sys
sys.path.append('../../src/helpers')
import processor

class TestProcessor:

  #
  # FIXTURES
  #

  path = '../assets/D1/bad0616.wav'


  #
  # METHODS
  #

  def testProcess( self ):
    testData = processor.process( self.path )
    assert_equal( len(testData), 2  )
    for i in testData:
      assert_equal( len(i), 441000 )
    
