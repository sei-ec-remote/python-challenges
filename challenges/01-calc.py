# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

def calc():
    calculation = input('What calculation would you like to do? (add, subtract, divide, multiply): ')
    first_number = int(input('What is the first number?: '))
    second_number = int(input('What is the second number?: '))

    if (calculation == 'add'):
        print(f'The sum of {first_number} and {second_number} is {first_number + second_number}')
    elif (calculation == 'subtract'):
        print(f'The difference of {first_number} and {second_number} is {first_number - second_number}')
    elif (calculation == 'divide'):
        print(f'The quotient of {first_number} and {second_number} is {first_number / second_number}')
    elif (calculation == 'multiply'):
        print(f'The product of {first_number} and {second_number} is {first_number * second_number}')

calc()