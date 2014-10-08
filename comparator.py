from parser import parseFiles
import math


def parseAndCompare( files ):
  f1, f2 = parseFiles(files[0], files[1])
  return compareFiles(f1, f2)


def compareFiles(f1, f2):
  result = 'MATCH'
  THRESHOLD = 500000

  if ( len(f1) == len(f2) ):
    for i in range(0, len(f2) / 2):
      abs_f1 = math.fabs(f1[i].real)
      abs_f2 = math.fabs(f2[i].real)

      if ( math.fabs(abs_f1 - abs_f2) > THRESHOLD):
        result = 'NO MATCH'
  else:
    result = 'NO MATCH'

  print result
