# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.
def calc():
    method = input("What calculation would you like to do? (add, sub, mult, div)\n")
    num1 = int(input("What is number 1?\n"))
    num2 = int(input("What is number 2?\n"))

    if method == "add":
        result = num1 + num2
    elif method == "sub":
        result = num1 - num2
    elif method == "mult":
        result = num1 * num2
    elif method == "div":
        result = num1 / num2
    else:
        return print("Illegal Opperator")
    return print("Your result is", result)

calc()