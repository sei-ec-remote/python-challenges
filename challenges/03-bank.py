print("Welcome to Chase bank.")

print('Would you like to check your balance? Please enter yes or no')
check_balance = input()

balance = 10000
deposit = 0
withdraw = 0


if check_balance == 'yes':
    print('Your current balance is:', balance)

print('Do you want to deposit or widthdraw? Enter d or w')
transaction = input()

if transaction == 'd':
    print('How much would you like to deposit?')
    deposit = input()
    print('Your current balance is:', int(deposit) + balance)
elif transaction == 'w':
    print('How much would you like to withdraw?')
    withdraw = input()
    print('Your current balance is:', balance - int(withdraw))
    
print("Have a nice day!")

