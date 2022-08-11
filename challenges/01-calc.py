# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

# Get what operation to do.
print("What would you like to use")
print('options: add sub times divide')
operation = input()

# get the two numbers
print('First number: ')
num1 = input()
print('Second number: ')
num2 = input()

# Do the operaton user asks for, and print it out.
if operation in 'add':
     print(int(num1) + int(num2))
elif operation in 'sub':
     print(int(num1) - int(num2))
elif operation in 'times':
     print(int(num1) * int(num2))
elif operation in 'divide':
     print(int(num1) / int(num2))

# Put a nice goodby message.
print('Goodbye')