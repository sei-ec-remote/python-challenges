# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.
str = input("Alphabetize me, boss: ")
str_list = list(str)
str_list.sort()
az_str = ''.join(str_list)
print(az_str)
