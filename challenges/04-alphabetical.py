# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.
def sortString(str):
    calc_problem = input("Give me a string to alphabetize?\n")
    return ''.join(sorted(str))

str = ''
print("Alphabetized:", sortString(str))