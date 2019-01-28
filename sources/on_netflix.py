#Netflix and Chill on_netflix.py
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
#Last file update on 01.23.2019

##FIX IMPORT LOOP

import ncimports
import os
import time
from splash import cursor

print("""So you wanna see if your movie is on Netflix?
Well, you've come to the right place!
""")
net_movie = input("Type the name of the movie you would like to check: ")

ncimports.clearscreen()

sql_command = ("SELECT movie, on_netflix FROM movies WHERE movie='{0}'".format(net_movie.title()))
cursor.execute(sql_command)
ncimports.clearscreen()
print('Loading...')
time.sleep(1)
ncimports.clearscreen()

print('Results for your search:')
print ('')

ncimports.fetchall()

input("Continue?")


#weight.py rewrite for on_netflix
#because weight.py prompts user to on_netflix
ncimports.clearscreen()
print('Would you like to perform another search? (Y/N)')
yesno = input('')

#if/else statement on whether to restart or terminate program
if yesno.upper() == ('Y'):
    os.system('python splash.py')
elif yesno.upper() == ('N'):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Goodbye! See you next time!')
    time.sleep(1.5)
