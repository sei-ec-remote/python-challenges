# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.
print("calculator choose and option below:")
print("1. add")
print("2. subtract")
print("3. multiply")
print("4. divide") 

operation = input()

if operation == "1":
    num1 = input('enter first number ')
    num2 = input('enter second number ')
    print( "the sum is " + str(int(num1) + int(num2)))
    # add
elif operation == "2":
    num1= input('enter first number ')
    num2= input('enter second number ')
    print( "the difference is " + str(int(num1) - int(num2)))
    # subtract
elif operation == "3":
    num1= input('enter first number ')
    num2= input('enter second number ')
    print( "the product is " + str(int(num1) * int(num2)))
    #multiply
elif operation == "4":
    num1= input('enter first number ')
    num2= input('enter second number ')
    print( "the result is " + str(int(num1) / int(num2)))
     # divide
else:
    print("invalid entry")
# number1 = input(int)
# number2 = input(int)
