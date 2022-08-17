print("Welcome to Chase bank.")

balance = 5000

def show_balance(balance):
    return print(f"Your balance is {balance} ")

def withdraw(balance):
    withdraw_amount = input("How much would you like to withdraw? ")
    balance = balance - int(withdraw_amount)
    return print(balance)

def deposit(balance):
    deposit_amount = input("How much would you like to deposit? ")
    balance = balance + int(deposit_amount)
    return print(balance)

loop = True
while(loop):
    user_option = input("Would you like to 1: See your balance', 2: Make a withdrawal, 3: Make a deposit, or 4: Exit. Please enter a number: ")
    if user_option == "1":
        show_balance(balance)
    elif user_option == "2":
        withdraw(balance)
    elif user_option == "3":
        deposit(balance)
    else: break

print("Have a nice day!")

