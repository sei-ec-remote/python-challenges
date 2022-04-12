# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.
def sorting(string):
    split_string = list(string)
    new_list = []
    for char in split_string:
        new_list.append(char)
    new_list.sort()
    print(''.join(new_list))

sorting('turkey')
