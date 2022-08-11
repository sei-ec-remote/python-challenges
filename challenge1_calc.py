userOperator = input('What calculation would you like to do? (add, sub, mult, div)\n')
num1 = int(input('What is number 1?\n'))
num2 = int(input('What is number 2?\n'))
if userOperator == 'add':
    print('Your result is', num1 + num2)
elif userOperator == 'sub':
    print('Your result is', num1 - num2)
elif userOperator == 'mult':
    print('Your result is', num1 * num2)
else:
    print('Your result is', num1 / num2)