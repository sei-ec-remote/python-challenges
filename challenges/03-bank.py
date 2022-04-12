print("Welcome to Chase bank.")



question = input("Would you like to display your balance, withdraw funds, or deposit funds? Please enter one of the following: balance, withdrawl, deposit. \n")

def bank_transaction(str):
    balance = 0
    if str == "deposit":
        deposit = input("Please type the amount of your deposit (ex: 50) \n")
        balance += int(deposit)
    elif str == "withdrawl":
        withdrawl = input("Please type the amount of your withdrawl (ex: 50) \n")
        balance -= int(withdrawl)
    else:
        print(f"Your current balance is: {balance}")
    return (f"Your current balance is: {balance}")

print(bank_transaction(question))

print("Have a nice day!")



