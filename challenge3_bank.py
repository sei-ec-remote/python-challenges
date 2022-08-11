done = False
total = 0
while not done:
    action = input('What would you like to do?(deposit, withdraw, check_balance)\n')


    if action == 'deposit':
        deposit = int(input('How much would you like to deposit\n'))
        total+=deposit
        print('Your current balance is', total)
    elif action == 'withdraw':
        withdrawal = int(input('How much would you like to withdraw\n'))
        total-=withdrawal
        print('Your current balance is', total)
    else:
        print('Your current balance is', total)
    
    areyoudone = input('Are you done?(yes or no)\n')
    if areyoudone == 'yes':
        done = True
        print('Thank you!')
