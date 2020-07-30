# Name:
# Josh Herndon
# Date Started:
# 07/28/2020
# Date Completed:
#
# File name: CurrencyCalculator.py
#
# Program Description: The following program takes an input of a cash value and
# then converts and prints it into however many bills and coins are needed to
# equal this amount

# no hints this time, you can ask if you need them ;)

price = 1.1111

while True:
    if price == round(price, 2):
        price = float(price)
        break
    else:
        print(' ')
        print('Prices only have two decimal places.')
        print(' ')
        try:
            price = float(input('Enter a price: '))
        except:
            print(' ')
            print('That is not a valid price! Try again.')

def currency_calc(price):
    y = price*100
    for x in range(0, 100):
        if y - x in range(100, int(price*1000), 100):
            cents = x
            bills = int(price - cents/100)


    print(' ')
    b = ['', '', '', '', '', '', '']
    w = bills/100

    print('The paper bills you will need are: ')

    if w < 0.1:
        b[1] = '0 Hundreds'
        b[2] = '0 Fifties'
        b[3] = '0 Twenties'
        b[4] = '0 Tens'
        for c in b:
            if bills < 5:
                b[5] = '0 Fivs'
                b[6] = str(bills) + ' ' + 'Ones'
            elif bills >= 5:
                b[5] = '1 Five'
                b[6] = str(bills % 5) + ' ' + 'Ones'
            print(c)

    if 0.1 <= w < 1:
        b[1] = '0 Hundreds'
        for c in b:
            if bills % 50 == 0:
                b[2] = '1 Fifty'
                b[3] = '0 Twenties'
                b[4] = '0 Tens'
                b[5] = '0 Fives'
                b[6] = '0 Ones'
            elif bills in range(50, 60) and (bills % 10)/5 < 1:
                b[2] = '1 Fifty'
                b[3] = '0 Twenties'
                b[4] = '0 Tens'
                b[5] = '0 Fives'
                b[6] = str(bills % 5) + ' ' + 'Ones'
            elif bills in range(50, 60) and (bills % 10)/5 >= 1:
                b[2] = '1 Fifty'
                b[3] = '0 Twenties'
                b[4] = '0 Tens'
                b[5] = '1 Five'
                b[6] = str(bills % 5) + ' ' + 'Ones'
            elif bills % 20 == 0 and bills not in range(50, 60):
                b[2] = '0 Fifties'
                b[3] = str(int(bills/20)) + ' ' + 'Twenties'
                b[4] = '0 Tens'
                b[5] = '0 Fives'
                b[6] = '0 Ones'
            elif bills % 20 == 10 and bills not in range(50, 60):
                b[2] = '0 Fifties'
                b[3] = str(int((bills / 20) - 0.5)) + ' ' + 'Twenties'
                b[4] = '1 Ten'
                b[5] = '0 Fives'
                b[6] = '0 Ones'
            elif bills % 20 == 5 and bills % 5 == 0 and bills not in range(50,60):
                b[2] = '0 Fifties'
                b[3] = str(int(bills / 20)) + ' ' + 'Twenties'
                b[4] = '0 Tens'
                b[5] = '1 Five'
                b[6] = '0 Ones'
            elif bills % 20 == 15 and bills % 5 == 0 and bills > 10 and bills not in range(50, 60):
                b[2] = '0 Fifties'
                b[3] = str(int((bills / 20) - 0.5)) + ' ' + 'Twenties'
                b[4] = '1 Ten'
                b[5] = '1 Five'
                b[6] = '0 Ones'
            elif bills % 10 != 0 and bills % 5 != 0 and bills >= 20 and bills % 20 >= 10 and (bills % 10)/5 >= 1 and bills not in range(50, 60):
                b[2] = '0 Fifties'
                b[3] = str(int((bills - bills % 20)/20)) + ' ' + 'Twenties'
                b[4] = '1 Ten'
                b[5] = '1 Five'
                b[6] = str(bills % 5) + ' ' + 'Ones'
            elif bills % 10 != 0 and bills % 5 != 0 and bills >= 20 and bills % 20 >= 10 and (bills % 10)/5 < 1 and bills not in range(50, 60):
                b[2] = '0 Fifties'
                b[3] = str(int((bills - bills % 20)/20)) + ' ' + 'Twenties'
                b[4] = '1 Ten'
                b[5] = '0 Fives'
                b[6] = str(bills % 5) + ' ' + 'Ones'
            elif bills % 10 != 0 and bills % 5 != 0 and bills >= 20 and bills % 20 < 10 and (bills % 10)/5 < 1 and bills not in range(50, 60):
                b[2] = '0 Fifties'
                b[3] = str(int((bills - bills % 20)/20)) + ' ' + 'Twenties'
                b[4] = '0 Tens'
                b[5] = '0 Fives'
                b[6] = str(bills % 5) + ' ' + 'Ones'
            elif bills % 10 != 0 and bills % 5 != 0 and bills >= 20 and bills % 20 < 10 and (bills % 10)/5 >= 1 and bills not in range(50, 60):
                b[2] = '0 Fifties'
                b[3] = str(int((bills - bills % 20)/20)) + ' ' + 'Twenties'
                b[4] = '0 Tens'
                b[5] = '1 Five'
                b[6] = str(bills % 5) + ' ' + 'Ones'
            elif bills % 10 != 0 and bills % 5 != 0 and 20 > bills >= 10 and (bills % 10)/5 < 1 and bills not in range (50, 60):
                b[2] = '0 Fifties'
                b[3] = '0 Twenties'
                b[4] = '1 Ten'
                b[5] = '0 Fives'
                b[6] = str(bills % 5) + ' ' + 'Ones'
            elif bills % 10 != 0 and bills % 5 != 0 and 20 > bills >= 10 and (bills % 10)/5 >= 1 and bills not in range (50, 60):
                b[2] = '0 Fifties'
                b[3] = '0 Twenties'
                b[4] = '1 Ten'
                b[5] = '1 Five'
                b[6] = str(bills % 5) + ' ' + 'Ones'
            print(c)

    if 1 <= w:
        for c in b:
            if bills % 100 == 0:
                b[1] = str(int((bills - bills % 100) / 100)) + ' ' + 'Hundreds'
                b[2] = '0 Fifties'
                b[3] = '0 Twenties'
                b[4] = '0 Tens'
                b[5] = '0 Fives'
                b[6] = '0 Ones'
            elif bills % 50 == 0 and bills % 100 != 0:
                b[1] = str(int((bills - bills % 100) / 100)) + ' ' + 'Hundreds'
                b[2] = '1 Fifty'
                b[3] = '0 Twenties'
                b[4] = '0 Tens'
                b[5] = '0 Fives'
                b[6] = '0 Ones'
            elif bills % 50 in range(0, 10) and (bills % 10)/5 < 1 and bills % 100 != 0:
                b[1] = str(int((bills - bills % 100) / 100)) + ' ' + 'Hundreds'
                b[2] = '1 Fifty'
                b[3] = '0 Twenties'
                b[4] = '0 Tens'
                b[5] = '0 Fives'
                b[6] = str(bills % 5) + ' ' + 'Ones'
            elif bills % 50 in range(0, 10) and (bills % 10)/5 >= 1 and bills % 100 != 0:
                b[1] = str(int((bills - bills % 100) / 100)) + ' ' + 'Hundreds'
                b[2] = '1 Fifty'
                b[3] = '0 Twenties'
                b[4] = '0 Tens'
                b[5] = '1 Five'
                b[6] = str(bills % 5) + ' ' + 'Ones'
            elif bills % 20 == 0 and bills % 50 not in range(0, 10):
                b[1] = str(int((bills - bills % 100) / 100)) + ' ' + 'Hundreds'
                b[2] = '0 Fifties'
                b[3] = str(int(bills/20) - 5*int((bills - bills % 100) / 100)) + ' ' + 'Twenties'
                b[4] = '0 Tens'
                b[5] = '0 Fives'
                b[6] = '0 Ones'
            elif bills % 20 == 10 and bills % 50 not in range(0, 10):
                b[1] = str(int((bills - bills % 100) / 100)) + ' ' + 'Hundreds'
                b[2] = '0 Fifties'
                b[3] = str(int((bills / 20) - 0.5 - 5*int((bills - bills % 100) / 100))) + ' ' + 'Twenties'
                b[4] = '1 Ten'
                b[5] = '0 Fives'
                b[6] = '0 Ones'
            elif bills % 20 == 5 and bills % 5 == 0 and bills % 50 not in range(0, 10):
                b[1] = str(int((bills - bills % 100) / 100)) + ' ' + 'Hundreds'
                b[2] = '0 Fifties'
                b[3] = str(int(bills / 20) - 5*int((bills - bills % 100) / 100)) + ' ' + 'Twenties'
                b[4] = '0 Tens'
                b[5] = '1 Five'
                b[6] = '0 Ones'
            elif bills % 20 == 15 and bills % 5 == 0 and bills > 10 and bills % 50 not in range(0, 10):
                b[1] = str(int((bills - bills % 100) / 100)) + ' ' + 'Hundreds'
                b[2] = '0 Fifties'
                b[3] = str(int((bills / 20) - 0.5 - 5*int((bills - bills % 100) / 100))) + ' ' + 'Twenties'
                b[4] = '1 Ten'
                b[5] = '1 Five'
                b[6] = '0 Ones'
            elif bills % 10 != 0 and bills % 5 != 0 and bills >= 20 and bills % 20 >= 10 and (bills % 10)/5 >= 1 and bills % 50 not in range(0, 10):
                b[1] = str(int((bills - bills % 100) / 100)) + ' ' + 'Hundreds'
                b[2] = '0 Fifties'
                b[3] = str(int(((bills - bills % 20)/20) - 5*int((bills - bills % 100) / 100))) + ' ' + 'Twenties'
                b[4] = '1 Ten'
                b[5] = '1 Five'
                b[6] = str(bills % 5) + ' ' + 'Ones'
            elif bills % 10 != 0 and bills % 5 != 0 and bills >= 20 and bills % 20 >= 10 and (bills % 10)/5 < 1 and bills % 50 not in range(0, 10):
                b[1] = str(int((bills - bills % 100) / 100)) + ' ' + 'Hundreds'
                b[2] = '0 Fifties'
                b[3] = str(int(((bills - bills % 20)/20) - 5*int((bills - bills % 100) / 100))) + ' ' + 'Twenties'
                b[4] = '1 Ten'
                b[5] = '0 Fives'
                b[6] = str(bills % 5) + ' ' + 'Ones'
            elif bills % 10 != 0 and bills % 5 != 0 and bills >= 20 and bills % 20 < 10 and (bills % 10)/5 < 1 and bills % 50 not in range(0, 10):
                b[1] = str(int((bills - bills % 100) / 100)) + ' ' + 'Hundreds'
                b[2] = '0 Fifties'
                b[3] = str(int(((bills - bills % 20)/20) - 5*int((bills - bills % 100) / 100))) + ' ' + 'Twenties'
                b[4] = '0 Tens'
                b[5] = '0 Fives'
                b[6] = str(bills % 5) + ' ' + 'Ones'
            elif bills % 10 != 0 and bills % 5 != 0 and bills >= 20 and bills % 20 < 10 and (bills % 10)/5 >= 1 and bills % 50 not in range(0, 10):
                b[1] = str(int((bills - bills % 100) / 100)) + ' ' + 'Hundreds'
                b[2] = '0 Fifties'
                b[3] = str(int(((bills - bills % 20)/20) - 5*int((bills - bills % 100) / 100))) + ' ' + 'Twenties'
                b[4] = '0 Tens'
                b[5] = '1 Five'
                b[6] = str(bills % 5) + ' ' + 'Ones'
            elif bills % 10 != 0 and bills % 5 != 0 and 20 > bills >= 10 and (bills % 10)/5 < 1 and bills % 50 not in range (0, 10):
                b[1] = str(int((bills - bills % 100) / 100)) + ' ' + 'Hundreds'
                b[2] = '0 Fifties'
                b[3] = '0 Twenties'
                b[4] = '1 Ten'
                b[5] = '0 Fives'
                b[6] = str(bills % 5) + ' ' + 'Ones'
            elif bills % 10 != 0 and bills % 5 != 0 and 20 > bills >= 10 and (bills % 10)/5 >= 1 and bills % 50 not in range (0, 10):
                b[1] = str(int((bills - bills % 100) / 100)) + ' ' + 'Hundreds'
                b[2] = '0 Fifties'
                b[3] = '0 Twenties'
                b[4] = '1 Ten'
                b[5] = '1 Five'
                b[6] = str(bills % 5) + ' ' + 'Ones'
            print(c)

    print(' ')
    print('The coins you will need are: ')
    k = len(str(cents))

    j = ['', '', '', '', '']

    if k == 1:
        for i in j:
            j[1] = '0 Quarters'
            j[2] = '0 Dimes'
            if cents < 5:
                j[3] = '0 Nickels'
                j[4] = str(cents) + ' ' + 'Pennies'
            elif cents >= 5:
                j[3] = '1 Nickel'
                j[4] = str(cents % 5) + ' ' + 'Pennies'
            print(i)

    if k == 2:
        for i in j:
            if cents % 25 == 0:
                j[1] = str(int(cents/25)) + ' ' + 'Quarters'
                j[2] = '0 Dimes'
                j[3] = '0 Nickels'
                j[4] = '0 Pennies'
            elif (cents % 25) != 5:
                j[1] = str(int((cents - cents % 25)/25)) + ' ' + 'Quarters'
                j[2] = str(int(((cents % 25) - ((cents % 25) % 10))/10)) + ' ' + 'Dimes'
                j[3] = str(int((cents % 25) % 5)) + ' ' + 'Nickels'
                j[4] = str(int(cents % 5)) + ' ' + 'Pennies'
            elif (cents % 25) == 5:
                j[1] = str(int((cents - cents % 25)/25)) + ' ' + 'Quarters'
                j[2] = str(int(((cents % 25) - ((cents % 25) % 10))/10)) + ' ' + 'Dimes'
                j[3] = '1 Nickel'
                j[4] = str(int(cents % 5)) + ' ' + 'Pennies'
            #elif cents >= 25 and cents >= 45:
                j[1] = str(int((cents - cents % 25)/25)) + ' ' + 'Quarters'
                j[2] = str(int(((cents % 25) - ((cents % 25) % 10))/10)) + ' ' + 'Dimes'
                j[3] = '0 Nickels'
                j[4] = str(int(cents % 5)) + ' ' + 'Pennies'
            #elif cents >= 25 and cents % 10 != 5:
                j[1] = str(int((cents - cents % 25)/25)) + ' ' + 'Quarters'
                j[2] = str(int(((cents % 25) - ((cents % 25) % 10))/10)) + ' ' + 'Dimes'
                j[3] = str(int((cents - cents % 25)/25)) + ' ' + 'Nickels'
                j[4] = str(int(cents % 5)) + ' ' + 'Pennies'
            #elif cents >= 25 and cents % 10 == 5:
                j[1] = str(int((cents - cents % 25)/25)) + ' ' + 'Quarters'
                j[2] = str(int(((cents % 25) - ((cents % 25) % 10))/10)) + ' ' + 'Dimes'
                j[3] = '0 Nickels'
                j[4] = str(int(cents % 5)) + ' ' + 'Pennies'
            print(i)



currency_calc(price)
