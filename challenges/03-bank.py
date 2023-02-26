balance = 4000
choose_deposit = 'deposit'
choose_withdraw = 'withdraw'

print("Welcome to Chase bank.")
choice = input('What would you like to do? (deposit, withdraw, check_balance) \n')
print('Your current balance is: \n', balance)

while True:
    choice = input('Are you done?: ')
    if (choice == 'no'):
      choice = input('What would you like to do? (deposit, withdraw, check_balance) \n')

    if (choice == 'deposit'):
      deposit = input('How much would you like to deposit?: ')
      balance += int(deposit)
      print('Your balance is: $', balance)

    elif (choice == 'withdraw'):
      withdraw = input('How much would you like to withdraw?: ')
      balance -= int(withdraw)
      print('Your balance is: $', balance)

    elif (choice == 'check_balance'):
      print('Your balance is: $', balance)

    elif (choice == 'yes'):
      print("Have a nice day!")
      break




# print(bank(choice, balance))
