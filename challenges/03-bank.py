print("Welcome to Chase bank.")
print("Have a nice day!")

amount = 1000



def banking_questions():
    action = input('What would you like to to?\n1. Display Balance\n2. Withdraw \n3. Deposit \n4. Quit\n ')
    if action == "1":
        print('Your Account Balance is', amount)
    elif action == "2":
        withdrawal_amount = float(input("How much would you like to withdraw?\n"))
        print('Your remaining balance is', amount-withdrawal_amount)
    elif action == "3":
        deposited = float(input('How much would you like to deposit? '))
        print('Your current Balance is :', deposited + amount)
    elif action == "4":
        print('Thank You for banking with us!')
    else:
        print('Invalid choice. Please enter a valid choice. \n')

banking_questions()