class ATM_Transactions():
    def __init__(self,balance=0):
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
        return self.balance
    def check_balance(self):
        return self.balance
    def withdraw(self,amount):
        self.balance -= amount
        return self.balance

account = ATM_Transactions(1000)


def open():
    transacting = True
    while transacting:
        action = input("What would you like to do? (deposit, withdraw, check_balance)\n").casefold()
        if action == 'withdraw'.casefold():
            amount = int(input("How much would you like to withdraw?\n"))
            print(f"Your current balance is {account.withdraw(amount)}")
        elif action == 'deposit'.casefold():
            amount = int(input("How much would you like to deposit?\n"))
            print(f"Your current balance is {account.deposit(amount)}")
        elif action == 'check_balance'.casefold():
            print(f"Your current balance is {account.balance}")
        else:
            print("Please try a different action")
        done = input("Are you finished?\n").casefold()
        if done == 'yes'.casefold():
            transacting = False
print("Welcome to Chase bank.")

open()

print("Have a nice day!")

