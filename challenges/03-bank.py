"""
Create a prompt that asks the user if they would like to display 
their balance, withdraw or deposit. Write three methods to perform 
these calculations and output the result to the user.

Gather user input using the input function. Note that input always
 returns user input as a string. You have to manually convert it to an 
 int or a float to make it behave like number. Also, end the input prompt
  with a \n newline character if you want the user to type in on the next line.

age = input("How old are you?\n")
age = int(age)
Here is a sample output:

Your current balance is
4000
What would you like to do? (deposit, withdraw, check_balance)
deposit
How much would you like to deposit?
1000
Your current balance is 5000
Are you done?
yes
Thank you!
"""

"""


print("Welcome to Chase bank.")

age = input("How old are you? ")
age = int(age)

def current_balance(age):
   
    if age < 30:
        balance = 3000
        print(f"Your current balance is {balance}")

    elif age < 60:
        balance = 5000
        print(f"Your current balance is {balance}")
    else: 
        balance = 8000
        print(f"Your current balance is {balance}")

current_balance(age)

banking_purpose = input("What would you like to do? ")

def banking_transaction(banking_purpose):
    if banking_purpose == "deposit":
        deposit_amount = input("How much would you like to deposit? ")
        def deposit_money(deposit_amount):
            if age < 30:
                 balance = 3000
                 print(f"your current balance is {balance}+{deposit_amount}")
        deposit_money(deposit_amount)
banking_transaction(banking_purpose)


checkout_question = input("Are you done? ")

def checkout(checkout_question):
    if checkout_question == "yes":
        print("Thank you! Have a nice day!")
checkout(checkout_question)

"""

def bank_transaction():
    print("Welcome to Chase bank.")

    current_balance = 4000
    print(f"Your balance: {current_balance}")
    banking_purpose = input("What would you like to do (deposit, withdrawal, check balance? ")

    if banking_purpose == "deposit":
        deposit_amount = input("How much would you like to deposit? ")
        current_balance += int(deposit_amount)
        print(f"You're balance: {current_balance}")

    elif banking_purpose == "withdrawal":
        withdrawal_amount = input("How much would you like to withdraw?")
        current_balance -= int(withdrawal_amount)
        print(f"You're new balance: {current_balance}")
    elif banking_purpose == "check balance":
        print(f"Your balance: {current_balance}")
    checkout_question = input("Are you done? ")
    if checkout_question == "yes":
        print("Thank you! Have a nice day!")

bank_transaction()





#def bank_visit(banking_purpose, deposit_amount, withdrawal_amount, checkout_question):
   
    
    
   
    #print(bank_visit(current_balance, banking_purpose, deposit_amount, withdrawal_amount, checkout_question))

