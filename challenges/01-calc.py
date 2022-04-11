# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

def calculator():
    method = input("What calculation would you like to do? (add, sub, mult, div)") 

    num2 = input("What is number 1?")
    num3 = input("What is number 2?")

    if method == "add":
        print(f"Your result is {int(num2) + int(num3)}")
    elif method == "sub":
        print (f"Your result is {int(num2) - int(num3)}")
    elif method == "mult":
        print (f"Your result is {int(num2) * int(num3)}")
    elif method == "div":
        print (f"Your result is {int(num2) / int(num3)}")
    else:
        print ("That is not an calc option")

calculator()
