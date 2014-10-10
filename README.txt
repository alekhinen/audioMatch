-------------
 Description
-------------

Dan is a prototype app for the Software Development semester project.
Dan was created to fulfill the requirements of Assignment 4, listed here:

http://www.ccs.neu.edu/course/cs4500f14/assignment4.txt

Dan is an audio recognition software designed to detect the use
of copyright protected music in digital audio and video media. The 
full version of this software will be able to scan large collections
of multiple file types and search for multiple potential violations. 
For this prototype, the project scope is limited to detecting similarity
between two wav files of the same length.  


--------------
 Project Team
--------------

Nick Alekhine       - alekhine.n@husky.neu.edu
Michael Chadbourne  - chadbourne.m@husky.neu.edu
Charles Perrone     - perrone.c@husky.neu.edu
John Meenagh        - jpmeenagh@gmail.com

Github - https://github.com/alekhinen/assignment4


-------
 Setup
-------

After downloading the submission, unpack the .tar.gz file in 
the command line with the tar command:

	tar -zxvf assignment4.tar.gz

Enter the assignment4 directory with the cd command and run the 
Dan app with the command(s) listed in 'Command Line Arguments' section below.


------------------------
 Command Line Arguments
------------------------
 
Command Form: 

	./dan -f file1 -f file2

file1 and file2 should be Linux path names that end in '.wav'

Example: 

        ./dan -f /audio/z01.wav -f /audio/z02.wav

This example compares two test files from the 'audio' directory. The result
should be a match.


--------
 Output
--------

If the two files are found to NOT sound similar, the program will print
"No Match" followed by a newline to the command line and terminate with 
an exit status of 0.

If the two files are found to sound similar, the program will print
"Match" followed by a space, followed by the short name of the first file, 
followed by a space, followed by the short name of the second file, followed 
by a newline to the command line and terminate with an exit status of 0.

The following Errors may occur:

-If the command line input is not in the correct form-
Prints 'ERROR: two files must be supplied' followed by a newline with an
exit status of 1.

-if either file path does not exist-
Prints 'ERROR: <input argument> is not a valid file path' followed by a
newline with an exit status of 1. 

-If the file doesn't have a header or the header doesn't indicate .wav format-
Prints 'ERROR: <filename> is not a supported format' followed by a newline
with an exit status of 1.

------------------
 Project Contents
------------------

The project should contain the following files:

audio         - (directory) a collection of audio files for test purposes
tests         - (directory) a collection of test scripts
.gitignore    - (GITIGNORE file) an unnamed file to tell GitHub what to save
README.md     - (MD file) a readme for the github project
README.txt    - (txt file) a readme for the dan app
validator.py  - (PY file) validates file path and .wav formats of files 
comparator.py - (PY file) compares the two parsed files
parser.py     - (PY file) parses files using SciPy functions
dan           - (file) executable file to take the arguments and run the app
__init__.py   - (PY file) tells the Python where to import modules from    

-Contents of the 'tests' directory-
__init__.py   - (PY file) tells the Python where to import modules from
blackbox.py   - (PY file) script to run blackbox tests (currently not used)
custom.py     - (PY file) script to run custom tests (currently not used)
README.md     - (MD file) readme for the test scripts
whitebox.py   - (PY file) script to run whitebox tests

-contents of the 'audio' directory-
Sor3508.mp3            -(mp3 file) Sor Opus 35, Number 8(deliberately butchered)
bad_guy_in_yer_bar.mp3 -(mp3 file) bad guy in yer bar, by Baron Knoxburry

bad0616.wav  -(.wav file) 10-second extract (6, 16) from bad_guy_in_yer_bar.mp3
bad2131.wav  -(.wav file) 10-second extract (21, 31) from bad_guy_in_yer_bar.mp3
Sor1929.wav  -(.wav file) 10-second extract (19, 29) from Sor3508.mp3
Sor4959.wav  -(.wav file) 10-second extract (49, 59) from Sor3508.mp3
z01.wav      -(.wav file) bad0616.wav with noise added to low-order bits
z02.wav      -(.wav file) bad0616.wav with channels mixed (.9, .1, .1, .9)
z03.wav      -(.wav file) bad2131.wav with channels mixed (-.85, .14, .16, -.83)
z04.wav      -(.wav file) z03.wav converted to MP3 and back to WAVE
z05.wav      -(.wav file) Sor1929.wav with noise added and channels swapped
z06.wav      -(.wav file) Sor1929.wav with channels mixed (.9, -.1, -.1, .9)
z07.wav      -(.wav file) Sor4959.wav converted to MP3 and back to WAVE
z08.wav      -(.wav file) z07.wav with channels mixed (.8, .2, .25, .75)

-----------
 Packages
-----------

The following packages were used in addition to the Standard Python Library:

NumPy
SciPy
nose (tests)


-------
 Tests
-------

The 'tests' directory contains a file whitebox.py for whitebox testing. This 
file contains two functions which each run a set of tests to check file 
validation and comparison. The tests use the assert_equals function from the 
nose.tools library. The functions go through a series of test cases using
small example files from the 'audio' directory.

The tests can be run by cd'ing to the 'tests' directory and running the
following command:

	nosetests whitebox

-----------
 Algorithm
-----------