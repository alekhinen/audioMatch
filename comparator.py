from parser import parseFiles


def parseAndCompare(f1, f2):
  f1, f2 = parseFiles(f1, f2)
  return compareFiles(f1, f2)


def compareFiles(f1, f2):
  result = 'MATCH'

  if ( len(f1) == len(f2) ):
    for i in range(0, len(f2) / 2):
      if ( f1[i] != f2[i] ):
        result = 'NO MATCH'
  else:
    result = 'NO MATCH'

  print result
