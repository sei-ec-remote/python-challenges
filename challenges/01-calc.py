# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.


def calculator():
    choice = input('What method they would like to use addition, subtraction, multiply, or divide?')

    num1 = int(input('please input your first number.'))
    num2 = int(input('please input your second number.'))
    answer = ()

    if choice == 'addition':
        answer = num1 + num2
    elif choice == 'subtraction':
        answer = num1 - num2
    elif choice == 'multply':
        answer = num1 * num2
    elif choice == 'divide':
        answer = num1 / num2

    print(f'The results are {answer}.')
calculator()

