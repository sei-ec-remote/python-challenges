# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

addition = 'add'
subtraction = 'sub'
multiplication = 'mult'
division = 'div'

operation = input('What calculation would you like to do? (add, sub, mult, div): ').lower()

if (operation in addition):
    num1 = input('What is number 1?: ')
    num2 = input('What is number 2?: ')
    print('Your result is ', int(num1) + int(num2))
elif (operation in subtraction):
    num1 = input('What is number 1?: ')
    num2 = input('What is number 2?: ')
    print('Your result is ', int(num1) - int(num2))
elif (operation in multiplication):
    num1 = input('What is number 1?: ')
    num2 = input('What is number 2?: ')
    print('Your result is ', int(num1) * int(num2))
elif (operation in division):
    num1 = input('What is number 1?: ')
    num2 = input('What is number 2?: ')
    print('Your result is ', int(num1) // int(num2))
