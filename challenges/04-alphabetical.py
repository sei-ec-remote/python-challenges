# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

def alphabetize():
    string = input("Enter a string. \n")
    str_list = sorted(string)
    alphabetized_string = ''.join(str_list)

    print("{} in alphabetical order is {}.".format(string, alphabetized_string))

alphabetize()