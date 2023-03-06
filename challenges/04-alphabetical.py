# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

input = input('String to alphabetize? ') # supercalifragilisticexpialidocious
list = list(input)
list.sort()
sorted = ''.join(list)

print(f'Sorted: {sorted}')