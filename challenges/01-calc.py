# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

operator = input("What calculation would you like to do? (add, sub, mult, div) \n")
num1 = input("What is number 1? \n")
num2 = input("What is number 2? \n")

def calc(operation, numb1, numb2):
    if operation == "add":
        return int(numb1) + int(numb2)
    elif operation == "sub":
        return int(numb1) - int(numb2)
    elif operation == "mult":
        return int(numb1) * int(numb2)
    elif operation == "div":
        return int(numb1) / int(numb2)

print(calc(operator, num1, num2))