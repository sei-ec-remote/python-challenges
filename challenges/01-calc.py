# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

def calculator():
    prompt = input("What calculation would you like to do (add, sub, mul, div)? ")
    num1 = int(input("First number:"))
    num2 = int(input("Second number:"))
    result = 0
    if prompt == "add":
        result = num1 + num2
        print(result)
    elif prompt == "sub":
        result = num1 - num2
        print(result)
    elif prompt == "mul":
        result = num1 * num2
        print(result)
    elif prompt == "div":
        result = num1 / num2
        print(result)

calculator()