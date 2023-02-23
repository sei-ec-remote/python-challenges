print("Welcome to Chase bank.")
balance = float(input("What is your balance?\n"))
while True:
    action = input("What would you like to do today? (deposit, withdraw, check_balance)\n")
    current_balance = balance
    if action == 'deposit':
        deposit = float(input("How much would you like to deposit?\n"))
        current_balance = balance + deposit
        print("Your current balance is", current_balance)
        balance = current_balance
    elif action == 'withdraw':
        withdraw = float(input("How much would you like to withdraw?\n"))
        current_balance = balance - withdraw
        print("Your current balance is", current_balance)
        balance = current_balance
    elif action == 'check_balance':
        print("Your current balance", current_balance)
    done = input("Would you like to do another transaction? (yes/no): ")
    if done == 'no':
        print("Have a nice day!")
        break
        
