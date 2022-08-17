print("Welcome to Chase bank.")

ask = input('How can I help you today? Respond with: balance, withdraw, or deposit. ')

balance = 1000

# check balance
if ask == 'balance':
    print(f'Your account balance is: ${balance}')
elif ask == 'withdraw':
    subtract_balance = input('How much would you like to withdraw? You cannot exceed your account balance. $')
    after_withdrawal = balance - int(subtract_balance)
    print(f'Your new balance is: ${after_withdrawal}.')
elif ask == 'deposit':
    add_balance = input('How much would you like to deposit? $')
    after_deposit = balance + int(add_balance)
    print(f'Your new balance is ${after_deposit}.')
else:
        print("Have a nice day!")