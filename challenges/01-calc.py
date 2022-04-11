# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.
# Challenge 1 - Calculator

# Create a simple calculator that first asks the user what method they would like
# to use (addition, subtraction, multiplication, division) and then asks the user
# for two numbers, returning the result of the method with the two numbers. Here
# is a sample prompt:

# ```
# What calculation would you like to do? (add, sub, mult, div)
# add
# What is number 1?
# 3
# What is number 2?
# 6
# Your result is 9
# ```

op = input(
    "What calculation would you like to do? (add, sub, mult, div)")

num1 = int(input(f"What is the first number you'd like to {op}?"))
num2 = int(
    input(f"What is the second number you'd like to {op} to/by {num1}?"))

result = 0
if op == "add":
    result = num1 + num2
elif op == "sub":
    result = num1 - num2
elif op == "mult":
    result = num1 * num2
elif op == "div":
    result = num1 / num2


print(f"{num1} {op} {num2} = {result}")
