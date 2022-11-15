# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

# What calculation would you like to do? (add, sub, mult, div)
# add
# What is number 1?
# 3
# What is number 2?
# 6
# Your result is 9

while True:
    operation = input("What calculation would you like to do? (add, sub, mult, div): ")
    if operation.lower() not in ('add', 'sub', 'mult', 'div'):
        print("Not an operation")
    else:
        break

num1 = float(input("What is number 1? : "))
num2 = float(input("What is number 2? : "))

if operation == 'add':
    solution = num1 + num2
elif operation == 'sub':
    solution = num1 - num2
elif operation == 'mult':
    solution = num1 * num2
elif operation == 'div':
    solution = num1 / num2

print('Your result is', solution)