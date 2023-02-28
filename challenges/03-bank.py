print("Welcome to Chase bank.")

def display_balance(balance):
    print("Your current balance is: ", balance)

def withdraw(balance, amount):
    if amount > balance:
        print("Insuffecient balance. Cannot withdraw")
    else: 
        balance -= amount
        print("Withdrawal successful. Your new balance is: ", balance)
    return balance

def deposit(balance, amount):
    balance += amount
    print("Deposit successful. Your new balance is: ", balance)
    return balance

balance = 4000
while True:
    print("\nWhat would you like to do?")
    print("1. Display Balance")
    print("2. Withdraw money")
    print("3. Deposit money")
    print("4. Exit")

    choice = input("Enter choice (1-4): ")

    if choice == '1':
        display_balance(balance)

    elif choice == '2':
        amount = int(input("Enter amount to withdraw: "))
        balance = withdraw(balance, amount)

    elif choice == '3':
        amount = int(input("Enter amount to deposit: "))
        balance = deposit(balance, amount)

    elif choice == '4':
        print("Have a nice day!")
        exit()

    else:
        print("INvalid choice, please enter a number from 1 to 4.")

