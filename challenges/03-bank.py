print("Welcome to Bank of America.")

# age = input("How old are you?\n")
# age = int(age)

Balance = 23084.76
check = input("Choose between: Deposit, Withdrawl, or Check Balance\n")

if check == 'Deposit':
    deposit = int(input("How much do you want to deposit?:\n "))
    print("Your total balance is now: ", deposit + Balance)
    print("Have a nice day!")
elif check == 'Withdrawl':
    withdraw = int(input("How much of our money are you taking?:\n "))
    print("Your total balance is now: ", Balance - withdraw)
    print("Have the day you deserve!")
elif check == 'Check_Balance':
    print("Total Balance: \n", Balance)