#tests for Adder.

from nose.tools import *
from os import listdir, path
import sys
sys.path.append('../../src')
from operationsCore import OperationsCore
import helpers.processor as processor
import helpers.adder as adder
import helpers.copyconvert as copyconvert
from recordings.recording import Recording
from os import makedirs
from shutil import rmtree


class TestAdder:

  #
  # FIXTURES
  #

  f1 = '../assets/D1/bad0616.wav'
  core = OperationsCore(2.5,1)

  d1 = './tmp/users/'
  d2 = './tmp/ads/'

  def reset( self ):
    self.implode()
    makedirs(self.d1)
    makedirs(self.d2)
    
    self.f1 = '../assets/D1/bad0616.wav'
    self.core = OperationsCore(2.5, 1)
    self.core.setAdsDir( self.f1 )
    self.core.setModes( 0, 0 )

    copyconvert.copyConvert( self.f1, self.d2 )

  def implode( self ):
    if (path.exists( self.d1 )):
      rmtree( self.d1 )
    if (path.exists( self.d2 )):
      rmtree( self.d2 )

  #
  # METHODS
  #

  def testAdder( self ):
    self.reset()
    adder.add(self.core)
    rec1 = Recording( 'bad0616.wav', self.f1 )
    hashVal = rec1.hash()
    assert_equal( self.core.recDB.recordingsDB[hashVal].fragments, processor.process(self.f1)  )

