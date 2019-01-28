#Netflix and Chill hello.py
#
#encoded in UTF-8
#
#distributed under The MIT License:
#
#The MIT License (MIT)
#
#Copyright (c) 2018-2019 thatswhereurwrongkiddo
#
#Permission is hereby granted, free of charge, to any person obtaining a
#copy of this software and associated documentation files (the "Software"),
#to deal in the Software without restriction, including without limitation
#the rights to use, copy, modify, merge, publish, distribute, sublicense,
#and/or sell copies of the Software, and to permit persons to whom the
#Software is furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#DEALINGS IN THE SOFTWARE.
#
#Last file update on 01.21.2019

'''
hello.py

This is the jumping off point of the entire Netflix and Chill program.
This is the initial page the user (you!) sees when starting the program, and
redirects the user to the other parts of the Netflix and Chill program.
'''

#import modules
import os
from splash import cursor
import time
import platform
import ncimports

#define platform identifying vars
platsys = platform.system()
platrel = platform.release()
platdist = platform.dist()

#print intro screen
print("""Welcome to Netflix and Chill v1.2

Designed with love by github user thatswhereurwrongkiddo
""")

#if/else statement for displaying system version
#i had to make this due to macOS technically being Darwin OS,
#and identifying itself as such when using the traditional
#platform.###() modules
if platsys == "Darwin":                                          ##############################################
    macosv = os.system("/usr/bin/sw_vers")                       # not 100% sure how well this works on macOS #
    print("Running on macOS {0}".format(macosv))                 ########### if it even works at all ##########
                                                                 ##### i promise i'll have it tested soon #####
                                                                 ##############################################
if platsys == "Linux":
    lin_dist = "{0} {1}".format(platdist[0], platdist[1])
    print("Running on {0} (Linux)".format(lin_dist))
else:
    print("Running on {0} {1}".format(platsys, platrel))

#ask user which way they would like to select movie
#genre -> genre.py -> weight.py
#release year -> release.py -> weight.py
#imdb rating -> imdb.py -> weight.py
print("""
How would you like to select your movie?

Options are:

Genre
Release Year
IMDb Rating

""")
db_selection = input('And you pick...?: ')

ncimports.clearscreen()

#if/else statement sending user to selection of their choice
if db_selection.lower() == ('genre'):
    import genre
elif db_selection.lower() == ('release year'):
    import release
elif db_selection.lower() == ('imdb rating'):
    import imdb
else:
    import progfail
