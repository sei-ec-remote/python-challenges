# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

operation = input("Which calculation would you like to do? (add, sub, mult, div):\n")
num1 = input("What is the first number?\n")
num1 = int(num1)
num2 = input("What is the second number?\n")
num2 = int(num2)

if operation == "add":
    print(f"The total is: {num1 + num2}")
elif operation == "sub":
    print(f"The total is: {num1 - num2}")
elif operation == "mult":
    print(f"The total is: {num1 * num2}")
elif operation == "div":
    print(f"The total is: {num1 / num2}")
else:
    print("Please enter a valid operator option.")
