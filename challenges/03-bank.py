print("Welcome to Chase bank.")

def deposit(balance):
    num = int(input("How much would you like to deposit?\n"))
    balance += num
    check_balance(balance)

def withdraw(balance):
    num = int(input("How much would you like to withdraw?\n"))
    if num > balance:
        print("Insufficient Funds\n")
        check_balance(balance)
    else:    
        balance -= num
        check_balance(balance)

def check_balance(balance):
    print("Your current balance is", balance)
    again = input("Are you done?\n")
    if (again.lower() == "no") or (again.lower() == "n"):
        start_transaction(balance)
    else:
        print("Have a nice day!")

def start_transaction(balance):
    print("Your current balance is:\n", balance)
    action = input("What would you like to do? (deposit, withdraw, check_balance)\n")
    if action == "deposit":
        deposit(balance)
    elif action == "withdraw":
        withdraw(balance)
    elif action == "check_balance":
        check_balance(balance)
    else:
        print("Invalid Request. Bink Bonk.")
        # start_transaction(balance)

start_transaction(100)

