#Netflix and Chill splash.py
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
#Last file update on 02.03.2019

'''
splash.py

Simple, and invisible to the user, but holds the entire program together. splash.py
initializes the SQLite database connection that the entire program depends on to function.
'''

import sqlite3 as sqlite
import os


os.system('cls' if os.name == 'nt' else 'clear')

#begin initial SQL db connection and var initialization
connection = sqlite.connect("../deps/movie_db.db")
#
cursor = connection.cursor()
#move to hello.py

if __name__ == '__main__':
    import hello
