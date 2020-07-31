# Name:
# Josh Herndon
# Date Started:
# 07/30/2020
# Date Completed:
#
# File name: MPBabyName.py
#
# Program Description: This program will ask the user for the name of the file
# and then open that file.  It will also prompt the user for a full name and
# gender of the baby name. The program will then search the file for the first
# name in the appropriate column (one column for boys another for girls).  If
# the name is found, the rank for that name will be printed to the screen.

# no hints this time, you can ask if you need them ;)

#.read()
#.readlines()
#.readline()

file_name = 'z'
file_list = ['names_1950s.txt', 'names_1960s.txt', 'names_1970s.txt', 'names_1980s.txt', 'names_1990s.txt', 'names_2000s.txt', 'names_2010s.txt']
while file_name not in file_list:
        file_name = input('What is your file name?: ')
        if file_name not in file_list:
            print(' ')
            print('That is not a valid file name. Try again.')
            print(' ')

baby_name = input("Enter the baby's first and last name: ").capitalize()

gender = '5'
while gender not in ['m', 'f']:
        gender = input('Enter the gender of the baby (m/f): ')
        if gender not in ['m', 'f']:
            print(' ')
            print('That is not a valid gender. Try again.')
            print(' ')


with open(file_name, 'r') as f_decade:
    f_contents = f_decade.read()
    baby = baby_name.split()[0]
    print(' ')
    if baby in f_contents.split() and gender == 'm':
        print('{}{}{}{}s rank: {}'.format(file_name[6], file_name[7], file_name[8], file_name[9], f_contents.split()[f_contents.split().index(baby) - 1]))
    elif baby in f_contents.split() and gender == 'f':
        print('{}{}{}{}s rank: {}'.format(file_name[6], file_name[7], file_name[8], file_name[9], f_contents.split()[f_contents.split().index(baby) - 3]))
    elif baby not in f_contents.split():
        print('{} was not ranked in the {}{}{}{}s.'.format(baby_name, file_name[6], file_name[7], file_name[8], file_name[9]))

