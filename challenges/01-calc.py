# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.
def calculation(n1, n2, oper):
    num1 = int(n1)
    num2 = int(n2)
    total = None
    if oper == 'add':
        total = num1 + num2
    elif oper == 'sub':
        total = num1  - num2
    elif oper == 'mult':
        total = num1 * num2
    elif oper == 'div':
        total = num1 /  num2
    else:
        return "You did not specify a correct operator. Good-bye."
    return total

input1 = input("What calculation would you like to do? (add, sub, mult, div) ")
input2 = input("What is the first number? ")
input3 = input("What is the second number? ")

print(calculation(input2, input3, input1))