# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

operator = input("Select operation: \n 1 or 'Add' \n 2 or 'Subtract' \n 3 or 'Multiply' \n 4 or 'Divide' ")
# a = 0
# b = 0

# add function
def add(a, b):
    return a + b

#subtract function
def subtract(a, b):
    return a - b

#multiply function
def multiply(a, b):
    return a * b

#divide function
def divide(a, b):
    return a / b

first_num = float(input("What is the first number? "))
second_num = float(input("What is the second number? "))

if operator == '1' or operator == 'Add':
    print(first_num, " + ", second_num ," = " ,add(first_num, second_num))
elif operator == '2' or operator == 'Subtract':
      print(first_num, " - ", second_num ," = " ,subtract(first_num, second_num))
elif operator == '3' or operator == 'Multiply':
      print(first_num, " * ", second_num ," = " ,multiply(first_num, second_num))
elif operator == '4' or operator == 'Divide':
      print(first_num, " / ", second_num ," = " ,divide(first_num, second_num))


