print("Welcome to Chase bank.\n")
# print("Have a nice day!")

print("Would you like to: \n")
print("1. check account balance")
print("2. withdraw cash")
print("3. make a deposit ")

operation = input()

if operation == "1":
    print("your account balance is -19,000. You broke\n")

elif operation == "2":
    print("insuffecient funds\n")

elif operation == "3":
    print("Gimme that money\n")

print("all set ? yes : no  ")  

response = input()

if response == "yes":
    print("thank you, goodbye")
elif response == "no":
    print("get a job, you broke")
print()


class BankAccount():
    def __init__(self, acct_type, balance=0):
        self.type = acct_type
        self.balance = balance
        self.overdraft_fees = 0

    def __str__(self):
        status = 'balance: {} \noverdraft fees: {}'.format(self.balance, self.overdraft_fees)
        return status

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount
        if (self.balance < 0):
            self.overdraft_fees += 20
        return amount

my_acct = BankAccount('checking', 6)
my_acct.deposit(50)
my_acct.withdraw(25)
print(my_acct)
my_acct.withdraw(35)
print(my_acct)