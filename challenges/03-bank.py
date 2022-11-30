
balance = int(input('Enter your starting balance: \n'))

print("Welcome to PNC Bank!")

def going_to_bank():
    services = input('How may we help you today? (Deposit, Withdraw, Check Balance) \n')
    if (services == 'Deposit' or services == 'deposit'):
        deposit_amount = int(input('How much would you like to deposit today? \n'))
        print(f"You have deposited ${deposit_amount}. Your new balance is ${deposit_amount+balance}")
        anything_else = input("Is there anything else you would like to do today? (Yes or No) \n")
        if (anything_else == 'Yes' or anything_else == 'yes'):
            going_to_bank()
        elif (anything_else == 'No' or anything_else == 'no'):
            print('Have a great day!')
        else:
            print("Hmm, I didn't understand that. Goodbye!")
    elif (services == 'Withdraw' or services == 'withdraw'):
        withdraw_amount = int(input('How much would you like to withdraw today? '))
        print(f"You have withdrawn ${withdraw_amount}. You have ${balance-withdraw_amount} left in your account.")
        anything_else = input("Is there anything else you would like to do today? (Yes or No) \n")
        if (anything_else == 'Yes' or anything_else == 'yes'):
            going_to_bank()
        elif (anything_else == 'No' or anything_else == 'no'):
            print('Have a great day!')
        else:
            print("Hmm, I didn't understand that. Goodbye!")
    elif (services == 'Check Balance' or services == 'check balance'):
        print(f"You have ${balance} in your account")
        anything_else = input("Is there anything else you would like to do today? (Yes or No) \n")
        if (anything_else == 'Yes' or anything_else == 'yes'):
            going_to_bank()
        elif (anything_else == 'No' or anything_else == 'no'):
            print('Have a great day!')
        else:
            print("Hmm, I didn't understand that. Goodbye!")
    else:
        print("Sorry, I didn't catch that.")
        going_to_bank()

going_to_bank()