# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.


# Python3 program to sort letters
# of string alphabetically
 
def sortString(str):
    return ''.join(sorted(str))
     
# Driver code
str = 'PYTHON'
print(sortString(str))