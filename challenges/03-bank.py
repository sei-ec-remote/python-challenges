print("Welcome to Chase bank.")
balance = 2000

customer_answer= input(f'What would you like to do (deposit, withdraw, check_balance)? ')

if customer_answer == 'check_balance':
    print(f'Your total balance is {int(balance)} ')
elif customer_answer == 'deposit':
    deposit_value = input('How much would you like to deposit?')
    balance = balance + int(deposit_value)
    print(f'Your new balance is: {int(balance)}')
elif customer_answer == 'withdraw':
    withdraw_value = input('How much would you like to withdraw?')
    balance = balance - int(withdraw_value)
    print (f'Your new balance is: {int(balance)}')
print("Have a nice day!")

