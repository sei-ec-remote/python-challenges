print("Welcome to Chase bank.")
finish = 'no'
balance = 40000

while finish == 'no':
    print(f'Your current balance is ${balance}')
    action = input('What would you like to do? (deposit, withdraw, check_balance)\n')
    if action == 'deposit':
        deposit_amt = input('How much would you like to deposit?\n')
        balance += int(deposit_amt)
        print(f'Your current balance is ${int(balance)}')
        finish = input('Are you done? (yes or no)\n')
    if action == 'withdraw':
        withdraw_amt = input('How much would you like to withdraw?\n')
        if int(withdraw_amt) > int(balance):
            print("Insufficient fund")
            finish = input('Are you done? (yes or no)\n')
        else:
            balance -= int(withdraw_amt)
            print(f'You current balance is ${int(balance)}')
            finish = input('Are you done? (yes or no)\n')
    if action == 'check_balance':
        print(f'Your current balance is ${balance}')
        finish = input('Are you done? (yes or no)\n')
        
print("Thank you! Have a nice day!")

