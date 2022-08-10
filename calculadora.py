defcalculate():
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

    number_1 = int(input('Enter your first number: '))
    number_2 = int(input('Enter yout second number: '))

    if operation == '+':
        #Adicion
        print('{} + {} = {}' .format(number_1, number_2, (number_1 + number_2)))
    elif operation == '-':
        #Subtraction
        print('{} - {} = {}' .format(number_1, number_2, (number_1 - number_2)))
    elif operation == '*':
        #Multiplication
        print('{} * {} = {}' .format(number_1, number_2, (number_1 * number_2)))
    elif operation == '/':
        #Division
        print('{} / {} = {}' .format(number_1, number_2, (number_1 / number_2)))
    else: 
        print('You have not typed a valid operator,please run the program again.')
    
    #Add again() function to calculate() function again()
def again():
    calc_again = input('''
    Do you want to calculate again?
    Please type Y for YES or N for NO.    
    ''')
    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper == 'N':
        print('See you later.')
    else:
        again()
        
calculate()