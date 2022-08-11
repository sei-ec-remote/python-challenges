# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

def calc_python():
 calc_problem = input("What calculation would you like to do? (add, sub, mult, div) ")
 num_one = int(input("What is number 1?\n" ))
 num_two = int(input("What is number 2?\n" ))

 if calc_problem == "add":
    print(num_one + num_two)
 elif(calc_problem == "sub"):
    print(num_one - num_two)
 elif(calc_problem == "multiply"):
    print(num_one * num_two)

 else:
    print(num_one / num_two)
#  count = {
#     "add": num_one + num_two,
#     "sub": num_one - num_two,
#     "multiply": num_one * num_two,
#     "div": num_one / num_two,
#   }


# for i in range(count):
#   print(f"Hello {name}!")
