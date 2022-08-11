# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

calculator = input('What calculation would you like to do? (add, sub, mult, div) ')

first_num = input('What is the first number? ')

second_num = input('What is the second number? ')

if calculator == 'add' or calculator =='ADD':
    print(f'The sum is {int(first_num) + int(second_num)}')
if calculator == 'sub' or calculator == 'SUB':
    print(f'The difference is {int(first_num) - int(second_num)}') 
if calculator == 'mult' or calculator == 'MULT':
    print(f'The product is {int(first_num) * int(second_num)}')
if calculator == 'div' or calculator ==  'DIV':
    print(f'The quotient is {int(first_num) / int(second_num)}')