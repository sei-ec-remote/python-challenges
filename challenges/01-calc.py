# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.


def calculate():
    question = input(
        'What calculation would you like to do? (add, sub, mult or div) ')
    pick_a_num = input(int('Pick a number: '))
    pick_a_num_two = input(int('Pick a second number: '))

    if question == 'add':
        sum = pick_a_num + pick_a_num_two
        print(sum)
    elif question == 'sub':
        difference = pick_a_num - pick_a_num_two
        print(difference)
    elif question == 'mult':
        product = pick_a_num * pick_a_num_two
        print(product)
    elif question == 'div':
        quotient = pick_a_num / pick_a_num_two
        print(quotient)
    else:
        print('Error')


calculate()
