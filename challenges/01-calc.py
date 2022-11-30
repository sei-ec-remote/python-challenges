# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

def simple_calc():
    user_choice = input("what would you like to do? Type '+', '-', '*', or '/': ")
    num1 = int(input('what is number 1? '))
    num2 = int(input('what is number 2? '))
    if (user_choice == '+'):
        print(num1 + num2)
    elif (user_choice == '-'):
        print(num1 - num2)
    elif (user_choice == '*'):
        print(num1 * num2)
    elif (user_choice == '/'):
        print(num1 / num2)
    else:
        return 'no valid option entered'

simple_calc()