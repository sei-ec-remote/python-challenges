# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

method = input("What calculation would you like to do? (add, sub, mult, div)")
print(method)
num1 = input("What is number 1?")
print(num1)
num2 = input("What is number 2?")
print(num2)

if method == "add":
    print(f"Your result is {int(num1) + int(num2)}")
elif method == "sub":
    print(f"Your result is {int(num1) - int(num2)}")
elif method == "mult":
    print(f"Your result is {int(num1) * int(num2)}")
elif method == "div":
    print(f"Your result is {int(num1) / int(num2)}")


