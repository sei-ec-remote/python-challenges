# print("Welcome to Chase bank.")
# print("Have a nice day!")

# ### Challenge 3 - Bank Transactions
# Create a prompt that asks the user if they would like to display their balance,
# withdraw or deposit. Write three methods to perform these calculations and
# output the result to the user.
continue_ = 'yes'

while continue_ == 'yes':

    balance = 0

    # def add_Balance(e):
    #     num = e
    #     print('add', num)

    def sub_Balance(num):
        # num = e.target
        print('sub', num)

# /////////////////////////////////////////////

    prompt = input(f'Your balance is ${balance} What would you like to do? (deposit, withdraw, check balance)\n')

    if prompt == 'check balance':
        print(f'Your current balance is ${balance}')
    elif prompt == 'withdraw':
        question_withdraw = input('How much would you like to withdraw?')
        print('withdraw', question_withdraw)
        balance = balance - int(question_withdraw)
        print('balance', balance)
    elif prompt == 'deposit':
        question_deposit = input('How much would you like to deposit?')
        print('deposit', question_deposit)
        balance = balance + int(question_deposit)
        print('balance', balance)

    question_done = input('Are  you done?')

    if question_done == 'yes':
        continue_ = 'no'
        print('Thank you!')



# Your current balance is 5000

# Gather user input using the `input` function. Note that input always returns
# user input as a string. You have to manually convert it to an int or a float
# to make it behave like number. Also, end the input prompt with a \n newline
# character if you want the user to type in on the next line.

# ```
# age = input("How old are you?\n")
# age = int(age)
# ```

# Here is a sample output:

# ```
# Your current balance is
# 4000
# What would you like to do? (deposit, withdraw, check_balance)
# deposit
# How much would you like to deposit?
# 1000
# Your current balance is 5000
# Are you done?
# yes
# Thank you!
# ```