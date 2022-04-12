# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

str = input('enter string')
new_list = list(str)
new_list.sort()
join_str = ''.join(new_list)

print(join_str) 