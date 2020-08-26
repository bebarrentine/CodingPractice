def main():
    while True:
        try:
            x = int(input('What would you like the first number of the Fibonacci sequence to be?: '))
            y = int(input('What would you like the second number of the Fibonacci sequence to be?: '))
            z = int(input('How long would you like the Fibonacci sequence to be?: '))
            break
        except:
            print(' ')
            print('Try again.')
            print(' ')

    fiblist = [str(x), str(y)]
    for i in range(0, z):
        fib = x + y
        x,y = y, fib
        fiblist.append(str(fib))

    fibstring = ' '.join(fiblist)
    print(fibstring)

if __name__ == '__main__':
    main()