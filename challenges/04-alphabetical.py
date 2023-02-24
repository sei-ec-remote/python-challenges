# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.


def sort_string(string):
    str_list = sorted(string)
    sorted_string = ''.join(str_list)
    return print(sorted_string)

string = input("Give me a string to alphabetize: ")

sort_string(string)