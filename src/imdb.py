#Netflix and Chill imdb.py
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
imdb.py

This program, when ran/imported, will allow you to select movies from the
SQLite database based on IMDb rating.
'''

#import required modules
from splash import cursor
import os
import time
import ncimports

#ask for user input for which way they would
#like to search using iMDB rating
print("""How would you like to select your movie?

Options:

IMDb rating greater than ___ (1)
IMDb rating less than ___(2)
""")

imdb_selection = input('Type selection number: ')

ncimports.clearscreen()

#if/else statement for whichever method was chosen by user
if imdb_selection == ('1'):
    #ask for user input for iMDB rating
    num_year = input('I would like to see a movie with an IMDb rating greater than _____: ')
    #initialize and execute SQL command variable with user input
    sql_command = ('SELECT movie, rating FROM movies WHERE rating >= "{0}"'.format(num_year))
    cursor.execute(sql_command)
    #clear screen and return results of SQL command
    ncimports.clearscreen()
    print('Loading...')
    time.sleep(1)
    ncimports.clearscreen()

    print('Results for your search:')
    print ('')

    ncimports.fetchall()

    #start weight.py
    ncimports.stweight()

if imdb_selection == ('2'):
    #ask for user input for iMDB rating
    num_year = input('I would like to see a movie with an IMDb rating less than _____: ')
    #initialize and execute SQL command variable with user input
    sql_command = ('SELECT movie, rating FROM movies WHERE rating <= "{0}"'.format(num_year))
    cursor.execute(sql_command)
    #clear screen and return results of SQL command
    ncimports.clearscreen()
    print('Loading...')
    time.sleep(1)
    ncimports.clearscreen()

    print('Results for your search:')
    print ('')

    ncimports.fetchall()

    #start wight.py
    ncimports.stweight()
