from hashlib import new


print("Welcome to Chase bank.")
print("Have a nice day!")
session = True
account = 0


def new_operation():
    global session
    input("something else? (yes, no) \n")
    if (new_operation == "yes"):
         session = True      
    elif (new_operation == "no"):
         session = False
        

while session == True:
    
    operation = input("What would you like to do? (deposit, withdraw, check balance) \n")

    if (operation == "deposit"):
        num1 = input("Deposit quantity \n")
        num1 = int(num1)
        account = account + num1
        print(f"Your account is now  {account}")
        new_operation()

    elif (operation == "withdraw"):
        num2 = input("Withdraw quantity \n")
        num2 = int(num2)
        account = account - num2
        print(f"Your account is now  {account}")
        new_operation()

    elif (operation == "check balance"):
        print(f"your balance is {account} \n")
        new_operation()
        print(session)


print("Have a nice day!")