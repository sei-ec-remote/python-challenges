balance = 1000
# end = False

print("Welcome to Chase bank.")


text = input('What would you like to do? (deposit, withdraw, check balance)')

if text == 'deposit':
    deposit = input('How much would you like to deposit?')
    balance = balance + int(deposit)
    print(f'Your current balance is {balance}')

elif text == 'withdraw' and balance > 0 :
    withdraw = input('How much would you like to withdraw?')
    if int(withdraw) > balance:
        print("insufficient funds")
    else:
        balance = balance - int(withdraw)


elif text == 'check balance':
    print(f'Your current balance is {balance}')

# if text == 'done' or text == 'exit':
#     end = True






print("Thank you!")
