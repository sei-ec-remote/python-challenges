# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

# Challenge 1 - Calculator
# Create a simple calculator that first asks the user what method they would like to use 
# (addition, subtraction, multiplication, division) and then asks the user for 
# two numbers, returning the result of the method with the two numbers. Here is 
# a sample prompt:


method=input(" Hi, this is a simple calc! What method would you like to use: +,-,*,/ ")
num1=input(" please enter num1 ")
num2=input(" please enter num2 ")

ans = eval(f"{num1}{method}{num2}")


print(f'{num1} {method} {num2} = {ans}')