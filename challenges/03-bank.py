print("Welcome to Chase bank.")

balance = int(input("Your current balance is:\n"))

action = input("What would you like to do? (deposit, withdraw, check_balance)\n")

if action == "check_balance":
    print("Your current balance is:\n{balance}")
    done = input("Are you done?\n")
    if done == "no":
        balance
    else:
        print("Thank you!")
# how_much = int(input("What is the second number?\n"))

# if calc == 'add':
#     print(first_number + second_number)
# elif calc == 'sub':
#     print(first_number - second_number)
# elif calc == 'mult':
#     print(first_number * second_number)
# elif calc == 'div':
#     print(first_number / second_number)

print("Have a nice day!")

