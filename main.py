#!/usr/bin/env python
# AudioMG: MATCH GOOD!
# Created by:
# Nick Alekhine
# Michael Chadbourne
# John Meenagh
# Charles Perrone

# Designed to identify files in one directory with matching segments in
#     The other.

#Imports
from parser    import parse
from validator import validate
from adder     import add
from processor import process
from checker   import check
from logger    import log


# Initialize Operation Struct:
OCore = {
    'U_Dir':"..",
    'A_Dir':".",
    'Mode1': 0,
    'Mode2': 0,
    'Stage': 0,
    'Threshold':100,
    'FSize':2.5,
    'FlatR':0.8,
    'DBase':{},
    'Log':[]
}

# Main function, acts based upon OCore['Mode']
OCore, output = parse(OCore)
log(output)
OCore, output = validate(OCore)
log(output)
OCore, output = add(OCore)
log(output)
OCore, output = process(OCore)
log(output)
OCore, output = check(OCore)
log(output)


# if OCore['Mode1'] == 0 and OCore['Mode2'] == 0:
# 	#OCore = validateAll(OCore)
#         #OCore = addAll(OCore)
# 	#OCore = checkAll(OCore)
# 	#OCore = printLog(OCore)
# 	# return None
#   print 'Something is gonna happen'
# #elif OCore['Mode'] == 1:
# else:
# 	print "ERROR: Invalid Mode"