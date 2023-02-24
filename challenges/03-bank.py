balances = 5000
finished = False

def balance():
    print(f'Your balance is ${balances}.')    

def deposit(num):
    global balances
    balances += num
    balance()

def withdraw(num):
    global balances
    balances -= num
    balance()


while not finished:
    action = input('What would you like to do? (deposit, withdraw, balance, exit) ')

    if action == 'exit':
        print("Thank you, come again.")
        finished = True
    elif action == 'balance':
        balance()
    elif action == 'deposit':
        amount = int(input('What is the amount? '))
        deposit(amount)
    elif action == 'withdraw':
        amount = int(input('What is the amount? '))
        withdraw(amount)
