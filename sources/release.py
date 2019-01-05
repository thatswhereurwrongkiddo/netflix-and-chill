#Netflix and Chill release.py
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
#Last file update on 01.04.2019

from splash import cursor
import os
import time

print("""How would you like to select your movie?

By specific release year? (1)
By release date before specific year (i.e. Movies released after 2010) (2)
By release date after specific year (i.e. Movies released before 2010) (3)

""")

year_option = input('Type the number of your selelction: ')

os.system('cls')

if year_option == ('1'):

    print("""Which release year would you like to see a movie from?

Options:

1977
1997
2007
2008
2010
2011
2015
2016
2017
""")

    num_year = input('Type Selection: ')

    sql_command = ('SELECT movie, rel_year FROM movies WHERE rel_year = "{0}"'.format(num_year))
    cursor.execute(sql_command)
    os.system('cls')
    print('Loading...')
    time.sleep(1)
    os.system('cls')

    print('Results for your search:')
    print ('')

    result = cursor.fetchall()
    for r in result:
        print(r)

    time.sleep(1)
    print('Continue?')
    input('')
    import weight

elif year_option == ('2'):

    num_year = input('I would like to see a movie released before _____: ')
    sql_command = ('SELECT movie, rel_year FROM movies WHERE rel_year <= "{0}"'.format(num_year))
    cursor.execute(sql_command)
    os.system('cls')
    print('Loading...')
    time.sleep(1)
    os.system('cls')

    print('Results for your search:')
    print ('')

    result = cursor.fetchall()
    for r in result:
        print(r)

    time.sleep(1)
    print('Continue?')
    input('')
    import weight

elif year_option == ('3'):

    num_year = input('I would like to see a movie released after _____: ')
    sql_command = ('SELECT movie, rel_year FROM movies WHERE rel_year >= "{0}"'.format(num_year))
    cursor.execute(sql_command)
    os.system('cls')
    print('Loading...')
    time.sleep(1)
    os.system('cls')

    print('Results for your search:')
    print ('')

    result = cursor.fetchall()
    for r in result:
        print(r)

    time.sleep(1)
    print('Continue?')
    input('')
    import weight
