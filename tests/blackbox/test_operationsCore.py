# AudioMatch Testing Suite
# @description blackbox tests for src/operationsCore
# @author Nick Alekhine
# @version 11-11-2014 (DD-MM-YYYY)

# -----------------------------------------------------------------------------
# IMPORTS
# -----------------------------------------------------------------------------

from nose.tools import *
import sys
sys.path.append('../../src')
from operationsCore import OperationsCore

# -----------------------------------------------------------------------------
# TESTS
# -----------------------------------------------------------------------------

# tests OperationsCore class
class TestOperationsCore:

  ocore1 = OperationsCore(1, 1)
  ocore2 = OperationsCore(2.5, 75000)
  ocore3 = OperationsCore(5, 10)

  args1 = ['i', 'am', 'stupid']
  args2 = ['this', 'is', 'bad']
  args3 = ['./dan', '-f', '../assets/D1/curieuse.mp3', '-d', '../assets/D2/']

  def reset( self ):
    self.ocore1 = OperationsCore(1, 1)
    self.ocore2 = OperationsCore(2.5, 75000)
    self.ocore3 = OperationsCore(5, 10)

    self.args1 = ['i', 'am', 'stupid']
    self.args2 = ['this', 'is', 'bad']
    self.args3 = ['./dan', '-f', '../assets/D1/curieuse.mp3', '-d', '../assets/D2/']

  @raises( SystemExit )
  def testSetArguments1( self ):
    self.reset()
    self.ocore1.setArguments( self.args1 )
  
  @raises( SystemExit )
  def testSetArguments2( self ):
    self.reset()
    self.ocore1.setArguments( self.args2 )

  def testSetArguments3( self ):
    self.reset()
    self.ocore1.setArguments( self.args3 )
    assert_equals( self.ocore1.getUsersMode(), 0 )
    assert_equals( self.ocore1.getAdsMode(), 1 )
    assert_equals( self.ocore1.getUsersDir(), '../assets/D1/curieuse.mp3' )
    assert_equals( self.ocore1.getAdsDir(), '../assets/D2/' )

  def testConvertFiles( self ):
    self.reset()
    self.ocore1.setArguments( self.args3 )
    self.ocore1.convertFiles()
    assert_equals(os.path.exists('./tmp/Users/curieuse.mp3'), True)