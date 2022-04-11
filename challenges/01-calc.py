# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

#created a function with 3 parameters
def calculator(operator, num_1, num_2):
    if operator == 'add' or operator == 'addition':
        ans = num_1 + num_2
        print(f'Your result is {ans}')
    elif operator == 'sub' or operator == 'subtraction':
        ans = num_1 - num_2
        print(f'Your result is {ans}')
    elif operator == 'mult' or operator == 'multiplication':
        ans = num_1 * num_2
        print(f'Your result is {ans}')
    elif operator == 'div' or operator == 'division':
        ans = num_1 / num_2
        print(f'Your result is {ans}')
    else:
        print('That is not an option')

operator = input('What calculation would you like to do? (add, sub, mult, div) ')
num_1 = int(input('What is number 1? '))
num_2 = int(input('What is number 2? '))
calculator(operator, num_1, num_2)


