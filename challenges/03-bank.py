deposit = 0
balance = 300

action = input('What would you like to do? (deposit, withdraw, check_balance, exit) ')

if action == 'exit':
    print('Thank you for banking with Python 🐍.')

elif action == 'check_balance':
    print(f'Your balance is ${balance}.')

elif action == 'deposit':
    amount = int(input('How much? '))
    balance += amount

    print(f'Your new balance is ${balance}.')

elif action == 'withdraw':
    amount = int(input('What amount? '))
    
    balance -= amount

    print(f'your new balance is ${balance}')

    if (balance < 0):
        print(f'You have overdrawn your account. Please transfer funds to resolve your balance.')

else:
    print('Invalid Input')

print("Thank you for banking with Python 🐍. Have a nice day!")