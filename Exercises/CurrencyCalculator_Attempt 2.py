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

price = str(price)
splitprice = price.split('.')

bills = int(splitprice[0])
cents = int(splitprice[1])


def currency_calc(bills, cents):
    numhundred = 0
    numfifty = 0
    numtwenty = 0
    numten = 0
    numfive = 0
    numones = 0

    numhundred = bills // 100
    bills = bills - numhundred * 100

    numfifty = bills // 50
    bills = bills - numfifty * 50

    numtwenty = bills // 20
    bills = bills - numtwenty * 20

    numten = bills // 10
    bills = bills - numten * 10

    numfive = bills // 5
    bills = bills - numfive * 5

    numones = bills // 1
    bills = bills - numones

    bill_list = [str(numhundred) + ' Hundreds', str(numfifty) + ' Fifty', str(numtwenty) + ' Twenties', str(numten) + ' Tens', str(numfive) + ' Fives', str(numones) + ' Ones']

    print(' ')
    print('The paper bills you will need are: ')
    print(' ')

    for a in bill_list:
        print(a)

    print(' ')

    numquarters = 0
    numdimes = 0
    numnickels = 0
    numpennies = 0


    numquarters = cents // 25
    cents = cents - numquarters * 25

    numdimes = cents // 10
    cents = cents - numdimes * 10

    numnickels = cents // 5
    cents = cents - numnickels * 5

    numpennies = cents // 1
    cents= cents - numpennies


    cents_list = [str(numquarters) + ' Quarters', str(numdimes) + ' Dimes', str(numnickels) + ' Nickels',
             str(numpennies) + ' Pennies']


    print('The coins you will need are: ')
    print(' ')

    for b in cents_list:
        print(b)

currency_calc(bills, cents)


