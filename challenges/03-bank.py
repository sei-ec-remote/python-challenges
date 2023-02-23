balance = 5000

def bank (balance):
    print(f'===============================')
    print("====Welcome to Chase bank.=====")
    print(f'===============================')
    print(f'your current balance is \n {balance} ')
    msg = input('What would you like to do? (deposit, withdraw or balance)')
    if msg=='balance':
        print(f'your current balance is \n {balance} ')
        msg = input('are you done? (yes or no)')
    elif msg == 'deposit':
        msg= input('How much would you like to deposit?')
        balance += int(msg)
        print(f'Your new balance is {balance}')
        msg = input('are you done? (yes or no)')
    elif msg == 'withdraw':
        msg= input('How much would you like to withdraw?')
        balance -= int(msg)
        print(f'Your new balance is {balance}')
        msg = input('are you done? (yes or no)')
    else:
        print('ERROR')
        msg = input('you want to cancel the operation? (yes or no)')

    if msg == 'no':
        bank(balance)
    else:
        print("Have a nice day!")

bank(balance)