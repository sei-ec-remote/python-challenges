# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

calc = input('What type of problem would you like to do?')
num1 = int(input('first number :'))
num2 = int(input('second number :'))

def calculator ():
    if calc == 'add':
        print (num1 + num2)
    elif calc == 'sub':
        print (num1 - num2)
    elif calc == 'div':
        print (num1 / num2)
    elif calc == 'mult':
        print (num1 * num2)
calculator()