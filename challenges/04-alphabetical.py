# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

string = input('enter text')

def letters(sting):
    text = ''
    print(text.join(sorted(string)))
letters(string)