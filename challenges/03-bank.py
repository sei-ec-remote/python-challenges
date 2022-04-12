print("Have a nice day!")
print("Welcome to Chase bank.")

balance = 10000
done = "no"

def bank():

    global balance
    global done

    while (done != "yes" ):
        action = input("what would you like to do?")

        if (action == "deposit"):
            deposit = int(input("How much would you like to deposit"))
            balance = balance + deposit
            print(f"Your balance is {balance}")
            done = input("Are you done?")
        elif (action == "withdraw"):
            withdraw = int(input("How much would you like to withdraw?"))
            balance = balance - withdraw
            print(f"Your balance is {balance}")
            done = input("Are you done?")
        elif (action == "balance"):
            print(f"Your balance is {balance}")
            done = input("Are you done?")

bank()
