print("Welcome to Chase bank.")


def manage_account(balance):
    
    selection = input("What would you like to do? Select by number:\n 1 - Deposit\n 2 - Withdraw\n 3 - Check balance\n 4 - Exit\n ")
    if selection == "4":
        print("Have a nice day!")
    else:
        if selection == "1":
            amount = int(input("How much would you like to deposit?\n "))
            balance += amount 
        elif selection == "2":
            amount = int(input("How much would you like to withdraw?\n "))
            balance -= amount
        elif selection == "3":
            balance = balance
        print(f"Your current balance is {balance}")
        manage_account(balance)

manage_account(5000)