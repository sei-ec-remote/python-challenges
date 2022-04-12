# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

string = input("Enter some text:")
def alpha_letters (string):
    text = ""
    print(text.join(sorted(string)))
alpha_letters(string)
