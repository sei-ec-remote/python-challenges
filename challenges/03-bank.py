print("Welcome to Chase bank.")
# print('Would you like to display your balance, withdraw or deposit?')
# input = '2'
balance = 4000
do = ''

while do != 'e':
     print('Would you like to display your balance, withdraw or deposit?')
     print(' Enter 1: To see your balance. \n Enter 2: To withdraw \n Enter 3: To deposit \n Press e to exit.')
     do = input()

     if do == '1':
          print(f"\nYour current balance is {balance}\n")
     elif do == '2':
          withdraw = float(input("How much would you like to withdraw?\n"))
          balance -= withdraw
          print(f"\nYour current balance is {balance}\n")
     elif do == '3':
          deposit = float(input('How much would you like to deposit?\n'))
          balance += deposit
          print(f"\nYour current balance is {balance}el\n")

print("Have a nice day!")

