print("Welcome to Chase bank.")
print("Have a nice day!")


def deposit():
    deposit_amount = float(input('How much would you like to deposit? \n'))
    global balance
    balance = balance + deposit_amount
    check_balance()

def withdraw():
    withdraw_amount = float(input('How would you like to withdraw? \n'))
    global balance
    balance -= withdraw_amount
    check_balance()

def check_balance():
    print('Your current balance is \n', balance)

balance = 0

done = 'no'
while done != 'yes':
    operation = input("What would you like to do? (deposit, withdraw, check_balance) \n")
    if operation == 'deposit':
        deposit()
        done = input('Are you done? \n')
    elif operation == 'withdraw':
        withdraw()
        done = input('Are you done? \n')
    elif operation == 'check_balance':
        check_balance()
        done = input('Are you done? \n')

print('Thank you!')