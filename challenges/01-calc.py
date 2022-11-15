# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

operator = input('What calculation would you like to do? (add, sub, mult, div)')

first_num = input('What is number 1?')

second_num = input('What is number 2?')

if operator == 'add':
    print(f'Your result is {int(first_num) + int(second_num)}')
elif operator == 'sub':
    print(f'Your result is {int(first_num) - int(second_num)}')
elif operator == 'mult':
    print(f'Your result is {int(first_num) * int(second_num)}')
elif operator == 'div': 
    print(f'Your result is {int(first_num) / int(second_num)}')