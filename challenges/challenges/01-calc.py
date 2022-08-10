# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

opp = input('Which oepration? ')

num1 = int(input('what is the first number? '))


num2 = int(input('what is the second number? '))


if opp == 'add' or opp == "+":
    print(num1 + num2)

elif opp == 'subtract' or opp == "-":
    print(num1 - num2)

elif opp == 'multiply' or opp == "*":
    print(num1 * num2)

elif opp == 'divide' or opp == '/':
    print(num1 / num2)

else:
    print("um what?")