# Developer:
#
# Date Started:
#
# Date Completed:
#
# File name: LeapYear.py
#
# Program Description: The following program is used to display all
# of the leap years in the range entered by the user

# Ask the user for a starting year and ending year in order to
# calculate the amount of leap years between the two years
#startingYear = #?
#endingYear = #?

# Use a for loop, if/elif statements, and print statements to
# determine and then display which years between the start and
# end years are leap years
#for
    # Follow the logic: if the year is divisible by 4 it is a leap year
    #if
        #print
    # Follow the logic: if the year is divisible by 4, 100, and 400 it is a leap year
    #elif
       # print

# Josh's Contribution:

starting_year = input('Choose a starting year: ')

while True:
    if starting_year.isnumeric():
        starting_year = int(starting_year)
        break
    else:
        starting_year = input('Choose a starting year: ')

ending_year = input('Choose an ending year: ')

while True:
    if ending_year.isnumeric():
        ending_year = int(ending_year)
        break
    else:
        ending_year = input('Choose an ending year: ')

for leap_year in range(starting_year, ending_year + 1):
    if leap_year % 4 == 0:
        print(leap_year)
    elif leap_year % 4 == 0 and leap_year % 100 == 0 and leap_year % 400 == 0:
        print(leap_year)
