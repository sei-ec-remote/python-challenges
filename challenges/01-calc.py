# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

while True:
    choice = input("Enter choice(add, sub, mult, div): ")

    if choice in ('add', 'sub', 'mult', 'div'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if choice == 'add':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == 'sub':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == 'mult':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == 'add':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Invalid input, Please enter one of the choices.")