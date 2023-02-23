print("Welcome to Chase bank.")

balance = 110000
done = False

while not done:
    bank_account = input("What would you like to do? (deposit, withdraw, check_balance) ")
    if bank_account == "deposit":
        deposit = int(input("How much would you like to deposit?\n"))
        balance = balance + deposit
        print("Your current balance is ", balance)
    elif bank_account == "withdraw":
        withdraw = int(input("How much would you like to withdraw?\n"))
        balance = balance - withdraw
        print("Your current balance is ", balance)
    elif bank_account == "check_balance":
        print("Your current balance is ", balance)
    else:
        print("Invalid action. Please try again.")
        continue

    done = input("Are you done? (yes or no)\n")
    if done.lower() == "yes":
        print("Thank you!")
        done = True
    else:
        done = False

print("Have a nice day!")