# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.


# Give me a string to alphabetize
# supercalifragilisticexpialidocious
string = input('Enter a string to alphebatize')

# Alphabetized: aaacccdeefgiiiiiiillloopprrssstuux
def alphabetized_string(string):
    return ''.join(sorted(string))

print(alphabetized_string(string))
