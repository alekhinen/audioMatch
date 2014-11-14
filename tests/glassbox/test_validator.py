# AudioMatch Testing Suite
# @description glassbox tests for src/helpers/validator
# @author Nick Alekhine, Charles Perrone
# @version 11-11-2014 (DD-MM-YYYY)

# -----------------------------------------------------------------------------
# IMPORTS
# -----------------------------------------------------------------------------

from nose.tools import *
import sys
sys.path.append('../../src')
import helpers.validator as validator

# -----------------------------------------------------------------------------
# TESTS
# -----------------------------------------------------------------------------

# tests validator
class TestValidator:

  args1 = None
  args2 = None
  args3 = None
  args4 = None

  def reset( self ):
    self.args1 = ['i', 'am', 'dumb', 'lol']
    self.args2 = ['this', 'is', 'not', 'legit']
    self.args3 = [0, '../assets/D1/rimsky.mp3', 1, '../assets/D2']
    self.args4 = [1, '../assets/D1', 1, '../assets/D2']

  # System Exit 1
  @raises( SystemExit )
  def testSystemExitOnIsValid1( self ):
    self.reset()
    validator.isValid( self.args1 )
  # System Exit 2
  @raises( SystemExit )
  def testSystemExitOnIsValid2( self ):
    self.reset()
    validator.isValid( self.args2 )

  # Test two folders
  def testIsValidFolders( self ):
    self.reset()
    assert_equals( validator.isValid(self.args4), True )
  
  # Test file and folder
  def testIsValidFileAndFolder( self ):
    self.reset()
    assert_equals( validator.isValid(self.args3), True )