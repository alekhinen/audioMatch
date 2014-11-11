# AudioMatch Testing Suite
# @description glassbox tests for src/parser
# @author Nick Alekhine
# @version 10-11-2014 (DD-MM-YYYY)

# -----------------------------------------------------------------------------
# IMPORTS
# -----------------------------------------------------------------------------

from nose.tools import *
import sys
sys.path.append('../../src')
import argParser as parser

# -----------------------------------------------------------------------------
# TESTS
# -----------------------------------------------------------------------------

# tests parser
class TestParser:

  # TODO more tests

  args1 = None
  args2 = None
  args3 = None
  args4 = None

  def reset( self ):
    self.args1 = ['i', 'am', 'dumb']
    self.args2 = ['this', 'is', 'not', 'legit']
    self.args3 = ['', '-f', '../assets/D1/rimsky.mp3', '-d', '../assets/D2']
    self.args4 = ['', '-d', '../assets/D1', '-d', '../assets/D2']

  # System Exit 1
  @raises( SystemExit )
  def testSystemExitOnParse1( self ):
    self.reset()
    parser.parse( self.args1 )
  # System Exit 2
  @raises( SystemExit )
  def testSystemExitOnParse2( self ):
    self.reset()
    parser.parse( self.args2 )

  # Legitimate values
  def testParse( self ):
    self.reset()
    assert_equals( parser.parse(self.args3), [0, '../assets/D1/rimsky.mp3', 1, '../assets/D2'] )
  