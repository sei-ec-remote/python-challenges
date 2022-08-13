from unicodedata import decomposition


print("Welcome to Chase bank.")
print("Have a nice day!")

balance = 0
amount = 0
while True:
  print(f"Your current balance is ${balance:.2f}.")
  option = input("What would you like to do? (deposit, withdraw, balance) ")
  if option == "deposit":
    amount = float(input("How much would you like to deposit? "))
    balance += amount
  elif option == "withdraw":
    amount = float(input("How much would you like to withraw? "))
    balance -= amount
  elif option == "balance":
    pass
  else:
    print("Sorry, your command was not recognized.")