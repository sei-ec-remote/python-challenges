# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

calculator = input('What calculation would you like to do? (add, subtract, multiply, divide) ')

first_value = input('What is the first number? ')

second_value = input('What is the second number? ')

if calculator == 'add':
    print(f'The sum is {int(first_value) + int(second_value)}')
elif calculator == 'subtract':
    print(f'The difference is {int(first_value) - int(second_value)}')
elif calculator == 'multiply':
    print(f'The product is {int(first_value) * int(second_value)}')
else:
    print(f'The quotient is {int(first_value) / int(second_value)}')