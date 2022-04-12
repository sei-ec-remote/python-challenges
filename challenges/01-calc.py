# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

# Create a simple calculator that first asks the user what method 
# they would like to use (addition, subtraction, multiplication, division)
# and then asks the user for two numbers, returning the result of the method
# with the two numbers. Here is a sample prompt:

from distutils.log import error


operator = input("What calculation would you like to do? (add, sub, mult, div)")
num1  = input("What is number 1?")
num2  = input("What is number 2?")

def calculate (operator, num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    if(operator == 'add'):
        return num1 + num2
    elif(operator == 'sub'):
        return num1-num2
    elif(operator == 'mult'):
        return num1*num2
    elif(operator == 'div'):
        try:
            return num1/num2
        except: 
            return error
    else: return "your operator input was not of the options(add, sub, mult, div)"

print(calculate(operator, num1, num2))

