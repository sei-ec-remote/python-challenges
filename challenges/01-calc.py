# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

operation = input('What calculation would you like to do? (add, sub, mult, div)')
num1 = input('what is number 1?')
num2 = input('what is number 2?')
if operation == 'add':
    print(f'{num1} + {num2} = {int(num1)+int(num2)}')
elif operation == 'sub':
    print(f'{num1} - {num2} = {int(num1)-int(num2)}')
elif operation == 'mult':
    print(f'{num1} * {num2} = {int(num1)*int(num2)}')
elif operation == 'div':
    print(f'{num1} / {num2} = {int(num1)/int(num2)}')
else:
    print('ERROR')