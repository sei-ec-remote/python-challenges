banking = True
operation = ''
balance = 0

print("Welcome to Chase bank.")

while (banking):
    while operation != 'balance' and operation != 'withdraw' and operation != 'deposit':
        operation = input('How can we help you today? (balance, withdraw, deposit):\n').lower()
        if operation != 'balance' and operation != 'withdraw' and operation != 'deposit':
            print("Sorry, could not read input. Please try again.")
    if operation == 'balance':
        print(f"Your current balance is ${balance}.")
    elif operation == 'withdraw':
        withdrawal = int(input("How much would you like to withdraw?\n"))
        if withdrawal > balance:
            print(f"Sorry, but your balance is only ${balance}.")
        else:
            balance -= withdrawal
            print(f"You have withdrawn ${withdrawal}. Your new balance is ${balance}")
    elif operation == 'deposit':
        deposit = int(input("How much would you like to deposit?\n"))
        balance += deposit
        print(f"You have deposited ${deposit}. Your new balance is ${balance}.")
    
    bankBool = input("Would you like to continue banking? (Y / N): ").lower()
    if bankBool == 'n':
        banking = False
    else:
        operation = ''


print("Have a nice day!")

