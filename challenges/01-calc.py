# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.


def calc ():
    calculator = input("What calculation would you like to do? (add, subtract, multiply, divide): ")
    num1 = int(input("What is number 1: "))
    num2 = int(input("What is number 2: "))

    if (calculator == 'add'):
            print(f'The sum is {num1 + num2}')
    elif (calculator == 'subtract'):
            print(f'The difference is {num1 - num2}')
    elif (calculator == 'divide'):
            print(f'The quotient is {num1 / num2}')
    elif (calculator == 'multiply'):
            print(f'The product is {num1 * num2}')

calc() 