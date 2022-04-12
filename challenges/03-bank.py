# Challenge 3 - Bank Transactions
# Create a prompt that asks the user if they would like to display their 
# balance, withdraw or deposit. Write three methods to perform these
#  calculations and output the result to the user.

# Gather user input using the input function. Note that input always returns
#  user input as a string. You have to manually convert it to an int or a 
# float to make it behave like number. Also, end the input prompt with a 
# \n newline character if you want the user to type in on the next line.

balance = 0
transacting = True

# prompts user if they want to close the transaction
def are_you_done():
    done = input("Are you done? (yes/no)")
    if(done == 'yes'):
        global transacting
        transacting = False
        return print("Thank you, have a great day!")
     
while transacting:
    transaction  = input('What would you like to do? (deposit, withdraw, check_balance)')
    if(transaction == 'deposit'):
        deposit_amount = input('How much would you like to deposit?')
        balance += int(deposit_amount)
        are_you_done()
    elif(transaction == 'withdraw'):
        withdraw_amount = input('How much would you like to withdrawal?')
        balance -= int(withdraw_amount)
        are_you_done()
    elif(transaction == 'check_balance'):
        print(f'Your current balance is {balance}')
        are_you_done()
    else: 
        print ('you did not choose from one of the following.. resetting to original prompt..')