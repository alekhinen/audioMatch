import os.path
import sndhdr

# Check if both files exist and are in .wav format.
# returns [isValid, errMsg, exitStatus]
def validateFiles( files ):
  if ( len(files) == 2 ):
    f1 = files[0]
    f2 = files[1]
  else:
    msg = 'ERROR: two files must be supplied\n'
    return [False, msg, 1]

  # check if files exist
  if ( not (os.path.isfile(f1) and os.path.isfile(f2)) ):
    msg = 'ERROR: '
    if ( not os.path.isfile(f1) ):
      msg += f1 + ' is not a valid file path\n'
    else:
      msg += f2 + ' is not a valid file path\n'
    return [False, msg, 1]

  # get the headers of the files
  f1Header = sndhdr.what(f1)
  f2Header = sndhdr.what(f2)

  # check if the headers exist
  if ( f1Header == None or f2Header == None ):
    msg = 'ERROR: '
    if ( f1Header == None ):
      msg += os.path.basename( f1 ) + ' is not a supported format\n'
    else:
      msg += os.path.basename( f2 ) + ' is not a supported format\n'
    return [False, msg, 2]
  # check if the files are in WAV format
  elif ( f1Header[0] != 'wav' or f2Header[0] != 'wav' ):
    msg = 'ERROR: '
    if ( f1Header[0] != 'wav' ):
      msg += os.path.basename( f1 ) + ' is not a supported format\n'
    else:
      msg += os.path.basename( f2 ) + ' is not a supported format\n'
    return [False, msg, 2]
  else:
    return [True, '', 0]
