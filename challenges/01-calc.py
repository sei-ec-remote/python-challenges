challenges/01-calc.py
# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

calc = input("What calculation would you like to do? (add, sub, mult, div)\n")
# print(calc)
first_number = int(input("What is the first number?\n"))

second_number = int(input("What is the second number?\n"))

if calc == 'add':
    print(first_number + second_number)
elif calc == 'sub':
    print(first_number - second_number)
elif calc == 'mult':
    print(first_number * second_number)
elif calc == 'div':
    print(first_number / second_number)