# Create a prompt that asks the user if they would like to display their balance, withdraw or deposit. Write three methods to perform these calculations and output the result to the user.

# Gather user input using the input function. Note that input always returns user input as a string. You have to manually convert it to an int or a float to make it behave like number. Also, end the input prompt with a \n newline character if you want the user to type in on the next line.

# age = input("How old are you?\n")
# age = int(age)
# Here is a sample output:

# Your current balance is
# 4000
# What would you like to do? (deposit, withdraw, check_balance)
# deposit
# How much would you like to deposit?
# 1000
# Your current balance is 5000
# Are you done?
# yes
# Thank you!

print("Welcome to Chase bank.")
current_balance = int(input('Your current balance is: \n'))
operation = input('What would you like to do? (deposit, withdraw, check_balance) \n')
if operation == 'deposit':
    number_two = int(input('How much would you like to deposit? \n'))
elif operation == 'withdraw':
    number_two = int(input('How much would you like to withdraw? \n'))
elif operation == 'check_balance':
    print(f'Your balance is {current_balance}. \n')
else:
    print('Please double check the action you selected at top. It must match one of the three listed values! \n')

if operation == 'deposit':
    current_balance = current_balance + number_two
    print(f'Your current balance is {current_balance}.')
elif operation == 'withdraw':
    current_balance = current_balance - number_two
    print(f'Your current balance is {current_balance}.')

are_done = input('Are you done? (yes, no)')
if are_done == 'yes':
    print('Thank you! Have a nice day!')
else: 
    print(f'Your current balance is: {current_balance}.')
    operation = input('What would you like to do? (deposit, withdraw, check_balance) \n')
    if operation == 'deposit':
        number_two = int(input('How much would you like to deposit? \n'))
    elif operation == 'withdraw':
        number_two = int(input('How much would you like to withdraw? \n'))
    elif operation == 'check_balance':
        print(f'Your balance is {current_balance}. \n')
    else:
        print('Please double check the action you selected at top. It must match one of the three listed values! \n')
        
    if operation == 'deposit':
        current_balance = current_balance + number_two
        print(f'Your current balance is {current_balance}.')
    elif operation == 'withdraw':
        current_balance = current_balance - number_two
        print(f'Your current balance is {current_balance}.')
