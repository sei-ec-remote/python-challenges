# You'll need to use a couple of built in functions to alphabetize a string.
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

# ask for an input
str = input('Give me a string to alphabetize: ')
# sort the string in alphabetical
sort = sorted(str)
# sorted in Python returns a list
# join list items into an empty string
join_str = ''.join(sort)
# return the string to console
print(join_str)
