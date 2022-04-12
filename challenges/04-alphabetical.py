# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

def alphabet():
    string = input("enter a word or phrase to alphebatize:")
    alphabet_string = sorted(string)
    alphabet_string = ''.join(alphabet_string)
    print(alphabet_string)
alphabet()