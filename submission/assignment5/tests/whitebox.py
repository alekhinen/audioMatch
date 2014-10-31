from nose.tools import *
from assignment4 import parser
from assignment4 import validator
from assignment4 import logger
from os import listdir
# -----------------------------------------------------------------------------
# tests the parser
class TestParser():

  # -------------------------------------------------------
  # attributes
  OCore = None

  # -------------------------------------------------------
  # setUp()
  def setUp( self ):
    print 'setting up'

    self.OCore = {
      'U_Dir':"..",
      'A_Dir':".",
      'Mode1': 0,
      'Mode2': 0,
      'Stage': 0,
      'Threshold':100,
      'FSize':2.5,
      'FlatR':0.8,
      'DBase':{},
      'Log':[]
    }

  # -------------------------------------------------------
  # testCheckTag()
  def testCheckTag( self ):
    assert_equal( parser.checkTag('-f'), 0 )
    assert_equal( parser.checkTag('-d'), 1 )
    assert_equal( parser.checkTag('asdfljksadf'), -1 )
    assert_equal( parser.checkTag(''), -1 )

  # -------------------------------------------------------
  # testParse()
  def testParse( self ):
    # TEST 1
    # setting up what the core should look like after parser.parse()
    expectedCore = self.OCore
    expectedCore['U_Dir'] = 'test_assets/D1'
    expectedCore['Mode1'] = 1
    expectedCore['A_Dir'] = 'test_assets/D2'
    expectedCore['Mode2'] = 1
    # setting up fake system arguments
    inputArgs = ['', '-d', 'test_assets/D1', '-d', 'test_assets/D2']
    assert_equal( parser.parse(self.OCore, inputArgs), (expectedCore, '') )

    # TEST 2
    inputArgs = ['']
    err = 'ERROR: Exactly two sets of flags and paths have to be specified.'
    assert_equal( parser.parse(self.OCore, inputArgs), (self.OCore, err) )

    # TEST 3
    inputArgs = ['', '-d', 'test_assets/D1', '-zasd', 'test_assets/D2']
    err = 'ERROR: improper flagtype supplied.'
    assert_equal( parser.parse(self.OCore, inputArgs), (self.OCore, err) )


# -----------------------------------------------------------------------------
# tests the validator
class TestValidator():

  # -------------------------------------------------------
  # attributes
  OCore = None

  # -------------------------------------------------------
  # setUp()
  def setUp( self ):
    print 'setting up'

    self.OCore = {
      'U_Dir':"..",
      'A_Dir':".",
      'Mode1': 0,
      'Mode2': 0,
      'Stage': 0,
      'Threshold':100,
      'FSize':2.5,
      'FlatR':0.8,
      'DBase':{},
      'Log':[]
    }

  # -------------------------------------------------------
  # testValidateFile()
  def testValidateFile( self ):
    # Test 1
    f = '../test_assets/D1/bad0616.wav'
    assert_equal( validator.validateFile( f ), True )
    # Test 2
    f = ''
    assert_equal( validator.validateFile( f ), False )
    # Test 3 TODO if below is acceptable remove this and test 1.
    f = '../test_assets/D1/janacek.mp3'
    assert_equal( validator.validateFile( f ), True )

    # Tests TODO is this acceptable?
    f = '../test_assets/D1/'
    for fileName in listdir( f ):
      f2 = join( f, fileName)
      assert_equal(validator.validateFile( f ), True )


  # -------------------------------------------------------
  # testValidateDir()
  def testValidateDir( self ):
    # Test 1
    d = '../test_assets/D1'
    assert_equal( validator.validateDir( d ), True )
    # Test 2
    d = '../test_assets/D2'
    assert_equal( validator.validateDir( d ), True )
    # Test 3
    d = '../dist'
    assert_equal( validator.validateDir( d ), False )
    # Test 4
    d = '/Something/Stupid'
    assert_equal( validator.validateDir( d ), False )

  # -------------------------------------------------------
  # testValidate()
  def testValidate( self ):
    msg = 'ERROR: flagged a directory that was not a directory OR flagged a file that was not a file'

    # Valid Cores -------------------------------------------------------------
    self.OCore['U_Dir'] = '../test_assets/D1'
    self.OCore['A_Dir'] = '../test_assets/D2'
    self.OCore['Mode1'] = 1
    self.OCore['Mode2'] = 1

    assert_equal( validator.validate( self.OCore ), (self.OCore, ''))

    self.OCore['U_Dir'] = '../test_assets/D1/bad0616.wav'
    self.OCore['A_Dir'] = '../test_assets/D2'
    self.OCore['Mode1'] = 0
    self.OCore['Mode2'] = 1

    assert_equal( validator.validate( self.OCore ), (self.OCore, ''))

    self.OCore['U_Dir'] = '../test_assets/D1'
    self.OCore['A_Dir'] = '../test_assets/D2/janacek2.wav'
    self.OCore['Mode1'] = 1
    self.OCore['Mode2'] = 0

    assert_equal( validator.validate( self.OCore ), (self.OCore, ''))

    self.OCore['U_Dir'] = '../test_assets/D1/bad0616.wav'
    self.OCore['A_Dir'] = '../test_assets/D2/janacek2.wav'
    self.OCore['Mode1'] = 0
    self.OCore['Mode2'] = 0

    assert_equal( validator.validate( self.OCore ), (self.OCore, ''))

    # Invalid Cores -----------------------------------------------------------
    self.OCore['U_Dir'] = '../test_assets/D1'
    self.OCore['A_Dir'] = '../test_assets/D2'
    self.OCore['Mode1'] = 0
    self.OCore['Mode2'] = 1

    assert_equal( validator.validate( self.OCore ), (self.OCore, msg))

    self.OCore['U_Dir'] = '../test_assets/D1/bad0616.wav'
    self.OCore['A_Dir'] = '../test_assets/D2'
    self.OCore['Mode1'] = 1
    self.OCore['Mode2'] = 1

    assert_equal( validator.validate( self.OCore ), (self.OCore, msg))

    self.OCore['U_Dir'] = '../test_assets/D1'
    self.OCore['A_Dir'] = '../test_assets/D2/janacek2.wav'
    self.OCore['Mode1'] = 0
    self.OCore['Mode2'] = 1

    assert_equal( validator.validate( self.OCore ), (self.OCore, msg))

    self.OCore['U_Dir'] = '../test_assets/D1/bad0616.wav'
    self.OCore['A_Dir'] = '../test_assets/D2/janacek2.wav'
    self.OCore['Mode1'] = 1
    self.OCore['Mode2'] = 1

    assert_equal( validator.validate( self.OCore ), (self.OCore, msg))
    
class testProcessor():
      
  result = None

  def setUp( self ):
    print "setting up"

    self.result = {
      'filename': "",
      'fileExtension': "wav",
      'samplingRate': 0,
      'channels': 0,
      'bitsPerSamp': 0,
      'fft': [],
    }
      
    def testProcess( self ):
      address = '../test_assets/D1/bad0616.wav'
      self.result['filename'] = 'bad0616'
      self.result['fileExtension'] = 'wav'
      self.result['samplingRate'] = 44000
      self.result['channels'] = 1
      self.result['bitsPerSamp'] = 16
      
      assert_equal( processor.process( address )['filename'],
      self.result['filename'])
  
      assert_equal( processor.process( address )['channels'], 1 )















