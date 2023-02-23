# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

# Create a simple calculator that first asks the user what method they would like
# to use (addition, subtraction, multiplication, division) and then asks the user
# for two numbers, returning the result of the method with the two numbers. Here
# is a sample prompt:

# What calculation would you like to do? (add, sub, mult, div)
# add
# What is number 1?
# 3
# What is number 2?
# 6
# Your result is 9


def calculator():

    math = input("What calculation would you like to do? (add, sub, mult, div) ")

    num1 = int(input("What is number 1? "))
    num2 = int(input("What is number 2? "))

    if math == "add":
        print(num1 + num2)
    elif math == "sub":
        print(num1 - num2)
    elif math == "mult":
        print(num1 * num2)
    elif math == "div":
        print(num1 / num2)
    else:
        print("Invalid input")


calculator()