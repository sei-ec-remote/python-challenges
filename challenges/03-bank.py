print("Welcome to Chase bank.")

initbalance = 0
def cycle(balance):
    action = input("What would you like to do? (deposit, withdraw, check_balance)\n")
    if action == "deposit":
        dep = input("how much would you like to deposit?\n")
        try:
            dep = float(dep)
            newbal = balance + dep
        except ValueError:
            print("invalid input")
            newbal = balance
        
    elif action == "withdraw":
        wi = input("how much would you like to withdraw?\n")
        try:
            wi = float(wi)
            newbal = balance - wi
        except ValueError:
            print("invalid input")
            newbal = balance
    elif action=="check_balance":
        newbal = balance
    else:
        print("invalid action")

    print("your balance is now: " + str(newbal) + " $")
    end = input("done? (yes,no)\n")
    if end == "yes":
        print("have a nice day")
    else:
        cycle(newbal)


cycle(initbalance)

