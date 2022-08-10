balance = 420
active = True

def deposit(dep):
    global balance
    balance += dep
    print(f'new balance: {balance}.00. Have a nice day!')

def withdrawal(withd):
    global balance
    balance -= withd
    print(f'new balance: {balance}.00. Have a nice day!')

def check():
    print(f'balance: {balance}.00. Have a nice day!')

print('Welcome!')
action = input('what would you like to do today? ')
if action == 'deposit':
    amount = int(input('How much? '))
    deposit(amount)

elif action == "withdrawal":
    amount = int(input('How much? '))
    withdrawal(amount)

elif action == 'balance':
    check()
