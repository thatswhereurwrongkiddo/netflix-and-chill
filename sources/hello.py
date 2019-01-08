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
#Last file update on 01.06.2019

import os
from splash import cursor
import time

print("""Welcome to Netflix and Chill v1.0.2

Designed with love by github user thatswhereurwrongkiddo
""")
print("""How would you like to select your movie?

Options are:

Genre (1)
Release Year (2)
IMDb Rating (3)

""")
db_selection = input('And you pick...? (Enter Selection Number): ')

os.system('cls')

if db_selection == ('1'):
    import genre
elif db_selection == ('2'):
    import release
elif db_selection == ('3'):
    import imdb
elif db_selection == ('4'):
    #awe look aren't you special
    #you found my hidden SQL insertion option
    #feel free to use it, i guess
    #
    #it's 1:34am and i have no internet and i'm super tired so i
    #really don't care about protecting this feature too hard
    #
    #have fun SQLing!
    sql_command = input('Enter SQL Command: ')
    cursor.execute(sql_command)
    os.system('cls')
    print('Loading...')
    time.sleep(1)
    os.system('cls')

    print('Results for the following SQL Command ({0}):'.format(sql_command))
    print ('')

    result = cursor.fetchall()
    for r in result:
        print(r)

    time.sleep(1)
    print('')
    input('Press ENTER to exit application')
else:
    import progfail
