# @module: checker
# @description: checks files against the database and compares them to matches
# @version: 31-10-2014

# -----------------------------------------------------------------------------
# imports
from os import listdir
from os.path import isfile, join
from processor import process
from copyconvert import copyFile, convertFile
import math

# -----------------------------------------------------------------------------
# check()
# @description: checks all files in user recordings against political
#               recordings in an attempt to find matches.
def check( core ):
  message = ''

  for userRec in core['database']['userRecs']:
    for adRec in core['database']['adRecs']:
      message += compare( userRec, adRec )

  # remove last /n from message
  message = message[:-2]
  return message

# -----------------------------------------------------------------------------
# compare()
# @user
# @ad
# @description:
def compare( user, ad ):
  # extensionMatch = user['fileExtension'] == ad['fileExtension']
  threshold = 75000
  userFftLength = len(user['fft'])
  adFftLength = len(ad['fft'])

  # if ( extensionMatch ):
  if userFftLength == adFftLength:
    i = 0
    j = 0
    while i < userFftLength and i < adFftLength:
      j = 0
      fragLenUser = len(user['fft'][i])
      fragLenAd   = len(ad['fft'][i])
      while j < fragLenUser and j < fragLenAd:
        userAmplitude = user['fft'][i][j].real
        adAmplitude = ad['fft'][i][j].real
        if math.fabs(userAmplitude - adAmplitude) > threshold:
          return ''
        j += 1
      i += 1
    return 'MATCH: ' + user['filename'] + ' ' + ad['filename'] + '\n'
  return ''

