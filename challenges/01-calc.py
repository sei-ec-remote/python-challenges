# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.


def calculate():
    operation = input(
        "What calculation would you like to do? \nPlease select one: \n add, sub, mult, div\n ")
    num_one = int(input("What is the first number? "))
    num_two = int(input("What is the second number? "))
    if operation == 'add':
        result = num_one + num_two
    elif operation == 'sub':
        result = num_one - num_two
    elif operation == 'mult':
        result = num_one * num_two
    elif operation == 'div':
        result = num_one / num_two
    else:
        print("Not a valid option!")
    return f"Your result is {result}"


print(calculate())
