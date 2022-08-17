# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

calc_type = input("What calculation would you like to do? (add, sub, mult, div) ")
num_one = input("What is number 1? ")
num_two = input("What is number 2? ")

if calc_type == "add":
    print(f"Your result is {int(num_one) + int(num_two)} ")
elif calc_type == "sub":
    print(f"Your result is {int(num_one) - int(num_two)} ")
elif calc_type == "mult":
    print(f"Your result is {int(num_one) * int(num_two)} ")
elif calc_type == "div":
    print(f"Your result is {int(num_one) / int(num_two)} ")




