current_balance = 0

def check_balance():
    global current_balance
    print(f"Your current balance is ${current_balance}")

def deposit():
    amount = input("How much would you like to deposit?\n")
    if int(amount) < 0:
        print("Please write your deposit as a positive integer.")
        return
    global current_balance
    current_balance += int(amount)
    print(f"You have deposited ${amount}.")

def withdraw():
    amount = input("How much would you like to withdraw?\n")
    global current_balance
    if int(amount) < 0:
        print("Please write your withdrawal as a positive integer.")
        return
    elif int(amount) > current_balance:
        print("Insufficient funds.")
        return
    current_balance -= int(amount)
    print(f"You have withdrawn ${amount}.")


def bank_loop():
    action = input("What would you like to do? (deposit, withdraw, check balance)\n")

    if action == "deposit":
        deposit()
    elif action == "withdraw":
        withdraw()
    elif action == "check balance":
        check_balance()
    else:
        print("Please type your answer exactly as prompted.")
        bank_loop()
        return
    
    again = input("Would you like to perform another action?\ny/n  ")
    if again.lower() == "y" or again.lower() == "yes":
        bank_loop()
        return
    else:
        print("Thank you!")
        return





print("Welcome to Chase bank.")

bank_loop()

print("Have a nice day!")

