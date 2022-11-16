# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.



print("welcome to the most basic, primitive but functional calculator!!!")


exit = False
print('To + type < add> \n to - type < sub > \n to * type < mult > \n to / type < div >')
while not exit:
    result = 0
    #number 1
    num1 = input('Choose your First number: ')
    if num1.isalpha():
        print('WRONG INPUT CHOOSE A NUMBER')
        continue
    else:
        num1 = int(num1)
    #number 2
    num2 = input('Choose your Second number: ')
    if num2.isalpha():
        print('WRONG INPUT CHOOSE A NUMBER')
        continue
    else:
        num2 = int(num2)
    #operator
    operator = input('Choose your operator: ')
    if operator == 'add':
        result = num1 + num2
        print(result)
    elif operator == 'sub':
        result = num1 - num2
        print(result)
    elif operator == 'mult':
        result = num1 * num2
        print(result)
    elif operator == 'div':
        result = num1 / num2
        print(result)
    else:
        print('WRONG OPERATOR INPUT  TRY AGAIN!')

    ask = input('Do you need to calculator again?\n Yes or No: ').lower()
    if ask == 'no':
        exit = True
    else:
        continue
    