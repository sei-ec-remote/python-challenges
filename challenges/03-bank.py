print("Welcome to Chase bank.")

balance = 10000
done = False

def deposit(amount):
    global balance
    balance += amount
    print(f"Your current balance is ${balance}")

def withdraw(amount):
    global balance
    if balance >= amount:
        balance -= amount   
        print(f"withdrawing ${amount}")
        print(f"Your current balance is ${balance}")    
    else:
        print(f"Sorry, do not have enough to withdraw ${amount}")

def check_balance():
    print(f"Your current balance is ${balance}")

while not done:
    transaction = input("What would you like to do? (deposit, withdraw, check_balance) \n")

    if transaction == 'check_balance':
        check_balance()
    elif transaction == 'deposit':
        amount = int(input("How much would you like to deposit? \n "))
        deposit(amount)
    elif transaction == 'withdraw':
        amount = int(input("How much would you like to withdraw? \n"))
        withdraw(amount)
    else:
        print("Something went wrong...try again")

    finished = input("Are you done? (yes or no) \n")
    if finished == 'yes':
        done = True
    elif finished == 'no':
        pass
    else:
        print("Invalid input..") 
        
print("Thank you! Have a nice day!")

