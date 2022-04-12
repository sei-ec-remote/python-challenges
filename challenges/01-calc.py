# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.


"""
statement = input("give a string")
num = input("give a number")

def p_times(name, number):
    for number in range(int(number)):
        print(f"Hello {name}")
p_times(statement, num)
"""

arithmetic_choice = input("what you like to do? add, subtract, divide, multiply? ")
first_number = input("enter first number: ")
second_number = input("enter second number: ")

def calculate(first_number,second_number):
    #if arithmetic_choice != "add" or arithmetic_choice != "subtract" or arithmetic_choice != "divide" or arithmetic_choice != "multiply":
           # print("please chooce a proper arithmetic operation")
    if arithmetic_choice == "add":
        sum = int(first_number) + int(second_number)
        print(f"{first_number} + {second_number} = {sum}")
    elif arithmetic_choice == "subtract":
        subtraction = int(first_number) - int(second_number)
        print(f"{first_number} - {second_number} = {subtraction}")
    elif arithmetic_choice == "divide":
        division = int(first_number) / int(second_number)
        print(f"{first_number} / {second_number} = {division}")
    elif arithmetic_choice == "multiply":
        multiplication = int(first_number) * int(second_number)
        print(f"{first_number} * {second_number} = {multiplication}")
  

calculate(first_number,second_number)