-------------
 Description
-------------

Dan is a prototype app for the Software Development semester project.
Dan was created to fulfill the requirements of Assignment 4, listed here:

http://www.ccs.neu.edu/course/cs4500f14/assignment4.txt

Dan is an audio recognition software designed to detect the use
of copyright protected music in digital audio and video media. The 
full version of this software will be able to scan large collections
of multuiple file types and search for multiple potential violations. 
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

Enter the assignment4 directory and run the Dan app with the command(s)
listed in 'Command Line Arguments' section below.

------------------------
 Command Line Arguments
------------------------
 
Form: ./dan -f file1 -f file2

file1.wav and file2.wav should be Linux pathnames that end in '.wav'

Example: ./dan -f /audio/politicalAd.wav -f /songs/oldRoad.wav

This example is assuming the directories 'audio' and 'songs' have 
been added to the project directory.

--------
 Output
--------

If the two files are found to sound similar, the program will print
"Match" to the command line and terminate with an exit status of 0.

If the two files are found to NOT sound similar, the program will print
"No Match" to the command line and terminate with an exit status of 0.

The following Errors may occur:


--------------
 Python Files
--------------

-------
 Tests
-------

-----------
 Libraries
-----------
The following Python libraries were used:

1. NumPy

2. SciPy

-----------
 Algorithm
-----------