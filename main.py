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
from parser import parse


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

# Initialize Data-Base Struct:
OCore['DBase'] = {}

# Main function, acts based upon OCore['Mode']
OCore = parse(OCore)
if OCore['Mode1'] == 0 and OCore['Mode2'] == 0:
	#OCore = validateAll(OCore)
        #OCore = addAll(OCore)
	#OCore = checkAll(OCore)
	#OCore = printLog(OCore)
	# return None
  print 'Something is gonna happen'
#elif OCore['Mode'] == 1:
else:
	print "ERROR: Invalid Mode"
