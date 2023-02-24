# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

# Catch errors with
first_active = True

while first_active:
    action = input("What calculation would you like to do? (add, sub, mult, div)" ).lower()
    if action in 'add, sub, mult, div':
        first_active=False
    elif action == 'q':
        exit()
second_active = True
while second_active:
    number_one = input("What is the first number?" ).lower()
    number_two = input("What is the second number? ").lower()
    try: 
        number_one, number_two = int(number_one), int(number_two)
        second_active=False
        print('result \n')   
    except ValueError:
        print("Try again with a number this time!")

if action == 'add':
    print(number_one+number_two)
    active = False
elif action == 'sub':
    print('result \n')
    print(number_one-number_two)
    active = False
elif action == 'mult':
    print('result \n')
    print(number_one*number_two)
    active = False
elif action == 'div':
    print('result \n')
    print(number_one/number_two)
    active = False
