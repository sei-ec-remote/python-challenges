print("Welcome to Chase bank.")

balance = 4000

print('Your current balance is:', balance)

def transaction():
    global balance
    choice = input('What would you like to do? (deposit, withdraw, check_balance)')
    if choice == 'deposit':
        deposit_amount = int(input('How much would you like to deposit?'))
        balance += deposit_amount
        cancel()
    elif choice == 'withdraw':
        withdraw_amount = int(input('Withdraw how much?'))
        balance -= withdraw_amount
        cancel()
    elif choice == 'check_balance':
        print(f'Your current balance is {balance}')
        cancel()
    else:
        print('Invalid choice')
        cancel()

def cancel():
    cont = input('Are you done? (yes, no)')
    if cont == 'yes':
        print('Thank you!')
    elif cont == 'no':
        transaction()

transaction()

print("Have a nice day!")

