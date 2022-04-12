
balance = 1000


print("Welcome to Chase bank.")


done = "no"

bank_selection = input("Enter action from the following: display balance, withdraw, or deposit ")
while done != "yes":
    if bank_selection == "balance":
        print(f"current balance is {balance}")
        done=input("Are you done? ")
        if done=="no":
            bank_selection = input("Enter action from the following: display balance, withdraw, or deposit ")
    elif bank_selection == "withdraw":
        withdraw = input("enter amount to withdraw ")
        balance -= int(withdraw)
        print(f"Your new balance is {balance}")
        done=input("Are you done? ")
        if done=="no":
            bank_selection = input("Enter action from the following: display balance, withdraw, or deposit ")
    elif bank_selection == "deposit":
        deposit = input("Enter amount you would like to deposit ")
        balance += int(deposit)
        print(f"Your new balance is {balance}")
        done=input("Are you done? ")
        if done=="no":
            bank_selection = input("Enter action from the following: display balance, withdraw, or deposit ")
    else:
        print('error with selection')
        bank_selection=input("Enter action from the following: display balance, withdraw, or deposit ")


print("Have a nice day!")

