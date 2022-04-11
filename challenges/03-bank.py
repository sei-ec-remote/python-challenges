print("Welcome to Chase bank.")
balance = 4000
method = input("what would you like to do? (deposit, withdraw, check_balance)")
if (method == "check_balance"):
    print(balance)
elif (method == "withdraw"):
    withdrawamt = int(input("how much?"))
    print(f"your current balance is: {balance - withdrawamt}")
elif (method == "deposit"):
    depositamt = int(input("how much?"))
    print(f"your current balance is: {balance + depositamt}")
else: 
    print("invalid option")


