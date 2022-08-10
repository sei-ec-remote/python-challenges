# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

# Give me a string to alphabetize
# supercalifragilisticexpialidocious
# Alphabetized: aaacccdeefgiiiiiiillloopprrssstuux

def alphabetize(string):
    str_list = list(string)
    str_list.sort()
    print("".join(str_list))

alphabetize('supercalifragilisticexpialidocious')
alphabetize('Alphabetizecompleted')
