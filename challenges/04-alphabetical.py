# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

# Challenge 4 - Sort a String
# Create a function that takes a string and returns the string with the letters in alphabetical order (ie. hello becomes ehllo), Assume numbers and punctuation symbols will not be included in the string.

# Give me a string to alphabetize
# supercalifragilisticexpialidocious
# Alphabetized: aaacccdeefgiiiiiiillloopprrssstuux

def alphabetize_string(string):
    alpha_list=list(string)
    alpha_list.sort()
    print("".join(alpha_list))
    # print(alpha_str)

alphabetize_string("pikachu")

alphabetize_string("supercalifragilisticexpialidocious")