# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

action = input('What calculation would you like to do? (+, -, *, /): ')
input1 = int(input('What is the first number? '))
input2 = int(input('What is the second number? '))
result = 0

if action == '+':
    result = input1 + input2

elif action == '-':
    result = input1 - input2

elif action == '/':
    result = input1 / input2
    
elif action == '*':
    result = input1 * input2

print(f'Huzzah! {result} is your answer.')