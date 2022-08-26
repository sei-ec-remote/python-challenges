# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.


calculator = input('What operation do you want to choose? (add, sub, mult, div)\n')

num_1 = int(input("What is the number 1?\n"))

num_2 = int(input("What is the number 2?\n"))

if calculator == 'add':
    print('answer:\n')
    print(num_1 + num_2)
elif calculator == 'sub':
    print('answer:')
    print(num_1 - num_2)
elif calculator == 'mult':
    print('answer:')
    print(num_1 * num_2)
elif calculator == 'div':
    print('answer:')
    print(num_1 / num_2)