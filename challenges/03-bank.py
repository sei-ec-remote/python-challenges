print("Welcome to Chase bank.")

balance = float(input("Your current balance is: $"))
while True:
    while True:
        action = input("What would you like to do? (deposit, withdraw, check_balance): ")
        if action.lower() not in ('deposit', 'withdraw', 'check_balance'):
            print("Not a bank operation")
        else:
            break

    if action == 'check_balance':
        print('Current Balance is: $', balance)
    else:
        amount = input('How much would you like to ' + action + '? $')
        if action == 'deposit':
            balance += float(amount)
        else:
            balance -= float(amount)

    while True:
        answer = input('Are you done?(Yes/No): ')
        if answer.lower() not in ('yes', 'no'):
            print("Not an expected input")
        else:
            break

    if answer == 'yes':
        break

print("Thank you! Have a nice day!")