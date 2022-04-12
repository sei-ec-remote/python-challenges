# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

def calculator():
    op = input('What calculation would you like to do? (add, sub, mult, div):')
    a = input('Enter your first number:')
    b = input('Enter your second number:')
    if op == 'add':
        print(f"your result is {int(a) + int(b)}")
    elif op == 'sub':
        print(f"your result is {int(a) - int(b)}")
    elif op == 'mult':
        print(f"your result is {int(a) * int(b)}")
    elif op == 'div':
        print(f"your result is {int(a) / int(b)}")
    

calculator()