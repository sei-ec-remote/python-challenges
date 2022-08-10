print("Welcome to Chase bank.")
print("Have a nice day!")

balance = 4000

def balance_query():
    print(f'Your balance is {balance}.')
    done = input("Are you done? y/n\n")
    if done == "n":
        homepage()

def deposit(number):
    global balance
    balance += number
    print(f'Deposit Received. Your new balance is {balance}.')
    done = input("Are you done? y/n\n")
    if done == "n":
        homepage()

def withdrawal(number):
    global balance
    if number <= balance:
        balance -= number
        print(f'Withdrawal confirmed. Your new balance is {balance}.')
    else:
        print("ERROR: withdrawal amount cannot exceed current balance.")
    done = input("Are you done? y/n\n")
    if done == "n":
        homepage()

def homepage():
    global balance
    action = input("What would you like to do today? You can type 'balance', 'deposit', or 'withdrawal'.\n")
    if action == 'balance':
        balance_query()
    elif action == 'deposit':
        money_to_add = input('How much would you like to deposit?\n')
        deposit(int(money_to_add))
    elif action == 'withdrawal':
        money_to_withdraw = input('How much would you like to withdraw?\n')
        withdrawal(int(money_to_withdraw))
    else:
        print("I'm sorry, I don't understand that action.")
        homepage()

homepage()