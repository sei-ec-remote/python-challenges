# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

str = input('enter string')
split_str = list(str)
split_str.sort()
sorted_list = ''.join(split_str)

print(sorted_list) 