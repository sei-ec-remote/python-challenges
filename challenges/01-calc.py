# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

op = input("Pick an operator (+, -, *, /)")
n1 = int(input("enter first number"))
n2 = int(input("enter second number"))

if op == "+":
    answer = n1 + n2
elif op == "-":
    answer = n1 - n2
elif op == "x":
    answer = n1 * n2
elif op == "/":
    answer = n1 / n2

print(f"{n1} {op} {n1} = {answer}")
