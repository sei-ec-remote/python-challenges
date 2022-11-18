balance = float(20)

print("Welcome to Chase bank.")
print("Your availble balance is", balance)
operator = input("Deposit or withdraw? ")
if operator == 'deposit' or operator == 'Deposit':
    amount = float(input("How big is your deposit?   "))
    print('New Balance: ', balance + amount)
elif operator == 'withdraw' or operator == 'Withdraw':
    amount = float(input("How much would you like to withdraw? "))
    print("New Balance: ", balance - amount)

print("Have a nice day!")

