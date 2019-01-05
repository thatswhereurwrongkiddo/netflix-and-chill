#Netflix and Chill genre.py
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

print("Which genre would you like to watch?")
print("""
Genre List:

Action (1)
Thriller (2)
Drama (3)
Fantasy (4)
Comedy (5)
""")
num_genre = input("Type Selection (Enter Selection Number):")
if num_genre == ('1'):
    real_genre = 'Action'
elif num_genre == ('2'):
    real_genre = 'Thriller'
elif num_genre == ('3'):
    real_genre = 'Drama'
elif num_genre == ('4'):
    real_genre = 'Fantasy'
elif num_genre == ('5'):
    real_genre = 'Comedy'


sql_command = ('SELECT movie, genre FROM movies WHERE genre = "{0}"'.format(real_genre))
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
