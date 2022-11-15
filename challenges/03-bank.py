# ### Challenge 3 - Bank Transactions
# Create a prompt that asks the user if they would like to display their balance,
# withdraw or deposit. Write three methods to perform these calculations and
# output the result to the user.

# Gather user input using the `input` function. Note that input always returns
# user input as a string. You have to manually convert it to an int or a float
# to make it behave like number. Also, end the input prompt with a \n newline
# character if you want the user to type in on the next line.
class BankAccount:
	def __init__(self, balance = 0):
		self.balance = balance
		self.interest = .02

	def __str__(self):
		return f'balance: {self.balance}'

	def deposit(self, amount):
		if(amount < 0):
			return False
		else:
			self.balance += amount

	def withdraw(self, amount):
		if(amount < 0):
			return False
		else:
			self.balance -= amount

	def atm(self):
		print(f"Your balance is: {self.balance} ")
		question = input("What would you like to do? (deposit, withdraw, check_balance)")
		if(question == "deposit"):
			amount = input("How much would you like to deposit?")
			self.deposit(int(amount))
			print(self.__str__())
			done = input("Are you done? ")
			if(done == "yes"):
				print("Thank you! Have a great day")
			elif(done == "no"):
				self.atm()
		elif(question == "withdraw"):
			amount = input("How much would you like to withdraw?")
			self.withdraw(int(amount))
			print(self.__str__())
			done = input("Are you done? ")
			if(done == "yes"):
				print("Thank you! Have a great day")
			else:
				self.atm()
		elif(question == "check_balance"):
			print(self.__str__())
			done = input("Are you done? ")
			if(done == "yes"):
				print("Thank you! Have a great day")
			elif(done == "no"):
				self.atm()
			

user_account = BankAccount(10000)

user_account.atm()


# Here is a sample output:

# ```
# Your current balance is
# 4000
# What would you like to do? (deposit, withdraw, check_balance)
# deposit
# How much would you like to deposit?
# 1000
# Your current balance is 5000
# Are you done?
# yes
# Thank you!
# ```
