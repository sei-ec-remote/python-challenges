# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

operation = input("What type of calculation would you like to perform? (add, sub, mult, div) ")

if operation == 'add':
    num1 = input("Enter the first number ")
    num2 = input("Enter the second number ")
    sum = int(num1) + int(num2)
    print(f"your answer is {sum}")
elif operation =='sub':
    num1 = input("Enter the first number ")
    num2 = input("Enter the second number ")
    total = int(num1) - int(num2)
    print(f"your answer is {total}")
elif operation =='mult':
    num1 = input("Enter the first number ")
    num2 = input("Enter the second number ")
    total = int(num1) * int(num2)
    print(f"your answer is {total}")
elif operation =='div':
    num1 = input("Enter the first number ")
    num2 = input("Enter the second number ")
    total = int(num1) / int(num2)
    print(f"your answer is {total}")