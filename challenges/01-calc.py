# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

operator = ''

while (operator != 'add' and operator != 'sub' and operator != 'mult' and operator != 'div'):
    operator = input("What calculation would you like to do? (please enter: add, sub, mult, div) ").lower()
    if (operator != 'add' and operator != 'sub' and operator != 'mult' and operator != 'div'):
        print('Sorry, could not read your input...')

num1 = int(input("What's your first number? "))
num2 = int(input("What's your second number? "))

match operator:
    case 'add':
        print(f"{num1} plus {num2} is {num1 + num2}")
    case 'sub':
        print(f"{num1} minus {num2} is {num1 - num2}")
    case 'mult':
        print(f"{num1} times {num2} is {num1 * num2}")
    case 'div':
        print(f"{num1} divided by {num2} is {num1 / num2}")