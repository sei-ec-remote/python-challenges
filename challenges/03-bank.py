print("Welcome to Chase bank.")
current_balance = 4000
print(f"Your current balance is {current_balance}")

def transaction(action, amount):
    if action == "deposit":
        new_balance = int(current_balance) + amount
        print(f'Your new balance is ${new_balance}')
    elif action == "withdraw":
        if amount > current_balance:
            print(f'You do not have enough funds to withdraw ${amount} from your balance.')
        else:
            new_balance = int(current_balance) - amount
            print(f'Your new balance is ${new_balance}')
    elif action == "check_balance":
        print(f'This is your current balance: ${current_balance}')
    else:
        print(f"That is not an option, please try again!")

action = (input('What would you like to do? (deposit, withdraw, check_balance) \n')).lower()
if (action == "check_balance"):
    print(f'This is your current balance: ${current_balance}')
else:
    amount = int(input(f"How much would you like to {action}?\n$"))
    transaction(action, amount)

print("Have a nice day!")