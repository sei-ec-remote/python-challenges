# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.


print('What calculation would you like to do? (add, sub, mult, div)')
calc= input()

print('what is number 1')
num1= input()

print('what is number 2')
num2= input()

if calc == 'add':
    print(int(num1) + int(num2))
elif calc == 'sub':
    print(int(num1) - int(num2))
elif calc == 'mult':
    print(int(num1) * int(num2))
elif calc == 'div':
    print(int(num1)/int(num2))
elif calc != 'add' or 'sub' or 'mult' or 'div':
    print('I did not understand the calculation, please try again')


