print("Welcome to Chase bank.")
current_balance = 0
initial = input(
    'What would you like to do today?(deposit, withdraw, check balance)\n')

def deposit():
    if initial == 'deposit':
        q_deposit = input('how much would you like to deposit?\n')
        q_deposit = int(q_deposit)
        new_balance = q_deposit + current_balance
        print(f'Your current balance is now {new_balance}')
        last_prompt = input('Are you done?\n')
        if last_prompt == 'yes':
            print("Have a nice day!")
        

def withdraw(): 
    if initial == 'withdraw':
        q_withdraw = input('how much would you like to withdraw?\n')
        q_withdraw = int(q_withdraw)
        new_balance = current_balance - q_withdraw 
        print(f'Your current balance is now {new_balance}')
        last_prompt = input('Are you done?\n')
        if last_prompt == 'yes':
            print("Have a nice day!")
        

def check_balance(): 
    if initial == 'check balance':
        print(f'Your current balance is {current_balance}')
        last_prompt = input('Are you done? \n')
        if last_prompt == 'yes':
            print("Have a nice day!")
        

print("Have a nice day!")



if initial == 'deposit':
    deposit()

elif initial == 'withdraw':
    withdraw()
elif initial == 'check balance':
    check_balance()
else: 
    print('Invalid option')