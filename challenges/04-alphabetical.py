# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.


def alphabetize_str (str):
    str_list = []
    for x in range(len(str)):
        str_list.append(str[x])
    str_list.sort()
    return "".join(str_list)


print (alphabetize_str("supercalifragilisticexpialidocious"))