print("Welcome to Chase bank.")
# Collect the user's starting balance
balance = 4000

# Display the user's current balance
print("Your current balance is")
print(balance)

# Ask the user what they want to do
action = input("What would you like to do? (deposit, withdraw, check_balance)\n")

# Perform the selected action
if action == "deposit":
    amount = float(input("How much would you like to deposit?\n"))
    balance += amount
elif action == "withdraw":
    amount = float(input("How much would you like to withdraw?\n"))
    balance -= amount
elif action == "check_balance":
    pass  # Do nothing
else:
    print("Invalid action. Please try again.")

# Display the user's updated balance
print("Your current balance is")
print(balance)

# Ask the user if they're done
done = input("Are you done?\n")

# Say goodbye
print("Have a nice day!")

