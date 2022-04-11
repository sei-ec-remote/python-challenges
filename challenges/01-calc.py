# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

calculation = input("What calculation would you like to do?")

functions = ["add", "subtract", "multiply", "divide"]

first_number = int(input("Enter your first number:"))
second_number = int(input("Enter your second number:"))

def calculator ():
    if functions[0] in calculation:
        print (first_number + second_number)
    elif functions[1] in calculation:
        print(first_number - second_number)
    elif functions[2] in calculation:
        print(first_number * second_number)
    else: 
        print(first_number / second_number)
calculator()