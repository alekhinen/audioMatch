# @module: adder
# @description: The Adder module, moves all validated files to tmp folders
#               and then adds them to the database.
# @version: 31-10-2014

# -----------------------------------------------------------------------------
# imports
from os          import listdir
from os.path     import isfile, join, basename
from processor   import process
from copyconvert import copyFile, convertFile
from sndhdr      import what
from os          import makedirs

# -----------------------------------------------------------------------------
# add()
# @description: Adds all the files in the user directory to the tmp directory
#               converts them and then adds them to the Database.
def add( core ):
  result = core

  # generate directories
  makedirs('./tmp/userRecs/')
  makedirs('./tmp/adRecs/')

  # file mode
  if ( core['Mode1'] == 0 ):
    f = result['U_Dir']
    result['database']['userRecs'].append( subAdd(f, 0) )
  
  # directory mode
  if ( core['Mode1'] == 1 ):
    # converts/copies over user recordings to a tmp folder.
    # fft's user recordings and adds data to OCore database.
    for f in listdir(result['U_Dir']):
      f = join( result['U_Dir'], f )
      result['database']['userRecs'].append( subAdd(f, 0) )

  # file mode
  if ( core['Mode2'] == 0 ):
    f = result['A_Dir']
    result['database']['adRecs'].append( subAdd(f, 1) )

  # directory mode
  if ( core['Mode2'] == 1 ):
    # same as above, but for advertisement recordings.
    for f in listdir(result['A_Dir']):
      f = join( result['A_Dir'], f )
      result['database']['adRecs'].append( subAdd(f, 1) )

  return result, ''

# -----------------------------------------------------------------------------
# subAdd()
# @filepath: path to a file (absolute or relative)
# @stage: 0 (users directory) or 1 (ads directory)
# @description: copies over file, converts that file, fft's that file
# @return: fft'd audio data
def subAdd( filepath, stage ):
  # if file is mp3, convert it
  if ( what( filepath ) == None ):
    convertFile( filepath, stage )
  # else, just copy it over
  else:
    copyFile( filepath, stage )

  # if in user recordings stage, process the file in the user's tmp dir
  if stage == 0:
    tmpF = join( './tmp/userRecs/', basename(filepath) )
  elif stage == 1:
    tmpF = join( './tmp/adRecs/', basename(filepath) )
  return process( tmpF )



