# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

def calculator():
    method = input("Enter a method. add/subtract/multiply/divide \n")
    number1 = int(input("Enter number 1 \n"))
    number2 = int(input("Enter number 2 \n"))

    if method == "add":
        solution = number1 + number2
        operator = "plus"
    elif method == "subtract":
        solution = number1 - number2
        operator = "minus"
    elif method == "multiply":
        solution = number1 * number2
        operator = "times"
    elif method == "divide":
        solution = number1 / number2
        operator = "divided by"
    else:
        print("Unable to calculate solution. Please try again")
    
    print("{} {} {} is {}".format(number1, operator, number2, solution))

calculator()