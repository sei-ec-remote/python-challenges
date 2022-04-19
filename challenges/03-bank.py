print("Welcome to Chase bank.")

def bank(base_balance):
    print(f'Your balance is: {base_balance}')
    balance = base_balance
    event = input('what would you like to do today?(Deposit, Withdraw, Check Balance) ')
    if event == 'Deposit':
        amount = input('What amount would you like to Deposit?')
        balance += int(amount)
        print(f'Your balance is now: {balance}')
        return event
    elif event == 'Withdraw':
        amount = input('What amount would you like to Withdraw?')
        balance -= int(amount)
        print(f'Your balance is now: {balance}')
        return event
    elif event == 'Check Balance':
        input(f'Your balance is: {balance}')
    else:
        print("Have a nice day!")

bank(2000)
