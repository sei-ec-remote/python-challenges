
def bank_transaction(starting_balance):
    print("Welcome to Chase bank.")
    print(f"Your starting balance is: {starting_balance}") 
    balance = starting_balance
    prompt = input("What would you like to do? (Deposit, Withdraw, Check Balance):")
    if prompt == "Deposit" or prompt == "deposit":
        amount = input("How much would you like to Deposit:")
        balance += int(amount)
        print(f"Your current balance is: {balance}")
    elif prompt == "Withdraw" or prompt == "withdraw":
        amount = input("How much would you like to withdraw:")
        balance -= int(amount)
        print(f"Your current balance now is: {balance}")
    elif prompt == "Check Balance" or prompt == "check balance":
        input(f"Here's your current balance:{balance}")
        print("thank you for visiting")
    else:
        print("Thanks for visiting")
bank_transaction(4000)

