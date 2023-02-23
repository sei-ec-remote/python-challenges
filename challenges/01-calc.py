# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

calc = input("What calculation would you like to do? (add, sub, mult, div) ")

num1 = int(input("What is number 1? "))
num2 = int(input("what is number 2? "))

if calc == "add":
    result = num1 + num2
elif calc == "sub":
    result = num1 - num2
elif calc == "mult":
    result = num1 * num2
elif calc == "div":
    result = num1 / num2
else:
    print("Incorrect calculation selection")
    result = none

if result is not None:
    print("Your answer is", result) 