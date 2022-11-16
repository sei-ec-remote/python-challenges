# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

my_str = "chicken tenders"
def alphabetize(str):
    list = [char for char in str]
    list.sort()
    sorted_str = "".join(list)
    return print(sorted_str)

alphabetize(my_str)
