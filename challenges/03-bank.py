question = input("Here are the possible actions available to you: balance, withdraw, deposit. \n")

def bank_transaction(str):
    balance = 0
    if str == "deposit":
        deposit = input("Please type the amount of your deposit (ex: 50) \n")
        balance += int(deposit)
    elif str == "withdraw":
        withdrawl = input("Please type the amount of your withdrawl (ex: 50) \n")
        balance -= int(withdrawl)
    elif str == "balance":
        print(f"Your current balance is: {balance}")
    return (f"Your current balance is: {balance}")

print(bank_transaction(question))
