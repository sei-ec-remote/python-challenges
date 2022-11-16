balance = 0

def bank_transactions():
    print("Welcome to Chase bank.")
    transaction = input("What would you like to do? (deposit, withdrawal, check_balance)")
    global balance
    if transaction == "deposit":
        amount = input("How much would you like to deposit? $")
        balance += int(amount)
    elif transaction == "withdrawal":
        amount = input("How much would yopu like to withdraw? $")
        if balance < int(amount):
            print(f"You only have ${balance}")
        else:
            balance -= int(amount)
    elif transaction == "check_balance":
        print(f"Your current balance is ${balance}")
    else:
        print("Please enter valid transaction type.")

    complete_transaction = input("Anything else? (yes, no)")
    if complete_transaction == "yes":
        bank_transactions()
    else:
        print("Have a nice day!")

bank_transactions()
