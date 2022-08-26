print("Welcome to Chase bank.")
balance = int(input("Your current balance is:\n"))
def chase_bank():

    global balance
    to_do = input("What would you like to do? (deposit, withdraw, check_balance)\n")

    if to_do == "deposit":
        deposit = int(input("How much would you like to deposit?\n"))
        balance = balance + deposit
        print(f"Your new balance is:\n{balance}")

    elif to_do == "withdraw":
        withdrawal = int(input("How much would you like to withdraw?\n"))
        balance = balance - withdrawal
        print(f"Your new balance is:\n{balance}")

    else:
        print(f"Your current balance is:\n{balance}")

    done = input("Are you done?\n")

    if done == "no" or done == "No" or done == "NO":
        chase_bank()

    else:
        print("Thank you!")


chase_bank()
print("Have a nice day!")

