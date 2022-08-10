print("Welcome to Chase bank.")

question = input("Please enter a selection: display balance, withdraw, deposit\n")

balance = 500.00

if question == 'display balance':
    print(f'Your current balance is ${balance}')
if question == 'withdraw':
    withdraw = int(input("Please enter the amount you would like to withdraw:"))
    if withdraw > 500.00:
        print("Sorry, your balance is too low for this transaction.")
    elif withdraw < 500.00:
        new_balance = balance - withdraw
        print("You're account balance is now:", f"${new_balance}")
if question == 'deposit':
    deposit = int(input("Please enter the amount you would like to deposit:"))
    print(f"Transaction complete, your new balance is ${balance + deposit}")
# else: 
#     print("I'm sorry I don't understand, please try again.")

question_2 = input('Are you done? Y/N\n')
if question_2 == 'Y':
    print("Have a nice day!")
elif question_2 == 'N':
    question = input("Please enter a selection: display balance, withdraw, deposit\n")

    if question == 'display balance':
        print(f'Your current balance is ${balance}')
    if question == 'withdraw':
        withdraw = int(input("Please enter the amount you would like to withdraw:"))
        if withdraw > 500.00:
            print("Sorry, your balance is too low for this transaction.")
        elif withdraw < 500.00:
            new_balance = balance - withdraw
            print("You're account balance is now:", f"${new_balance}")
    if question == 'deposit':
        deposit = int(input("Please enter the amount you would like to deposit:"))
        print(f"Transaction complete, your new balance is ${balance + deposit}")

print("Thank you! Please come again.")

