# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

# define the function that performs the operation
def calculator(op, num1, num2):
    if op == "add":
        return num1 + num2
    elif op == "sub":
        return num1 - num2
    elif op == "mult":
        return num1 * num2
    elif op == "div":
        return num1 / num2

# get user input for the operation and the numbers
op = input("What calculation would you like to do? (add, sub, mult, div) ")
num1 = float(input("What is number 1? "))
num2 = float(input("What is number 2? "))

# call the function with the user input and display the result
result = calculator(op, num1, num2)
print("Your result is", result)

