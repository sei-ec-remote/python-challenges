# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

calculation = input("What calculation would you like to do? (add, sub, mult, div)\n")
num_1  = input("What is number 1?\n")
num_2  = input("what is number 2?\n")

if calculation == "add":
    print("Your result is " ,int(num_1) + int(num_2))
elif calculation == "sub":
    print("Your result is " ,int(num_1) - int(num_2))
elif calculation == "mult":
    print("Your result is " ,int(num_1) * int(num_2))
elif calculation == "div":
    print("Your result is " ,int(num_1) / int(num_2))





