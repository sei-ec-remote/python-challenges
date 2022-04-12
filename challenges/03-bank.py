print("Welcome to Chase bank.")
print("Have a nice day!")



bank_act = input("Please Select your task: (deposit, withdraw, balance)")

total = 4000

if bank_act == "deposit":
     deposit = input("How much will you deposit?")
     total += int(deposit)
     print(f"Your current balance is {total}")
elif bank_act == "withdraw":
     withdraw = input("How much will you withdraw?")
     total -= int(withdraw)
     print(f"Your current balance is {total}")
elif bank_act == "balance":
     print(f"{total}")
else:
     print("Thank you!")
print("Have a nice day!") 