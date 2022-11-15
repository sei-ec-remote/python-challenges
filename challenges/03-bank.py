print("Welcome to Chase bank.")
def bankin(balance):
    
    
    action = input('Would you like to view your balance, make a deposit or make a withdraw? (balance, withdraw, deposit) ')
    if(action == 'balance'):
        print('Your current balance is: ', balance)
        again = input('Are you done? (yes or no) ')
        if(again == 'yes'):
            print("Have a nice day!")
        else:
            bankin(balance)
    elif(action == 'withdraw'):
        amount_withdraw = input('How much would you like to withdraw? ')
        amount_withdraw = int(amount_withdraw)
        balance = balance - amount_withdraw
        print('Your new account balance is: ', {balance})
        again = input('Are you done? (yes or no) ')
        if(again == 'yes'):
            print("Have a nice day!")
        else:
            bankin(balance)
    elif(action == 'deposit'):
        print('Your current account balance is: ', balance)
        amount_deposit = input('How much would you like to deposit? ')
        amount_deposit = int(amount_deposit)
        balance = balance + amount_deposit
        print('Your new account balance is: ', {balance})
        again = input('Are you done? (yes or no) ')
        if(again == 'yes'):
            print("Have a nice day!")
        else:
            bankin(balance)
    else:
        print('Not a valid input')
        bankin(balance)

bankin(4000)

