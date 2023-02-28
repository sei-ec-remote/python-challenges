# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

method = input("What calculation would you like to do? +, -, *, / : ")

num1 = float(input("What is number 1?: "))
num2 = float(input("What is number 2?: "))

if method == "+":
    result = num1 + num2
elif method == "-":
    result = num1 - num2
elif method == "*":
    result = num1 * num2
elif method == "/":
    result = num1 / num2
else:
    print("invalid method selected")
    exit()

print("Your result is: ", result)
