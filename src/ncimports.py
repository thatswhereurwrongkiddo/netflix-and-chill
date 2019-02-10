#Netflix and Chill ncimports.py
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
#Last file update on 02.10.2019

'''
ncimports.py

This file holds some basic shortcuts used all around the
Netflix and Chill program starting in version 1.2.
'''

from splash import cursor
import os
import time

#shorcut for result fetching in imdb.py and release.py
def fetchall():
    result = cursor.fetchall()
    for r in result:
        print(r[0], "({0})".format(r[1]))
#shortcut for result fetching in on_netflix.py
def fetchall():
    result = cursor.fetchall()
    for r in result:
        if r[1] == "True":
            print("{0} is on Netflix!".format(r[0]))
            print("")
        if r[1] == "False":
            print("{0} is not on Netflix. :(".format(r[0]))
#shortcut for result fetching in genre.py
def fa_genre():
    result = cursor.fetchall()
    for r in result:
        print(r[0])
#shortcut for clearing terminal screen via os.system() module
def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear')
#shortcut for starting weight.py
def stweight():
    time.sleep(1)
    print("")
    print('Continue?')
    input('')
    import weight
