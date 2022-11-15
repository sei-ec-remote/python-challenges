print("Welcome to Chase bank.")

# declare balance
balance = 100
# declare answer to question
status = False
#  declare function
def bank():
# globals
    global balance
    global status
#  create a loop 
    while(status != True):
        start_question = input('Would you like to display your balance(balance), withdraw, deposit into your account, or exit?\n')
# if statement
# display balance
        if(start_question == 'balance'):
            print(f'Your balance is {balance}\n')
#  deposit 
        elif(start_question == 'deposit'):
            amount = int(input('What amount would you like to deposit?\n'))
            balance = balance + amount 
            print(f'Your new balance is {balance}\n')
# withdraw 
        elif(start_question == 'withdraw'):
            amount = int(input('What amount would you like to withdraw?\n'))
            balance = balance - amount 
            print(f'Your new balance is {balance}\n')
        elif(start_question == 'exit'):
            status = True
print("Have a nice day!")

bank()



