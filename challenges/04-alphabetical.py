# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

print('Please enter a string')
string = input()

str_as_list = []
str_as_list[:0] = string

str_as_list.sort()

while (' ' in str_as_list):
    str_as_list.remove(' ')

str_alpha = ''.join(str_as_list)

print('Here is the alphabetized string:', str_alpha)