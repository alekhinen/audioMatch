from parser import parseFiles
import math
import os.path


def parseAndCompare( files ):
  f1, f2 = parseFiles(files[0], files[1])
  f1_name = os.path.basename(files[0])
  f2_name = os.path.basename(files[1])

  return compareFiles(f1, f2, f1_name, f2_name)


def compareFiles(f1, f2, f1_name, f2_name):
  result = 'MATCH ' + f1_name + ' ' + f2_name + '\n'
  # Set minimum amplitude difference we care about
  THRESHOLD = 500000

  if ( len(f1) == len(f2) ):
    for i in range(0, len(f2) / 2):
      abs_f1 = math.fabs(f1[i].real)
      abs_f2 = math.fabs(f2[i].real)

      if ( math.fabs(abs_f1 - abs_f2) > THRESHOLD):
        result = 'NO MATCH\n'
  else:
    result = 'NO MATCH\n'

  print result
