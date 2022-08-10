print("Welcome to Chase bank.")
atm = input("I Would Like To: (view_balance, withdrawal, deposit)\n")
# print(atm)

global balance
balance = 1000


if atm == "view_balance" or atm == "VIEW_BALANCE":
    print (f'Your balance is $ {balance} ')
if atm == 'withdrawal' or atm =='WITHDRAWAL':
    withdrawal_num = input("Enter the amount you would like to withdraw?\n")
    balance = balance - int(withdrawal_num)
    print(f"Your new balance is $ {balance}")
if atm == 'deposit' or atm =='DEPOSIT':
    deposit_num = input("Enter the amount you'd like to add?\n")
    balance = balance + int(deposit_num)
    print(f'Your new balance is $ {balance}')





print("Thank Yout For Being A Chase Member, Have a nice day!")

