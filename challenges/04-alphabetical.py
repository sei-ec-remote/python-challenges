# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

def alphabetize(str):
    new_str = list(str)
    new_str.sort()
    new_str = ''.join(new_str)
    print(new_str)

alphabetize("testinglol")