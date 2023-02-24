# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

some_str = 'supercalifragilisticexpialidocious'
list_str = list(some_str)
# print(list_str)
list_str.sort()
# print(list_str)
alphabet_str = ''.join(list_str)
print(alphabet_str)