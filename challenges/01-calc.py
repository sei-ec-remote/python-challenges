# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

operation = input("What calculation would you like to do? (add, sub, mult, div) ")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

output = ""
if operation == "add":
  output = f"The sum of your numbers is {num1 + num2}."
elif operation == "sub":
  output = f"{num1} - {num2} is {num1 - num2}."
elif operation == "mult":
  output = f"The product of your numbers is {num1 * num2}."
elif operation == "div":
  output = f"{num1} divided by {num2} is {num1 / num2}."

print(output)