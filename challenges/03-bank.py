print("Welcome to Chase bank.")

def usr_bank():
    banking = True
    balance = 0
    repeat = False
    while banking:
        if repeat == True:
            prompt = input("Would you like to continue? (Yes / no) ")
            if prompt.casefold() == 'yes':
                pass
            else:
                break
        prompt = input("What would you like to do? Type(widthdraw, deposit, or check_balance) ")
        if prompt == 'withdraw':
            withdraw_amount = int(input("How much would you like to withdraw? "))
            balance -= withdraw_amount
            repeat = True
        elif prompt == 'deposit':
            deposit_amount = int(input("How much would you like to deposit? "))
            balance += deposit_amount
            repeat = True
        elif prompt == 'check_balance':
            print(balance)
            repeat = True


usr_bank()

print("Have a nice day!")

