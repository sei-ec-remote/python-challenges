print("Welcome to Chase bank.")
keep_going = 'y'
balance = 5000
def bank():
    global balance
    operation = input('To see your balance, please type - balance\n To deposit funds please type - deposit\n To withdraw funds please type - withdraw\n')
    if operation == 'balance':
        print(f'Your balance is {balance}\n')
    elif operation == 'withdraw':
        if balance == 0:
            print('You will need to deposit funds first, sorry.')
        else: 
            withdraw_amount = int(input('Please type the amount you would like to withdraw:\n'))
            balance -= withdraw_amount
    elif operation == 'deposit':
        deposit = int(input('please type the amount you are depositing'))
        balance += deposit
while keep_going == 'y':
    bank()
    print(f'Your final balance is {balance}\n')
    keep_going = input('Press y to continue, or n to exit')


print("Have a nice day!")

 