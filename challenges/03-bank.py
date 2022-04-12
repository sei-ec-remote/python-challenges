print("Welcome to Chase bank.")
print("Have a nice day!")

balance = 4000
bank = input ("what would you like to do?: deposit, withdraw, check_balance, ")

if bank == 'check_balance':
    result = balance
elif bank == 'deposit':
    deposit = int(input ("how much would you like to deposit: "))
    result = balance + deposit
elif bank == 'withdraw':
    withdraw = int(input ("how much would you like to withdraw: "))
    result = balance - withdraw

print(f"you have {result} in your account")