import os.path
import sndhdr
import sys

# Check if both files exist and are in .wav format.
def validateFiles( files ):
  if ( len(files) == 2 ):
    f1 = files[0]
    f2 = files[1]
  else:
    return false

  # make sure file exists
  result = os.path.isfile(f1) and os.path.isfile(f2)

  if ( not result ):
    sys.stderr.write('ERROR: One (or both) of the files supplied does not exist!\n')
    return result

  # make sure file is in .wav format
  result = result and sndhdr.what(f1)[0] == 'wav'
  result = result and sndhdr.what(f2)[0] == 'wav'

  if ( not result ):
    sys.stderr.write('ERROR: One (or both) of the files supplied is not in WAV format\n')
    return result

  return result

