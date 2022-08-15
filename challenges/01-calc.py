# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

calc = input("What calculation would you like to do? (add, sub, mult, div)")
int_one =input("What is the first number?")
int_two =input("What is the second number?")

if calc.lower() == "add":
    print(f"Your result is {int(int_one) + int(int_two)}")
elif calc.lower() == "sub":
    print(f"Your result is  {int(int_one) - int(int_two)}")
elif calc.lower() == "mult":
    print(f"Your result is  {int(int_one) * int(int_two)}")
elif calc.lower() == "div":
    print(f"Your result is  {int(int_one) / int(int_two)}")
