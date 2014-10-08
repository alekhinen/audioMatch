from assignment4 import validator
from assignment4 import comparator
from assignment4 import parser
from assignment4 import audio

from nose.tools import *

def test_validateFiles():
	assert_equal(validator.validateFiles('zo1.wav', 'sees.wav'), False)
	#assert_equal(validator.validateFiles('zo1.wav', 'zo2.wav'), True)
	#assert_equal(validator.validateFiles('zo3.wav', 'zo4.wav'), True)

def test_parseFiles():
	assert_equal(parser.parseFiles('z01.wav', 'z02.wav'), True)
