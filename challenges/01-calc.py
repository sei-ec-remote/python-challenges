# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

calc = input ("what calculation would you like to do (add, sub, mult or div?: ")
num1 = int(input ("what is number 1: "))
num2 = int(input ("what is number 2: "))

if calc == 'add':
    result = num1 + num2
elif calc == 'sub':
    result =  num1 - num2
elif calc == 'mult':
    result = num1 * num2
elif calc == 'div':
    result = num1 / num2

print(f"the result of {num1} and {num2} is {result}")
