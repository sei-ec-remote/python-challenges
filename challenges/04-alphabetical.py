# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

my_string = input("Give me a string to alphabetize:\n   ")
my_string_list = list(my_string)
my_string_list.sort()
my_string_sorted = "".join(my_string_list)
print(f"Your alphabetized string is {my_string_sorted}.")