# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.
calculator = input("what calculation would you like to do? (add, sub, mult, divide)")

first_num = input("Whats is the first number?")

second_num =input("whats is the second number?")

if calculator == 'sub' or calculator =='SUB':
    print(f"the sum is {int(first_num) - int(second_num)}")
if calculator == 'add' or calculator =='ADD':
    print(f'The Difference is {int(first_num) + int(second_num)}')
if calculator == "mult" or calculator =="MULT":
    print (f'The product is {int(first_num) * int(second_num)} ')
if calculator == "divide" or calculator =="DIVIDE":
    print(int(first_num)/ int(second_num))