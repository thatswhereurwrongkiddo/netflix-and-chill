#Netflix and Chill weight.py
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
#
#do you want to start the game again?
#i'm listening to WEIGHT while coding this right now
#probably not a good song choice bc i keep getting distracted and singing
#but fuck it
import os
import time

os.system('cls')

print('Would you like to perform another search?(Y/N)')
yesno = input('')



if yesno == ('Y'):
    #!!!!!!!!FIX ME BEFORE 1.1 PRODUCTION RELEASE!!!!!!!!!!!
    #os.system('cd C:/Users/noaht/Desktop/Netflix and Chill/source files/')
    os.system('python sources/splash.py')
elif yesno == ('N'):
    os.system('cls')
    print('Goodbye! See you next time!')
    time.sleep(1.5)
    pass
