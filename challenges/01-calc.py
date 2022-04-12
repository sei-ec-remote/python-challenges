# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.


operator = input('pick an operator (add, sub, mult, div)')
num1 = int(input('enter number 1'))
num2 = int(input('enter number 2'))


if operator == 'add':
    answer = num1 + num2
elif operator == 'sub':
    answer = num1 - num2
elif operator == 'mult':
     answer = num1 * num2
elif operator == 'div':
    answer =  num1 / num2

print(f'Your result is {answer}') 