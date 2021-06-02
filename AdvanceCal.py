#python 3.8.8
#contract: zigm1315@gmail.com
import time
def calculate():

    number_1 = float(input('Please enter the first number: '))
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
** for power
% for modulo
''')
    number_2 = float(input('Please enter the second number: '))
    start = time.time()
    
    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)
        print("time:", (time.time()-start)*1000)
        loop()

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)
        print("time:", (time.time()-start)*1000)
        loop()

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)
        print("time:", (time.time()-start)*1000)
        loop()

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)
        print("time:", (time.time()-start)*1000)
        loop()

    elif operation == '**':
        print('{} ** {} = '.format(number_1, number_2))
        print(number_1**number_2)
        print("time:", (time.time()-start)*1000)
        loop()

    elif operation == '%':
        print('{} % {} = '.format(number_1, number_2))
        print(number_1 % number_2)
        print("time:", (time.time()-start)*1000)
        loop()

    else:
        print('You have not typed a valid operator, please run the program again.')

def loop():
    yn = str(input("do you want to calculate again?(y/n) : "))
    if yn == 'y':
        calculate()
    else:
        print("Good Bye~>:3")
calculate()