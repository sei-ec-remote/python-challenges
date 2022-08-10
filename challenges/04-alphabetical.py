# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.
def sort():
    mystr = input("give me a string to alphabetize: \n")
    myli = list(mystr)
    myli.sort()
    print(''.join(myli))

sort()