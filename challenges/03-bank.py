print("Welcome to Chase bank.")


action = input('What would you like to do today? (deposit, withdraw, chk_balance)')

balance = 4000


if action == 'chk_balance':
    print('Your current balance is $', balance)

elif action == 'deposit':
    deposit = input('How much would you like to deposit today? $')
    balance = balance + int(deposit)
    print('Your current balance is $', balance)

elif action == 'withdraw':
    withdraw = input('How much will you like to withdraw?')
    balance = balance - int(withdraw)
    print('Your current balnace is $', balance)

else:
    print("Have a nice day!")

