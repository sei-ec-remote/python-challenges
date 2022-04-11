print("Welcome to Chase bank.")
print("Have a nice day!")

balance = 4000
choice = input("What would you like to do? (deposit, withdraw, check_balance: ")

if (choice == "deposit"):
    deposit = int(input("How much would you like to deposit?: "))
    balance = balance + deposit
    print(f"Your current balance is: ${balance}")
elif (choice == "withdraw"):
    withdraw = int(input("How much would you like to withdraw?: "))
    balance = balance - withdraw
    print(f"Your current balance is: ${balance}")
elif (choice == "check_balance"):
    print(f"Your current balance is: ${balance}")
else:
    print("Please enter a valid method")