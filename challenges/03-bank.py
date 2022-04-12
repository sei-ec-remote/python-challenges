print("Welcome to Chase bank.")

action = input("What would you like to do? (deposit, withdraw, check_balance)")

total = 0

if action == "deposit":
    deposit = input("How much would you like to deposit?")
    total += int(deposit)
    print(f"Your current balance is {total}")
elif action == "withdraw":
    withdraw = input("How much would like yo withdraw?")
    total -= int(withdraw)
    print(f"Your current balance is {total}")
elif action == "check_balance":
    print(f"{total}")
else:
    print("Please enter a valid action :)!")
print("Have a nice day!")