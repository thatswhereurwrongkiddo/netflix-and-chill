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
#Last file update on 02.03.2019
#
#do you want to start the game again?
#i'm listening to WEIGHT while coding this right now
#probably not a good song choice bc i keep getting distracted and singing
#but whatever

'''
weight.py

Named as such because I coded it while listening to the song WEIGHT by
BROCKHAMPTON, as shown in the comment above. This is another essential file for
the entire program as it is what either loops the user back to hello.py, or ends
the program, based on whichever the user decides to do.
'''
runprog=0
#import modules
import os
import time
import ncimports

#clear screen
os.system('cls' if os.name == 'nt' else 'clear')

while runprog == 0:
    #prompt on whether or not to go to on_netflix.py
    print("Would you like to check if your movie is on Netflix (Y/N)?")
    yesno_net = input("")

    #if/else statement on whether or not to open on_netflix.py
    if yesno_net.upper() == ("Y"):
        os.system("python on_netflix.py")
        break
    elif yesno_net.upper() == ("N"):
        ncimports.clearscreen()
        pass

    #ask user whether or not they would like to perform another search
    print('Would you like to perform another search? (Y/N)')
    yesno = input('')

    #if/else statement on whether to restart or terminate program
    if yesno.upper() == ('Y'):
        os.system('python splash.py')
    elif yesno.upper() == ('N'):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Goodbye! See you next time!')
        time.sleep(1.5)
        break
