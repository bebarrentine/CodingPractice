# Name:
# Josh Herndon
# Date Started:
#07/30/2020
# Date Completed:
#
# File name: PasswordGenerator.py
#
# Program Description: The following program generates a randomized password upon being run
#join()
#sample()
#choice()
# Hint: don't over think it, this can be done in 4 lines (excluding import random)

import random
import string

while True:
    try:
        x = int(input('How long would you like your password to be?: '))
        break
    except:
        print(' ')
        print('That is not a valid password length. Try again.')
        print(' ')

print(''.join(random.sample(string.printable, x)))






