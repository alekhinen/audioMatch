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

# Initialize Operation Struct:
OCore = {
    'U_Dir':"..",
    'A_Dir':".",
    'Mode':0
    'Threshold':100
    'FSize':0.5
    'FlatR':0.8
    'DBase':{}
    'Log':[]}

# Initialize Data-Base Struct:
OCore['DBase'] = {}

# Main function, acts based upon OCore['Mode']
#parse(OCore)
if OCore['Mode'] == 0:
	#addAll(OCore)
	#checkAll(OCore)
	#printLog(OCore)
	return None
#elif OCore['Mode'] == 1:
else:
	print "ERROR: Invalid Mode"
