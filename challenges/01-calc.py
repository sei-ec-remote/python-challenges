# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

def calc():
    # declare all of the inputs I need
    method = input('What calculation would you like to do? (add,sub.mult,div)')
    # nums must use int to convert to number instead o string
    num1 = int(input('What is the first number?'))
    num2 = int(input('What is the second number?'))

    #  declare the different types of math that can be refrenced later in the func
    types = {
        'add': num1 + num2,
        'sub': num1 - num2,
        'div': num1 / num2,
        'mult': num1 * num2
    }

    # if statment that looks for method in  the user input that matches one of the types
    if (method in types):
        # if the method is found in the types then return the total of whatever method was chosen
        return types[method]
    else:
        # catch for any error that occurs if method is not valid (or total is a decimal)
        # prints the return as well as none(null)
        return print('Input valid method')


print(calc())