print("Welcome to Chase bank.")
print("Have a nice day!")

balance = 50



def bank_time():
    global balance
    action = input("What would you like to do? (deposit, withdraw, check_balance)\n")
    if action == "deposit":
        amount = input("How much would you like to deposit?\n")
        amount = int(amount)
        balance += amount
        print(f"Your current balance is {balance}")
    elif action == "withdraw":
        amount = input("How much would you like to withdraw?\n")
        amount = int(amount)
        balance -= amount
        print(f"Your current balance is {balance}")
    elif action == "check_balance":
        print(f"Your current balance is {balance}")
    finished()

def finished():
    answer = input("Are you done? (yes/no)\n")
    if answer == "yes":
        print("Thank you")
    elif answer == "no":
        bank_time()


bank_time()