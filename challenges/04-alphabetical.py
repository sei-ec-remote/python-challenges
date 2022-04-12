# You'll need to use a couple of built in functions to alphabetize a string.
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.
from pickletools import stringnl


input_string = input("Enter any word! \n")

def sort_string(string):
    alphabetized_string = ''.join(sorted(string))
    return alphabetized_string


print(sort_string(input_string))
