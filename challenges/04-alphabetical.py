# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

string = input('Give me a string to alphabetize\n')

def order(string):
    array = list(string)
    array.sort()
    print("Alphabetized:",("".join(array)))

order(string)