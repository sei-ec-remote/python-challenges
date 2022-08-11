# Use the `input()` function to prompt a user to enter something.

# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

# Create a simple calculator that first asks the user what method they would like
# to use (addition, subtraction, multiplication, division) and then asks the user
# for two numbers, returning the result of the method with the two numbers. Here
# is a sample prompt:

# ```


calculator = input('What calculation would you like to do?(add, sub, mult, div)')
# add
question_two = input('What is number 1?')
# 3
question_three = input('What is number 2?')
# 6
# Your result is 9
# ```
if calculator == 'add':
    print("The sum of", question_two, "and", question_three, "=", int(question_two) + int(question_three))
elif calculator == 'sub':
    print("The remainder of", question_two, "and", question_three, "=", int(question_two) - int(question_three))
elif calculator == 'mult':
    print("The product of", question_two, "and", question_three, "=", int(question_two) * int(question_three))
elif calculator == 'div':
    print("The quotient of", question_two, "and", question_three, "=", int(question_two) / int(question_three))

