
global balance
global done
balance = 6500
done = "no"

def bank():
    
    print('Welcome to Chase bank.')
while (done != "yes"):
    ans = input('What would you like to do?\n')

    if (ans == 'deposit'):
      amount = int(input('How much would you like to deposit?\n'))
      balance = balance + amount
      print(f'Your current balance is {balance}\n')
      done = input('Are you done?\n')
    elif (ans == 'withdraw'):
      amount = int(input('How much would you like to withdraw?\n'))
      balance = balance - amount
      print(f'Your current balance is {balance}\n')
      done = input('Are you done?\n')
    elif (ans == 'balance'):
      print(f'Your current balance is {balance}\n')
      done = input('Are you done?\n')
    if(done == 'yes'):
        print('Have a nice day!')
    else:
        print('Welcome to chase')  
bank()