print("")
print("Welcome to Chase bank.")
print("")

cur_bal = 4000

action = input("What would you like to do?\n(check_balance, withdraw, deposit, quit)\n")

if (action == "check_balance"):
    print(f"Your current balance is: ${cur_bal}")
elif (action == "withdraw"):
    withdraw_amt = int(input("How much would you like to withdraw?\n"))
    cur_bal -= withdraw_amt
    print(f"Your current balance is: ${cur_bal}")
elif (action == "deposit"):
    deposit_amt = int(input("How much would you like to deposit?\n"))
    cur_bal += deposit_amt
    print(f"Your current balance is: ${cur_bal}")
elif (action == "quit"):
    print("Have a nice day!")
else:
    print("Please select a valid option.")
