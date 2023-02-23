# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.
calculator = input("What calculation do you wanna use? (add, sub, multi, div): ")
num1 = int(input("What is the first number: "))
num2 = int(input("What is the second number: "))

if calculator == 'add':
    print(num1 + num2)
elif calculator == 'sub':
    print(num2 - num1)
elif calculator == 'multi':
    print(num1 ** num2)
elif calculator == 'div':
    print(num2 / num1)