print("Welcome to Chase bank.")

intro = input("Would you like to display your balance, withdraw or deposit? Please type: balance or withdraw or deposit.\n")

if intro.lower() == "balance":
    print(f"Your current balance is 500")
    last_ques = input("Are you done? Please type: yes or no\n")
    if last_ques.lower() == "yes":
        print("Have a nice day!")
    if last_ques.lower() == "no":
        intro = input("Would you like to display your balance, withdraw or deposit? Please type: balance or withdraw or deposit.\n")

if intro.lower() == "deposit":
    deposit = input("How much would you like to deposit today\n")
    deposit=int(deposit)
    print(f"Your current balance is now {500 + deposit}")
    last_ques = input("Are you done? Please type: yes or no\n")
    if last_ques.lower() == "yes":
        print("Have a nice day!")
    if last_ques.lower() == "no":
        intro = input(
            "Would you like to display your balance, withdraw or deposit? Please type: balance or withdraw or deposit.\n")

if intro.lower() == "withdraw":
    withdraw = input("How much would you like to withdraw today?\n")
    withdraw = int(withdraw)
    print(f"Your current balance is now {500 - withdraw}")
    last_ques = input("Are you done? Please type: yes or no\n")
    if last_ques.lower() == "yes":
        print("Have a nice day!")
    if last_ques.lower() == "no":
        intro = input(
            "Would you like to display your balance, withdraw or deposit? Please type: balance or withdraw or deposit.\n")

    
    
    
