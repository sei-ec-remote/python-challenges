def banking():
    balance = 0
    print("Welcome to Chase bank.")
    display = input('Would you like to view your balance, make a deposit, or make a widthdrawal? (balance, deposit, withdrawal): \n')
    if (display == 'balance'):
        print(f'You balance is: {balance}.')
    elif (display == 'deposit'):
        deposit = float(input('How much would you like to deposit?: \n'))
        new_balance = deposit + balance
        print(f'After a deposit of {deposit}, your new balance is {new_balance}.')
    elif (display == 'withdrawal'):
        withdrawal = float(input('How much would you like to withdraw?: \n'))
        new_balance = balance - withdrawal
        print(f'After a withdrawal of {withdrawal}, your new balance is {new_balance}.')
    print("Have a nice day!")

banking()