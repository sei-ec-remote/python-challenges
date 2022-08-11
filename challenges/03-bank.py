print("Welcome to Chase bank.")

balance = 500
finished = "no"

def bank_transaction():
  global balance
  global finished

  while (finished != "yes"):
    response = input("What would you like to do? (deposit, withdraw, check_balance)")

    if (response == "deposit"):
      amount = int(input("How much would you like to deposit?"))
      balance = balance + amount
      print(f"Your current balance is {balance}")
      finished = input("Are you finished? (yes or no)")
    elif (response == "withdraw"):
      amount = int(input("How much would you like to withdraw?"))
      balance = balance - amount
      print(f"Your current balance is {balance}")
      finished = input("Are you finished? (yes or no)")
    elif (response == "check_balance"):
      print(f"Your current balance is {balance}")
      finished = input("Are you finished? (yes or no)")
      
bank_transaction()


print("Have a nice day!")

