# ### Challenge 1 - Calculator

# Create a simple calculator that first asks the user what method they would like
def calculator():
	question = input("What would you like to do?\n 1. add 2. subtract. 3. multiply. 4. divide \nSelect the number of the operation you want. ")
	num1 = input("What is number 1? ")
	num2 = input("What is number 2? ")

	if(question == "1"):
		print(f"Your sum is:", int(num1) + int(num2))
	elif(question == "2"):
		print(f"Your difference is:",int(num1) - int(num2))
	elif(question == "3"):
		print(f"Your product is:", int(num1) * int(num2))
	elif(question == "4"):
		print(f"Your quotient is:", int(num1)/int(num2))

calculator()

# to use (addition, subtraction, multiplication, division) and then asks the user
# for two numbers, returning the result of the method with the two numbers. Here
# is a sample prompt:

# ```
# What calculation would you like to do? (add, sub, mult, div)
# add
# What is number 1?
# 3
# What is number 2?
# 6
# Your result is 9




