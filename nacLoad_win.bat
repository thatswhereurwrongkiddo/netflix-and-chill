@echo off

REM #nacLoad_win version 0.1
REM #Author: thatswhereurwrongkiddo
REM #
REM #The MIT License (MIT)
REM #
REM #Copyright (c) 2018-2019 thatswhereurwrongkiddo
REM #
REM #Permission is hereby granted, free of charge, to any person obtaining a
REM #copy of this software and associated documentation files (the "Software"),
REM #to deal in the Software without restriction, including without limitation
REM #the rights to use, copy, modify, merge, publish, distribute, sublicense,
REM #and/or sell copies of the Software, and to permit persons to whom the
REM #Software is furnished to do so, subject to the following conditions:
REM #
REM #The above copyright notice and this permission notice shall be included in
REM #all copies or substantial portions of the Software.
REM #
REM #THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
REM #OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
REM #FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
REM #LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
REM #AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
REM #DEALINGS IN THE SOFTWARE.
REM #FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER

echo ###########################################################
echo ###                                                     ###
echo ###   Welcome to the Netflix and Chill Windows Loader!   ###
echo ###                                                     ###
echo ###                   version 1.2.1                     ###
echo ###                                                     ###
echo ###########################################################
echo C: Start Neflix and Chill
echo Q: Exit

choice /C QC /n

if errorlevel 2 goto continue
if errorlevel 1 goto terminate
:terminate
exit
:continue
cd src && python splash.py
