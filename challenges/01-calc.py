# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.


calc = input('What is the calculation that you want to do (add, substract, multiply, divide)? ')

first_number = input('First Number: ')
second_number = input('Second Number ')

if calc == 'add':
    print(f'The addition result is {int(first_number) + int(second_number)}')
elif calc == 'substract':
    print(f'The substraction result is {int(first_number) - int(second_number)}')
elif calc == 'multiply':
    print(f'The multiplication result is {int(first_number) * int(second_number)}')
else:
    print(f'The division result is {int(first_number) / int(second_number)}')

