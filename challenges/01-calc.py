# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

def simple_calc():
    calc_select = input("what would you like to do? Type '+', '-', '*', or '/': ")
    num1 = int(input('First calculated integer is: '))
    num2 = int(input('Second calculated integer is: '))
    if (calc_select == '+'):
        print(num1 + num2)
    elif (calc_select == '-'):
        print(num1 - num2)
    elif (calc_select == '*'):
        print(num1 * num2)
    elif (calc_select == '/'):
        print(num1 / num2)
    else:
        return 'no valid option entered'

calc_select()