print("Welcome to Chase bank.")
balance = 4000

def display_balance():
    print("Your current balance is", balance)

def withdraw():
    global balance
    amount = float(input("How much would you like to withdraw?\n"))
    if amount > balance:
        print("Insufficient funds")
    else:
        balance -= amount
        print("Your new balance is", balance)

def deposit():
    global balance
    amount = float(input("How much would you like to deposit?\n"))
    balance += amount
    print("Your new balance is", balance)

print("Your current balance is")
display_balance()

while True:
    action = input("What would you like to do? (deposit, withdraw, check_balance)\n")
    if action == "deposit":
        deposit()
    elif action == "withdraw":
        withdraw()
    elif action == "check_balance":
        display_balance()
    else:
        print("Invalid action")

    done = input("Are you done?\n")
    if done == "yes":
        print("Thank you, Have a Nice Day!")
        break

        

