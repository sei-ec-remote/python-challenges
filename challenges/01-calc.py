# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.




operator = input('What calculation would you like to do? (add, sub, mult, div)')
num1 = int(input('enter 1st number'))
num2 = int(input('enter 2nd number'))

if operator == 'add':
    print('total =', num1 + num2)

elif operator == 'sub':
    print('total =',num1 - num2)

elif operator == 'mult':
    print('total =', num1 * num2)

elif operator == 'div':
    print('total =', num1 / num2)
