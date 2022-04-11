# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.


# Program make a simple calculator that can add, subtract, 
# multiply and divide using functions

# add function - take two numbers and add them.
def add(x, y):
   return x + y

# subtract function  - takes two numbers and subtracts them.
def subtract(x, y):
   return x - y

# multiply function - takes two numbers and multiplies them.
def multiply(x, y):
   return x * y

# divide function - takes two number and divides them.
def divide(x, y):
   return x / y

# Take input from the user for the calculation and for number 1 and number 2
choice = input("What calculation would you like to do? add, mult, div, sub \n")
num1 = int(input("What is number 1? \n"))
num2 = int(input("What is number 2? \n"))

# Perform the calculator function regardless of case and print the result
if choice.casefold() == 'add':
   print("Your result is ", add(num1,num2))
elif choice.casefold() == 'sub':
   print("Your result is ", subtract(num1,num2))
elif choice.casefold() == 'mult':
   print("Your result is ", multiply(num1,num2))
elif choice.casefold() == 'div':
   print("Your result is ", divide(num1,num2))
else:
   print("Invalid input")