#bank atm
print("Welcome to The Great Gatsby Bank.")
class BankAccount():
    def __init__(self,owner, account_type='checking', balance=100):
        self.owner = owner
        self.type = account_type
        self.balance = balance

    def __str__(self):
        return f'Hello {self.owner}! On your {self.type} account, you have ${self.balance} available'
    
    
    def check_balance(self):
        print(f"You have ${self.balance} available on your account")
    
    def deposit(self,amount):
        self.balance += amount
        print(f'Thanks for your deposit! of ${amount}! \n Your current balance is now ${self.balance}')

    def withdraw(self,amount):
        if self.balance > 0 and self.balance >= amount:
            self.balance -= amount
            print(f' amount withdrawn ${amount}, your current available balance is ${self.balance} ')
        else:
            print(f'you do not have enough to withdraw {amount}, your current balance is {self.balance}')

#class person account holder
random_person = BankAccount('Random Person', 'checking', 3000)
#atm loop
exit = False
while not exit:
    print('To Check Your Balance || press 1: ')
    print('To Make a Deposit || press 2: ')
    print('To Withdraw press || 3: ')
    print('To exit press || 4: ')
    ask_option = input(' What would you like to do?: ')
    if ask_option == '1':
        print(random_person.check_balance())
        ask_again = input('to continue type YES:  \n to quit type NO: ').lower()
        if ask_again == 'no':
            exit = True
            print('See you next time!')
        else:
            continue
    elif ask_option == '2':
        amount = input('how much would u like to deposit?: ')
        print(random_person.deposit(int(amount)))
        ask_again = input('to continue type YES:  \n to quit type NO: ').lower()
        if ask_again == 'no':
            exit = True
            print('See you next time!')
        else:
            continue
    elif ask_option == '3':
        amount = input('how much would u like to withdraw?: ')
        print(random_person.withdraw(int(amount)))
        ask_again = input('Do u need something else?:  \n to stay type YES:  \n to exit type NO: ').lower()
        if ask_again == 'no':
            exit = True
            print('See you next time!')
        else:
            continue
    elif ask_option == '4':
        exit = True
        print('See you next time!')
    
    else:
        print('WRONG INPUT PLEASE CHOOSE INPUT OPTIONS CAREFULLY!')






    