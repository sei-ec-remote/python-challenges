# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

method = input('what method they would like to use (addition, subtraction, multiplication, division)\n')
num_one = int(input('enter first number\n'))
num_two = int(input('enter second number\n'))

if method == 'addition' or method == '+':
    print(num_one + num_two)
elif method == 'subtraction' or method == '-':
    print(num_one - num_two)
elif method == 'multiplication' or method == '*' or method == 'x':
    print(num_one * num_two)
elif method == 'division' or method == '/':
    print(num_one / num_two)
else:
    print(' please input a valid method')