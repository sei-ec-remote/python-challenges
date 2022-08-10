# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

def alphabetize(string):
    string_to_alphabetize = list(string.lower())
    string_to_alphabetize.sort()
    print(''.join(string_to_alphabetize))

alphabetize("helloworld")
alphabetize("supercalifragilisticexpialidocious")