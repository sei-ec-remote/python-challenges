# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

string = input('Enter a string:\n')

def alphabetize(string):
    # new_list = list(string)
    # new_list.sort()

    new_string = ''
    # for letter in string:
        # new_string + new_string + letter
    print(new_string.join(sorted(string)))

alphabetize(string)