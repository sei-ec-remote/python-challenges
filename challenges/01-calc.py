# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

print('Hello! This is a calculator, so use it! ')
calc = input('What calculation would you like to do? (add, sub, mult, div) ')
if(calc == 'add'):
    num1 = input('What is number 1? ')
    num1 = int(num1)
    print(num1, '+ __?')
    num2 =input('What is number 2? ')
    num2 = int(num2)
    sol = num1 + num2
    print(num1, '+', num2, '=', sol)
elif(calc == 'sub'):
    num1 = input('What is number 1? ')
    num1 = int(num1)
    print(num1, '- __?')
    num2 =input('What is number 2? ')
    num2 = int(num2)
    sol = num1 - num2
    print(num1, '-', num2, '=', sol)
elif(calc == 'mult'):
    num1 = input('What is number 1? ')
    num1 = int(num1)
    print(num1, '* __?')
    num2 =input('What is number 2? ')
    num2 = int(num2)
    sol = num1 * num2
    print(num1, '*', num2, '=', sol)
elif(calc == 'div'):
    num1 = input('What is number 1? ')
    num1 = int(num1)
    print(num1, '/ __?')
    num2 =input('What is number 2? ')
    num2 = int(num2)
    sol = num1 / num2
    print(num1, '/', num2, '=', sol)
