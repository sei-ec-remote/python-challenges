# print("Welcome to Chase bank.")
# print("Have a nice day!")

# balance = 5000

# question = "no"
# while question == "no":
#     print("Your balance is")
#     method = input("What would you like to do? (deposit, withdraw, check_balance)\n")
#     deposit = input("How much would you like to deposit?\n")
#     method = "deposit"
#     if method == "deposit":
#         print("Your current balance is ", int(balance) + int(deposit))
    

#         question = input("Are you done?\n")

# greeting = input("Thank you!")

print("Welcome to YoooBank!")
balance = 5000
over = "no"

while over == "no":
    print(f"Your balance is ${balance}")
    action = input("What would you like to do? (deposit, withdraw, check_balance)\n")
    if action == "deposit":
        deposit_amount = input("How much would you like to deposit?\n")
        balance = balance + int(deposit_amount)
        print(f"Your current balance is ${int(balance)}")
        over = input("Are you done? (yes or no)\n")
    if action == "withdraw":
        withdraw_amount = input("How much would you like to withdraw?\n")
        if int(withdraw_amount) > int(balance):
            print("Insufficient fund!")
            over = input("Are you done? (yes or no)\n")
        else:
            balance = balance - int(withdraw_amount)
            print(f"Your current balance is ${int(balance)}")
            over = input("Are you done? (yes or no)\n")
    if action == "check_balance":
        print(f"Your current balance is ${balance}")
        over = input("Are you done? (yes or no)\n")

print("Thank you! Go get dat MONEY!!!")









