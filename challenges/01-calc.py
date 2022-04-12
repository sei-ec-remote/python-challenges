# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

from audioop import add

# set variables and the input questions
operator_choice = input('What calculation would you like to do? (add, sub, mult, div)')
number1 = int(input('What is number 1?'))
number2 = int(input('What is number 2?'))
result = ''
# if, elif statement depending on the operator chosen
if operator_choice == 'add':
    result = number1 + number2
elif operator_choice == 'sub':
    result = number1 - number2
elif operator_choice == 'mult':
    result = number1 * number2
elif operator_choice == 'div':
    result = number1/number2
#print results
#print(result)
# this printed the numbers as strings (ex. 5 + 5 = 55)
#int needs to be added to the number1 and number2
print(f"The total is: {result}")

