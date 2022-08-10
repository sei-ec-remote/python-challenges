# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.
def alphabatize_me(string):
    string = list(string)
    string.sort()
    return "".join(string)

ask_for_string = input('Give me some letters or words to alphabetize! ')

print(alphabatize_me(ask_for_string))