# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

operation = input('What calculation would you like to do? (add, sub, mult, div) \n')
num1 = float(input('What is number 1? \n'))
num2 = float(input('What is number 2? \n'))

if operation == 'add':
    print('Your result is', add(num1, num2))
elif operation == 'sub':
    print('Your result is', sub(num1, num2))
elif operation == 'mult':
    print('Your result is', mult(num1, num2))
else:
    print('Your result is', div(num1, num2)) 