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
  # TODO: these need to be tested.
  #   - ./dan -f z01.wav -f /course/cs4500f14/Assignments/A4/z01.wav
  #     - returns MATCH z01.wav z01.wav
  #   - ./dan -f z01.wav -f z02.wav
  #     - returns MATCH z01.wav z02.wav
  #   - ./dan -f z02.wav -f z03.wav
  #     - returns NO MATCH
  #   - ./dan -f z03.wav -f z04.wav
  #     - returns MATCH z03.wav z04.wav
  #   - ./dan -f z04.wav -f z05.wav
  #     - returns NO MATCH
  #   - ./dan -f z05.wav -f z06.wav
  #     - returns MATCH z05.wav z06.wav
  #   - ./dan -f z06.wav -f z07.wav
  #      - returns NO MATCH
  #   - ./dan -f z07.wav -f z08.wav
  #      - returns MATCH z07.wav z08.wav
  #   - ./dan -f z05.wav -f Sor3508.wav
  #     - returns NO MATCH

  files = ['../audio/bad0616.wav', '../audio/z06.wav']
  assert_equal( comparator.parseAndCompare( files ), 'NO MATCH' )

  files = ['../audio/z01.wav', '../audio/z02.wav']
  assert_equal( comparator.parseAndCompare( files ), 'MATCH z01.wav z02.wav' )

  files = ['../audio/z01.wav', '../audio/z06.wav']
  assert_equal( comparator.parseAndCompare( files ), 'NO MATCH' )
