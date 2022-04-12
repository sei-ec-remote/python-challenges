# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.
operation = input("Which basic operation [add, sub, mul, div] ")

if (operation == "add"):
    num1 = input("enter first number ")
    num1 = int(num1)
    num2 = input("enter second number ")
    num2 = int(num2)
    print("result is {}".format(num1 + num2))

elif (operation == "sub"):
    num1 = input("enter first number ")
    num1 = int(num1)
    num2 = input("enter second number ")
    num2 = int(num2)
    print("result is {}".format(num1 - num2))

elif (operation == "div"):
    num1 = input("enter first number ")
    num1 = int(num1)
    num2 = input("enter second number ")
    num2 = int(num2)
    print("result is {}".format(num1 / num2))

elif (operation == "mul"):
    num1 = input("enter first number ")
    num1 = int(num1)
    num2 = input("enter second number ")
    num2 = int(num2)
    print("result is {}".format(num1 * num2))
