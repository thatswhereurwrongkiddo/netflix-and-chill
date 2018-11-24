"""
Welcome to the source code for 'Netflix and Chill' v1.0.1b2
This is a program that pulls movie information from a basic 20 movie SEQueL database
and offers multiple selection options such as Genre, Release Year, and IMDb rating.

Written by: u/thatswhereurwrongkiddo on github

Last Updated: 11.24.2018
"""

import sqlite3
import os
import time
import sys
from playsound import playsound

connection = sqlite3.connect("movie_db.db")

cursor = connection.cursor()

print("""Welcome to Netflix and Chill v1.0.1b2

Designed with love by github user thatswhereurwrongkiddo
""")
print("""How would you like to select your movie?

Options are:

Genre (1)
Release Year (2)
IMDb Rating (3)

""")
db_selection = raw_input('And you pick...? (Enter Selection Number): ')

os.system('cls')


if db_selection == ('1'):

    print("Which genre would you like to watch?")
    print("""
Genre List:

Action (1)
Thriller (2)
Drama (3)
Fantasy (4)
Comedy (5)
""")
    num_genre = raw_input("Type Selection (Enter Selection Number):")
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

    print('Results for the following SQL Command ({0}):'.format(sql_command))
    print ('')

    result = cursor.fetchall()
    for r in result:
        print(r)

    time.sleep(1)
    print('')
    raw_input('Press ENTER to exit application')

elif db_selection == ('2'):

    print("""How would you like to select your movie?

    By specific release year? (1)
    By release date before specific year (i.e. Movies released after 2010) (2)
    By release date after specific year (i.e. Movies released before 2010) (3)

    """)

    year_option = raw_input('Type the number of your selelction: ')

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

        num_year = raw_input('Type Selection: ')

        sql_command = ('SELECT movie, rel_year FROM movies WHERE rel_year = "{0}"'.format(num_year))
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
        raw_input('Press ENTER to exit application')

    elif year_option == ('2'):

        num_year = raw_input('I would like to see a movie released before _____: ')
        sql_command = ('SELECT movie, rel_year FROM movies WHERE rel_year <= "{0}"'.format(num_year))
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
        raw_input('Press ENTER to exit application')

    elif year_option == ('3'):

        num_year = raw_input('I would like to see a movie released after _____: ')
        sql_command = ('SELECT movie, rel_year FROM movies WHERE rel_year >= "{0}"'.format(num_year))
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
        raw_input('Press ENTER to exit application')

elif db_selection == ('3'):

    print("""How would you like to select your movie?

Options:

IMDb rating greater than ___ (1)
IMDb rating less than ___(2)
""")

    imdb_selection = raw_input('Type selection number: ')

    os.system('cls')

    if imdb_selection == ('1'):

        num_year = raw_input('I would like to see a movie with an IMDb rating greater than _____: ')
        sql_command = ('SELECT movie, rating FROM movies WHERE rating >= "{0}"'.format(num_year))
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
        raw_input('Press ENTER to exit application')

    if imdb_selection == ('2'):

        num_year = raw_input('I would like to see a movie with an IMDb rating less than _____: ')
        sql_command = ('SELECT movie, rating FROM movies WHERE rating <= "{0}"'.format(num_year))
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
        raw_input('Press ENTER to exit application')

else:

    print('System Failure')
    time.sleep(0.5)
    print('Damn it, Desmond')
    time.sleep(0.5)
    print('')
    playsound('sys_fail.wav')
    raw_input('Press ENTER to exit application')
