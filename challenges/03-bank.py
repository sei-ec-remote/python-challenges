current_balance = 0
print("Welcome to Isobel bank.")

def continue_or_end(current_balance):
    option = input("Would you like to make another transaction or logout? new_transaction/logout \n")
    
    if option == "new_transaction":
        bank_transaction(current_balance)
    elif option == "logout":
        return
    else: 
        print("Unable to process request. Please try again.")


def bank_transaction(current_balance):
    operation = input("Please enter an option. view_balance/withdraw/deposit \n")

    if operation == "view_balance":
        print("You current balance is $", current_balance)
    elif operation == "withdraw":
        amount = int(input("How much would you like to withdraw? \n"))
        current_balance -= amount
        if current_balance < 0:
            print("You are unable to withdraw ${}. Your current balance is ${}.".format(amount, current_balance))
        else: 
            print("You have withdrawn ${}. You new balance is ${}.".format(amount, current_balance))
    elif operation == "deposit":
        amount = int(input("How much would you like to deposit? \n"))
        current_balance += amount
        print("You have deposited ${}. Your new balance is ${}.".format(amount, current_balance))
    else:
        print("Unable to process request. Please try again.")
    
    continue_or_end(current_balance)

bank_transaction(current_balance)

    
print("Thank you! Have a nice day!")