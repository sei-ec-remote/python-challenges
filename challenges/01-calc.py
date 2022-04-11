# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.


method = input("What calculation would you like to do? (add, sub, mult, div): ")
num = int(input("first number: "))
num2 = int(input("second number: "))

if method == "add":
    print(num + num2)
elif(method == "sub" ):
    print(num - num2)
elif(method == "mult"):
    print(num * num2)
elif(method == "div"):
    print(num/num2)
else:
    print("invalid method")
