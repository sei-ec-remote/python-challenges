# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

def order_string(string):
    print(sorted(string))

order_string('PYTHON')
# Orders it like [' ', '!', 'H', 'W', 'd', 'e', 'l', 'l', 'l', 'o', 'o', 'r']
# I couldn't find a way to lowercase it.
order_string('Hello World!')