#Create a prompt that asks the user if they would like to display their balance, withdraw or deposit

#Write three methods to perform these calculations and output the result to the user

#may need to declare starting variable for the bank account
current_account = 4000
#function for deposit
def deposit_amount(deposit):
    global current_account
    current_account += deposit
    #deposit = int(input('How much would you like to deposit?\n'))
    print(f"Your account after your deposit is: {current_account}")
def withdrawal_amount(withdrawal):
    global current_account
    current_account -= withdrawal
    #withdrawal = int(input('How much would you like to withdrawal?\n'))
    print(f"After your withdrawal, your account balance is: {current_account}")
def check_balance():
    print(f"Your current account balance is: {current_account}")
new_account = ''
#while loop to account for a user being done or not... set to false until the user states true
# def user_done():
#     user_done = False
#     print('See you later!')
user_done = True

while user_done:
    user_choice = input('What would you like to do? (deposit, withdraw, check_balance, done)\n')
#if statement...
    if user_choice == 'done':
        print('See you later!')
        user_done = False
    elif user_choice == 'deposit':
        deposit = int(input('How much would you like to deposit?\n'))
        deposit_amount(deposit)
    elif user_choice == 'withdraw':
        withdrawal = int(input('How much would you like to withdrawal?\n'))
        withdrawal_amount(withdrawal)
    elif user_choice == 'check_balance':
        current_account
        print(f"Your current balance is: {current_account}")


   