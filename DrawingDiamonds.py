# Developer:
# J. Herndon
# Date Started:
#07/26/2020
# Date Completed:
#
# File name: DrawingDiamonds.py
#
# Program Description: The following code will draw a diamond-shaped picture by taking the user's input.
# This input determines the number of lines to be drawn.

# prompts the user for a number to represent the variable diamondHeight
print("---------Stage 1---------")
print('')

diamondheight = ''

while True:
    if diamondheight.isnumeric() == True and int(diamondheight) % 2 != 0:
        diamondheight = int(diamondheight)
        break
    else:
        diamondheight = input('Please enter the height of the diamond: ')




#prints the statement when the height is a validated number
print('The height of the diamond is {}'.format(diamondheight))

print('')

print("---------Stage 2---------")
print('')

#a = 1 #a place holder variable used to calculate the height of the triangle
for a in range(1, diamondheight + 1):
    top = a * '* '
    print(top)

print('')

print("---------Stage 3---------")
print('')

#a = 1 #a place holder variable used to calculate the combined length of the triangles two sides (1/4 of a diamond)
for a in range(1, diamondheight - 1):
    top = a * '* '
    print(top)

print('')

print("---------Stage 4---------")
print('')

#a = 1 #a place holder variable used to calculate the top of the diamond
n = -1
m = 1
l = diamondheight + 1
for a in reversed(range(1, diamondheight - 1)):
    n += 2
    m += 1
    l -= 2
    if a == (diamondheight - m) and m <= diamondheight - 1 and n <= diamondheight and l >= 0:
        top = (l * ' ') + (n * '* ')
        print(top)


print('')

print("---------Stage 5---------")
print('')

#a = 1  # a placeholder variable used to solve the top half of the diamond
#b = 1  # a placeholder variable used to solve the bottom half of the diamond

# This for loop produces the top half of the diamond by alternating asterisks and spaces
n = -1
m = 1
l = diamondheight + 1
for a in reversed(range(1, diamondheight - 1)):
    n += 2
    m += 1
    l -= 2
    if a == (diamondheight - m) and m <= diamondheight - 1 and n <= diamondheight and l >= 0:
        top = (l * ' ') + (n * '* ')
        print(top)


# This for loop produces the bottom half of the diamond by alternating asterisks and spaces
i = diamondheight
j = 2
k = 0
for b in reversed(range(1, diamondheight - 2)):
    i -= 2
    j += 1
    k += 2
    if b == (diamondheight - j) and j <= diamondheight - 1 and i >= 0 and k <= diamondheight - 1:
        bot = (k * ' ') + (i * '* ')
        print(bot)

