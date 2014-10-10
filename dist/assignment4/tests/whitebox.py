from nose.tools import *
from assignment4 import validator
from assignment4 import comparator

def testValidateFiles():
    # non-existent files ------------------------------------------------------
    files = ['../audio/zoobat.wav', 'sees.wav']
    assert_equal(validator.validateFiles( files ),
      [False, 'ERROR: ../audio/zoobat.wav is not a valid file path\n', 1])

    files = ['../audio/z01.wav', 'sees.wav']
    assert_equal(validator.validateFiles( files ),
      [False, 'ERROR: sees.wav is not a valid file path\n', 1])

    # non-wav files -----------------------------------------------------------
    files = ['../audio/bad_guy_in_yer_bar.mp3', '../audio/Sor3508.mp3']
    assert_equal(validator.validateFiles( files ),
      [False, 'ERROR: bad_guy_in_yer_bar.mp3 is not a supported format\n', 2])

    files = ['../audio/z01.wav', '../audio/Sor3508.mp3']
    assert_equal(validator.validateFiles( files ),
      [False, 'ERROR: Sor3508.mp3 is not a supported format\n', 2])

    # existent filepaths and wav files ----------------------------------------
    files = ['../audio/z01.wav', '../audio/z02.wav']
    assert_equal(validator.validateFiles( files ), [True, '', 0])

def testComparator():

  files = ['../audio/z01.wav', '../audio/z02.wav']
  assert_equal( comparator.parseAndCompare( files ), 'MATCH z01.wav z02.wav' )

  files = ['../audio/z02.wav', '../audio/z03.wav']
  assert_equal( comparator.parseAndCompare( files ), 'NO MATCH' )

  files = ['../audio/z03.wav', '../audio/z04.wav']
  assert_equal( comparator.parseAndCompare( files ), 'MATCH z03.wav z04.wav' )

  files = ['../audio/z04.wav', '../audio/z05.wav']
  assert_equal( comparator.parseAndCompare( files ), 'NO MATCH' )

  files = ['../audio/z05.wav', '../audio/z06.wav']
  assert_equal( comparator.parseAndCompare( files ), 'MATCH z05.wav z06.wav' )

  files = ['../audio/z06.wav', '../audio/z07.wav']
  assert_equal( comparator.parseAndCompare( files ), 'NO MATCH' )

  files = ['../audio/z07.wav', '../audio/z08.wav']
  assert_equal( comparator.parseAndCompare( files ), 'MATCH z07.wav z08.wav' )

  files = ['../audio/z05.wav', '../audio/Sor3508.wav']
  assert_equal( comparator.parseAndCompare( files ), 'NO MATCH' )

