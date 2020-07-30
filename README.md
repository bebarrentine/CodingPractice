# Coding Practice
A repository of programming exercises. Yay!

## Exercise One: Leap Year

In this exercise, you will need to use user inputs, a single for loop, and if/elif statements to make a program that can display which years a leap years within a given range. For example, if the user inputs the starting year 2000 and the ending year 2016 then it would print "2000 2004 2008 2012 2016".

Example Output:

<img src="https://github.com/bebarrentine/CodingPractice/blob/master/ProgrammingSC/LeapYear.JPG" width="400" height="300" />


Keep in mind, it's best to be able to prevent errors before they happen; therefore, have it set to where the program will only accept an integer for the user inputs. 

**As a bonus:** If the user enters a letter, have the program prompt the user again until they enter an integer. This can be done in several different ways so get creative.

### Solution Code

Here is just one way to accomplish this exercise

```
while True:

  try:
  #This asks the user for a starting year and ending year in order to 
  #calculate the amount of leap years between the two years
    startingYear = int(input("Enter the starting year: "))
    endingYear = int(input("Enter the ending year: "))
    print("\n")
  except ValueError:
    print("Sorry, that is not a valid year. Please try again\n")
    continue
  else:
    break

  #The following 'for' loop is what's used to determine and then display which
  #years between the start and end years are leap years
for leapYear in range (startingYear, endingYear + 1):
  #Follows the logic: if the year is divisible by 4 it is a leap year
  if leapYear % 4 == 0 and leapYear % 100 != 0:
    print(leapYear)
  #Follows the logic: if the year is divisible by 4, 100, and 400 it is a leap year
  elif leapYear % 4 == 0 and leapYear % 100 == 0 and leapYear % 400 == 0:
    print(leapYear)
```


## Exercise Two: Drawing Diamonds

This exercise uses user input, for loops, if statements, and print statements to create the five stages of code to develop a complete diamond using asterisks and spaces. Keep in mind the user input must be an odd number.

Example Output:

<img src="https://github.com/bebarrentine/CodingPractice/blob/master/ProgrammingSC/DrawingDiamonds.JPG" width="300" height="400" />


**As a bonus:** Create an error statement to be printed if the user inputs an even number or invalid character. Have it set to prompt the user again for an answer or have the option to exit the code.

### Solution Code

Here is just one way to accomplish this exercise

```
#prompts the user for a number to represent the variable diamondHeight
print("---------Stage 1---------")
diamondHeight = int(input("Enter the height of the diamond:"))

#This while loop prevents the user from inputting a number an even and/or negative number by displaying an error code and prompting them for a new number
while diamondHeight % 2 == 0 or diamondHeight <= 0:
  print("ERROR: The height must be an odd number greater than 0")
  diamondHeight = int(input("Please re-enter:"))  

#prints the statement when the height is a validated number
print("The validated height of the diamond is",diamondHeight,"\n")

print("---------Stage 2---------")
print('')
a = 1
for a in range(diamondHeight + 1):
  top = (diamondHeight - a)
  print ("* "*(a) + " "*top)
print('')

print("---------Stage 3---------")
print('')
a = 1
for a in range(diamondHeight + 1):
  if a%2 != 0:
    top = (diamondHeight - a)//2
    print ("* "*((a // 2) + 1))# + " "*top)
print('')


print("---------Stage 4---------")
print('')
a = 1
for a in range(diamondHeight + 1):
    if a%2 != 0:
        top = (diamondHeight - a) // 2
        print (" "*(top*2) + "* "*(a) + " "*(a-1) +" "*top)
print('')

print("---------Stage 5---------")
print('')
a = 1 #a placeholder variable used to solve the top half of the diamond
b = 1 #a placeholder variable used to solve the bottom half of the diamond

#This for loop produces the top half of the diamond by alternating astracts and spaces
for a in range(diamondHeight + 1):
    if a%2 != 0:
        top = (diamondHeight - a) // 2
        print (" "*top*2 + "* "*(a) + " "*top)

#This for loop produces the bottom half of the diamond by alternating astracts and spaces
for b in range(diamondHeight - 1,0,-1):
    if b%2 != 0:
        bot = (diamondHeight-b)//2
        print (" "*bot*2 + "* "*(b) + " "*bot)
```


## Exercise Three: Currency Calculator

This exercise uses user input, if statements, functions, the split() method, and print statements to take an input of a cash value and then convert and print it into however many bills and coins are needed to equal the entered amount

Example Output:

<img src="https://github.com/bebarrentine/CodingPractice/blob/master/ProgrammingSC/CurrencyCalculator.JPG" width="400" height="400" />


**As a bonus:** Use while true to continue to run the program until a valid input is given. Try using try, except, and else

### Solution Code

Here is just one way to accomplish this exercise

```
Solution: To be posted
```


## Exercise Four: Most Popular Baby Name

This exercise uses user input, for loops, if statements, basic file methods, the split() method and print statements to open and search the user's specified file (names_1990s.txt, etc.) to display the inputted name's popularity rank. The program will ask the user for the name of the file and then open that file. It will also prompt the user for a full name and gender of the baby name. The program will then search the file for the first name in the appropriate column (one column for boys another for girls).  If the name is found, the rank for that name will be printed to the screen. 

Example Output:

<img src="https://github.com/bebarrentine/CodingPractice/blob/master/ProgrammingSC/MPBabyName.JPG" width="400" height="300" />


**As a bonus:** Create an error statement to be printed if the user inputs a nonexistent file name. For an extra challenge, try to have a statement only print when the name is not found in the list unlike the constant statement as seen in the image.

### Solution Code

Here is just one way to accomplish this exercise

```
Solution: To be posted
```


## Exercise Five: Password Generator

Generate a password using strings and the join() method (hint: I recommend using either sample() or choice() methods depending how you want to go about it). The passwords should be random, generating a new password every time the user asks for a new password. Include your code in a main method. Be sure to type 'import random' at the top of your code

Example Output:

<img src="https://github.com/bebarrentine/CodingPractice/blob/master/ProgrammingSC/PasswordGenerator.JPG" width="200" height="100" />


**As a bonus:** Instead of using a specified password length hard coded in, ask the user for the desired length. Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

### Solution Code

Here is just one way to accomplish this exercise

```
Solution: To be posted
```

## Coming Soon: Text-Based Adventure and Hangman

## Python/IDE Resources
I'll add to this as time goes on

* [Using Github in Pycharm](https://www.simplifiedpython.net/how-to-add-code-to-github/) - An article that gives instructions for using Github within Pycharm
* [Stackoverflow](https://stackoverflow.com/) - For all your questions and copy & paste needs
* [Python Docs](https://docs.python.org/3/tutorial/) - The official python documentation, it's a beautiful thing
