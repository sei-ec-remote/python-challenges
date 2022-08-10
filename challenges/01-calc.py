# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

question = input("What calculation would you like to do\n")

number_1 = input("What is the first number?\n")

number_2 = input("What is the second number?\n")

if question == 'add':
    print(f'Answer is: {int(number_1) + int(number_2)}')
elif question == 'subtract':
    print(f'Answer is: {int(number_1) - int(number_2)}')
elif question == 'multiply':
    print(f'Answer is: {int(number_1) * int(number_2)}')
elif question == 'divide':
    print(f'Answer is: {int(number_1) / int(number_2)}')
else:
    print(f"What does {question} mean?")