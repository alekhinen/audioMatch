import os.path
import sndhdr
import sys

# Check if both files exist and are in .wav format.
def validateFiles( files ):
  if ( len(files) == 2 ):
    f1 = files[0]
    f2 = files[1]
  else:
    return False

  # check if files exist
  if ( not (os.path.isfile(f1) and os.path.isfile(f2)) ):
    msg = 'ERROR: One (or both) of the files supplied does not exist!\n'
    msg += 'EXIT STATUS: 1\n'
    sys.stderr.write( msg )
    return False

  # get the headers of the files
  f1Header = sndhdr.what(f1)
  f2Header = sndhdr.what(f2)

  # check if the headers exist
  if ( f1Header == None or f1Header == None ):
    msg = 'ERROR: One (or both) of the files supplied is not in WAV format\n'
    msg += 'EXIT STATUS: 2\n'
    sys.stderr.write( msg )
    return False
  # check if the files are in WAV format
  elif ( f1Header[0] != 'wav' or f2Header[0] != 'wav' ):
    msg = 'ERROR: One (or both) of the files supplied is not in WAV format\n'
    msg += 'EXIT STATUS: 1\n'
    sys.stderr.write( msg )
    return False
  else:
    return True
