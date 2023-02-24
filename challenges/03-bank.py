
balance = 5000

def deposit(amt):
    bal = balance
    bal = bal + int(amt)
    print("Your new balance is\n", bal)

def withdraw(amt):
    bal = balance
    bal = bal - int(amt)
    print("Your new balance is\n", balance)

def chk_balance():
    print("Your account balance is\n", balance)


print("Your current balance is:\n", balance)
action = input("What would you like to do? (deposit, withdraw, balance)\n")

if action == "deposit":
    dep_amt = input("How much?\n")
    deposit(dep_amt)
elif action == "withdraw":
    wit_amt = input("How much?\n")
    if wit_amt <= balance:
        deposit(wit_amt)
    else:
        print("You don't have that much money!")
elif action == "balance":
    chk_balance()
