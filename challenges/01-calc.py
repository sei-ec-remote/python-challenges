# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

calc = input('What operation would you like to do (add, sub, mult, div)?\n')
num1 = input('What is the first number?\n')
num2 = input('What is the second number?\n')

if "." in num1:
    num1 = float(num1)
else:
    num1 = int(num1)

if "." in num2:
    num2 = float(num2)
else:
    num2 = int(num2)

if calc == "add":
    print(num1 + num2)
elif calc == "sub":
    print(num1 - num2)
elif calc == "mult":
    print(num1 * num2)
else:
    print(num1 / num2)