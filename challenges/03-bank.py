
# global bank balance
balance = 0

# Ask the user for the deposit amount and show the balance
def deposit():
    global balance
    deposit = float(input("How much would you like to deposit? \n"))
    balance += deposit
    print("Your current balance is ", balance)

# Ask the user for the withdrawal amount and show the balance
def withdraw():
    global balance
    withdraw = float(input("How much would you like to withdraw? \n"))
    balance -= withdraw
    print("Your current balance is ", balance)

# Check the balance and display to the user
def check_balance():
    global balance
    print("Your current balance is ", balance)


#  Greetings and ask what they would like to do
print("Welcome to Chase bank.")
print("Have a nice day!")

choice = input("What would you like to do? (deposit, withdraw, check_balance) \n")

# Loop until you are done.
while choice.casefold() != "done":
    if choice.casefold() == 'deposit':
        deposit()
    elif choice.casefold() == 'withdraw':
        withdraw()
    elif choice.casefold() == 'check_balance':
        check_balance()
    else:
        print("Invalid input")

    yes_or_no = input("Are you done? \n")
    if yes_or_no == "yes":
        choice = 'done'
        print("Thank You!")
    else:
        choice = input("What would you like to do? (deposit, withdraw, check_balance) \n")