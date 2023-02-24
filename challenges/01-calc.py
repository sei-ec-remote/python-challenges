# Challenge 1 - Calculator
# Create a simple calculator that first asks the user what method 
# they would like to use (addition, subtraction, multiplication, division) and then asks the user 
# for two numbers, returning the result of the method with the two numbers. Here is a sample prompt:What calculation would you like to do? (add, sub, mult, div)
# add
# What is number 1?
# 3
# What is number 2?
# 6
# # Your result is 9




# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

# Here is the function, it starts with def and then the name of the function which we will called
# in the end.


def calculator():

# Here we have the method, num 1 and num 2 as variables. 

    method = input("What calculation would you like to do? (add, sub, mult, div)\n")
    num1 = int(input("Type nubmer: \n"))
    num2 = int(input("Type nubmer: \n"))

# Here we have methods a variable and inside is an object which has the basic possibilties of a calcualtor.
    methods = {
    "add": num1 + num2,
    "mult": num1 * num2,
    "div": num1 / num2,
    "sub": num1 - num2,
  }

# We have and of statment to say if one of the methods inside the object is called 
# then is should return a method a user uses and the result of the two numbers. Otherwise, if the user
# commits a typo it should say to try again. 
    if (method in methods):
     return methods[method]
    else:
     return print("Invalid method! Try again.")

# Here we call the function we started to see the results in the terminal. 
print(calculator())


# python3 challenges/01-calc.py