print("Welcome to Chase bank.")


current_balance = 10000

# Display Balance, Withdraw, Deposit
def display_balance():
    print(f"This is your current balance: ${current_balance}")

def withdraw(amt):
    global current_balance
    current_balance -= int(amt)
    display_balance()
    active = False

def deposit(amt):
    global current_balance
    current_balance += int(amt)
    display_balance()
    active = False

active = True

while active:
    action = input("What would you like to do today? (1 - Withdraw, 2 - Deposit, 3 - See Current Balance or q to quit) ")
    try: 
        if action == 'q':
            print("Have a nice day!")
            exit()
        if action == '1':
            amount = input("How much would you like to withdraw? ")
            withdraw(amount)
        elif action == '2':
            amount = input("How much would you like to deposit? ")
            deposit(amount)
        elif action == '3':
            display_balance()
        else:
            print("Please choose 1, 2, 3 only, or q to quit!")
    except ValueError:
        print("Only numbers please!")
        
