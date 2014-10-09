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
between two wav files.  


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
 
Command Form: ./dan -f file1 -f file2

file1.wav and file2.wav should be Linux pathnames that end in '.wav'

Example: ./dan -f /audio/politicalAd.wav -f /songs/oldRoad.wav

This example is assuming the directories 'audio' and 'songs' have 
been added to the project directory.


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

When one of the file pathnames is incorrect -
"ERROR: One (or both) of the files supplied does not exist!"
followed by a newline will print to the command line.

When one of the files is not in .wav format -
"ERROR: One (or both) of the files supplied is not in WAV format"
followed by a newline will print to the command line.

When there is an issue with command line argument syntax -
"Error: incorrect command line" 
followed by a newline will print to the command line.


------------------
 Project Contents
------------------

The project should contain the following files:

audio         - (directory) a collection of files for test purposes
tests         - (directory) a collection of test scripts
.gitignore    - (GITIGNORE file) a file to tell GitHub which files to version 
README.md     - (MD file) a readme for the github project
README.txt    - (txt file) a readme for the dan app
validator.py  - (Python file) validates pathname and .wav formats of files 
comparator.py - (Python file) compares the two parsed files
parser.py     - (Python file) parses files using SciPy functions
dan           - (file) executable file to take the arguments and run the app 


-----------
 Libraries
-----------

The following Python libraries were used:

math
os.path
sndhdr
sys
NumPy
SciPy


-------
 Tests
-------


-----------
 Algorithm
-----------