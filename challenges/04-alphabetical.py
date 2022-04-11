# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

from hashlib import new
from ntpath import join
from posixpath import split


def alphabetize(string):
    new_list = []
    for char in string:
        new_list.append(char)
    ordered_list = sorted(new_list)
    print(''.join(ordered_list))

user_string = input("Give me a string to alphabetize\n")

alphabetize(user_string)