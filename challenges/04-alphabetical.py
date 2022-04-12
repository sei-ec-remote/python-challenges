# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

input_str = input("Enter any word! \n")

def sort_string(str):
    alphabetized_str = ''.join(sorted(str))
    return alphabetized_str
        

print(sort_string(input_str))