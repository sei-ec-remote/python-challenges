# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

def calculator():
    operation=input('What operation would you like to perform? (add, sub, mult, div)')
    num_1=int(input('What is the first number?'))
    num_2=int(input('What is the second number?'))
    if operation == 'add':
        ans=num_1+num_2
    elif operation == 'sub':
        ans=num_1-num_2
    elif operation == 'mult':
        ans=num_1*num_2
    elif operation == 'div':
        ans=num_1/num_2
    print('The result is', ans)

calculator()