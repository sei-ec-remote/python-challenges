# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

invalid_operation = True
operations = {"add", "sub", "mult", "div"}

while invalid_operation:
    operation = input("What calculation would you like to do? (add, sub, mult, div) ")
    if operation in operations:
        invalid_operation = False
    else:
        print("Invalid Operation")
        print()

def get_valid_number(num):
    while True:
        try:
            operand = float(input(f'What is number {num}?'))
        except ValueError:
            print("Please enter a number")
            continue
        else:
            break
    return operand

def calculate(first, second, operation):
    if operation == 'add':
        return first + second
    elif operation == 'sub':
        return first - second
    elif operation == 'mult':
        return first * second
    elif operation == 'div':
        if second == 0:
            return ('cannot divide by 0')
        else:
            return first / second
    else:
        return "Sorry, something went wrong"

first_num = get_valid_number(1)
second_num = get_valid_number(2)
print(f"Your result is {calculate(first_num,second_num,operation)}")

