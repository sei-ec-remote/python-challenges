# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

def calculator(num1, num2):
    select = input('Select an operator: add, sub, mul, div : ')

    total = 0
    if select == "add":
        total = num1 + num2
        print('Sum = ',total)
        return total
    elif select == "sub":
        total = num1 - num2
        print('Subtraction = ',total)
        return total
    elif select == "mul":
        total = num1 * num2
        print('Multiple = ',total)
        return total
    else: 
        total = num1/num2
        print('Quotient ->' ,total)
        return total


calculator(10, 20)

