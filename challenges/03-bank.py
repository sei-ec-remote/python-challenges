
balance = 500


def bank_account():
 transaction = input("What would you like to do? (deposit, withdraw, check_balance)\n" )

withdraw = int(input("how much?\n"))
deposit = int(input("how much?\n"))
check_balance = int(input("Your current balance is\n"))

transactions = {
    "withdraw": balance - withdraw,
    "deposit": balance + deposit,
    "check_balance": balance
    
  }

if (transaction in transactions):

#  return transactions[transaction]
print(bank_account())

print("Welcome to Chase bank.")
print("Have a nice day!")