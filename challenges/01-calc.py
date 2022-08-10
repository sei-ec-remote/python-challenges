# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.
import operator

def calculator(): 
    ops = { "+": operator.add,
            "-": operator.sub, 
            "x": operator.mul,
            "%": operator.truediv}
    stringops = ",".join(ops.keys())
    oper = input(f"What caluclation would you like to do?({stringops})\n")
    numb1 = int(input("What is number 1? \n"))
    numb2 = int(input("What is number 2? \n"))
    print(f"Your result is {ops[oper](numb1, numb2)}")

calculator()