# Logger
# Outputs text to command-line
#
# @author Nick Alekhine
# @author Michael Chadbourne
# @author John Meenagh
# @author Charles Perrone
#
# @version 2014-10-29

# -----------------------------------------------------------------------------
# imports
import sys

# -----------------------------------------------------------------------------
# log()
def log( output ):
  if output:
    if 'ERROR:' in output:
      print output
      sys.exit(1)
    else:
      print output

