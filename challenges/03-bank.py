print("Welcome to Chase bank.")

balance = 15000

user_response = input("What would you like to do? (Display My Balance; Deposit; Withdraw\n")

if user_response == "Display My Balance":
    print(f"Your current balance is {(balance)}.")
if user_response == "Withdraw":
    withdraw = input("Enter the amount you would like to withdraw.\n")
    balance = balance - int(withdraw)
    print(f"Your current balance after withdraw is {(balance)}.")
if user_response == "Deposit":
    deposit = input("Enter the amount you would like to deposit.\n")
    balance = balance + int(deposit)
    print(f"Your current balance after deposit is {(balance)}.")

print("Have a nice day!")
# elif calc == "sub":
#     print(f"Your result is {int(num_one) - int(num_two)}")
# elif calc == "mult":
#     print(f"Your result is {int(num_one) * int(num_two)}")
# elif calc == "div":
#     print(f"Your result is {int(num_one) / int(num_two)}")

# num_one = input("What is number 1?")
# num_two = input("What is number 2?")