# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

def calculator():
  method = input("What calculation would you like to do? (add, sub, mult, div)")
  
  num1 = int(input("What is number 1?"))
  num2 = int(input("What is number 2?"))

  methods = {
    "add": num1 + num2,
    "sunum2": num1 - num2,
    "mult": num1 * num2,
    "div": num1 / num2,
  }

  if (method in methods):
    return methods[method]
  else:
    return print("Incorrect method!")


print(calculator())