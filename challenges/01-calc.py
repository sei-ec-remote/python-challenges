# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

# What calculation would you like to do? (add, sub, mult, div)
# add
# What is number 1?
# 3
# What is number 2?
# 6
# Your result is 9

operator = input('What calculation would you like to do? (add, sub, mult, div) ')
num1 = int(input('What is number 1? '))
num2 = int(input('What is number2? '))

if operator == 'add':
    result = num1 + num2
elif operator == 'sub':
    result = num1 - num2
elif operator == 'mult':
    result = num1 * num2
elif operator == 'div':
    result = num1 / num2
else:
    result = 'something went wrong'

print(f'Your result is, {result}')