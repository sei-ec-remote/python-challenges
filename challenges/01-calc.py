# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

calc = input ("What calculation would you like to do? (add, sub, mult, div)")
print(calc)

first_num = input ("What is the first number?")
print(int(first_num))

second_num = input ("What is the second number?")
print(int(second_num))

if calc == 'add': 
    print(f'Your result is {int(first_num) + int(second_num)}')
elif calc == 'sub': 
    print(f'Your result is {int(first_num) - int(second_num)}')
elif calc == 'mult': 
    print(f'Your result is {int(first_num) * int(second_num)}')
elif calc == 'div': 
    print(f'Your result is {int(first_num) / int(second_num)}')