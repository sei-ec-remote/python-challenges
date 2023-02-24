# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

def alphabetize_string(string):
    return ''.join(sorted(string))

user_string = input("Give me a string to alphabetize\n")
alphabetized_string = alphabetize_string(user_string)
print("Alphabetized:", alphabetized_string)
