print("Welcome to Chase bank.")

balance = int(input("Your current balance is:\n"))

def run_app():
    
    action = input("What would you like to do? (deposit, withdraw, check_balance)\n")

    if action == "withdraw":
        withdrawal = int(input("How much would you like to withdraw?\n"))
        print(f"Your new balance is:\n{balance - withdrawal}")
    elif action == "deposit":
        deposit = int(input("How much would you like to deposit?\n"))
        print(f"Your new balance is:\n{balance + deposit}")
    else:
        print(f"Your current balance is:\n{balance}")
        
    done = input("Are you done?\n")
    if done == "no" or done == "No" or done == "NO":
        run_app()
    else:
        print("Thank you!")

run_app()

print("Have a nice day!")

