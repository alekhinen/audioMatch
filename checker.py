# @module: checker
# @description: checks files against the database and compares them to matches
# @version: 31-10-2014

# -----------------------------------------------------------------------------
# imports
from os import listdir
from os.path import isfile, join
from processor import process
from copyconvert import copyFile, convertFile

# -----------------------------------------------------------------------------
# check()
# @description: checks all files in user recordings against political
#               recordings in an attempt to find matches.
def check( core ):
  message = ''

  for userRec in core['database']['userRecs']:
    for adRec in core['database']['adRecs']:
      message += compare( userRec, adRec )

  return message

# -----------------------------------------------------------------------------
# compare()
# @user
# @ad
# @description:
def compare( user, ad ):
  if ( user['fileExtension'] == ad['fileExtension'] ):
    return 'MATCH: ' + user['filename'] + ad['filename'] + '\n'
  else:
    return ''

