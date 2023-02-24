# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

operation = input('What calculation would you like to do? (add, sub, mult, div)')

num_1 = int(input('What is the first number?'))


num_2 = int(input('What is the second number?'))


def calculate():
    if operation == 'add':
        return num_1 + num_2
    elif operation == 'sub':
        return num_1 - num_2
    elif operation == 'mult':
        return num_1 * num_2
    elif operation == 'div':
        return num_1 / num_2
    else:
        return 'invalid entry'

print('Your result is:', calculate())