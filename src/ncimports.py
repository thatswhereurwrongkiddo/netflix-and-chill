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
    if result == []:
        print("No Results Found :(")
    else:
        for r in result:
            print(r[0], "({0})".format(r[1]))
#shortcut for result fetching in on_netflix.py
def fa_onnet():
    result = cursor.fetchall()
    result0 = result[0]
    if result == []:
        print("No Results Found :(")
    else:
        if result0[1] == "True":
            print("{0} is on Netflix!".format(result0[0]))
            print("")
        elif result0[1] == "False":
            print("{0} is not on Netflix. :(".format(result0[0]))
#shortcut for result fetching in genre.py
def fa_genre():
    result = cursor.fetchall()
    if result == []:
        print("No Results Found :(")
    else:
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
#i made this fix after realizing that movies like BASEketball
#didn't play nice with my original on_netflix setup
#it took me hours
#but i finally did it
def baseketballfix():
    net_movie = input("Type the name of the movie you would like to check: ")
    execute = cursor.execute("SELECT movie FROM movies")
    fetchall = cursor.fetchall()
    x=0
    while x < 21:
        if fetchall[x][0].lower() == net_movie:
            realmovie = fetchall[x][0]
            break
        else:
            x = x+1
            pass
    clearscreen()

    sql_command = ("SELECT movie, on_netflix FROM movies WHERE movie='{0}'".format(realmovie))
    cursor.execute(sql_command)
    clearscreen()
    print('Loading...')
    time.sleep(1)
    clearscreen()

    print('Results for your search:')
    print ('')

    fa_onnet()
