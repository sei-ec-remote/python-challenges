# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.
def alphabet(string):
    new_string = list(string)
    empty_string = []
    for i in new_string:
        empty_string.append(i)
    empty_string.sort() 
    print(''.join(empty_string))

alphabet('reverse')