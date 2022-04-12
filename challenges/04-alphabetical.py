# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.


#  Sort the string into list of letters ascending then join them together
# [ 'a', 'a', 'b' ...]
#  Must make a new string
def alphabetize_string(str):
    return ''.join(sorted(str))

# Ask the user for a string to alphabetize
choice = input("Give me a string to alphabetize \n")

print(alphabetize_string(choice))

