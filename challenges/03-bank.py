print("Welcome to Chase bank.")

balance = 200
done = False

# ATM code
def deposit(amount):
    global balance
    balance += amount
    balance = round(balance, 2)
    print(f'Balance after deposit: ${balance}\n')

def withdraw(amount):
    global balance
    amount = round(amount, 2)
    if balance >= amount:
        balance -= amount
        print(f'Dispersing {amount}')
        print(f'Balance after withdraw: ${balance}!')
    else:
        print('Please deposit money into this account.\n')

def check_balance():
    print(f'Your balance is ${balance}!')

# Menu Code
while not done:
    action = input('What would you like to do? (type: "deposit", "withdraw", "check_balance") \nTo end transaction, type "done". ')

    if action == 'done' or action == 'exit':
        done = True
    elif action == 'balance' or action == 'check_balance':
        check_balance()
    elif action == 'deposit':
        amount = float(input('How much would you like to deposit?: '))
        deposit(amount)
    elif action == 'withdraw':
        amount = float(input('How much would you like to withdraw?: '))
        withdraw(amount)
    else:
        print('Please enter one of the above commands...')


print("Have a nice day!")

