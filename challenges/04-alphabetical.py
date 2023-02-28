# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.


def sort_string(input_string):
    
    char_list = list(input_string)

    char_list.sort()

    sorted_string = ''.join(char_list)

    return sorted_string

input_string = "carter is awesome"
sorted_string = sort_string(input_string)
print(sorted_string)