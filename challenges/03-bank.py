print("Welcome to Chase bank.")

def bank():
    balance = input("Your current balance is:")
    action = input("What would you like to do? (deposit, withdraw, check_balance):")
    if action == 'check_balance':
        print(balance)
    elif action == 'deposit':
        deposit = input('How much would you like to deposit?')
        print(f"Your current balance is: {int(balance) + int(deposit)} ")
    elif action == 'withdraw':
        withdraw = input('How much would you like to withdraw?')
        print(f"Your current balance is: {int(balance) - int(withdraw)} ")    
    print("Have a nice day!")
bank()