# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

operator = input("Input your operator (add,sub,mult,div): ")
first_number = int(input("Input the first number: "))
second_number = int(input("Input the second number: "))

if operator == "add" :
    result = (first_number + second_number)
    print(f"The result is: {result}")
elif operator == "sub":
    result = (first_number - second_number)
    print(f"The result is: {result}")
elif operator == "mult":
    result = (first_number * second_number)
    print(f"The result is: {result}")
elif operator == "div" :
    result = (first_number / second_number)
    print(f"The result is: {result}")
else:
    print("Invalid")