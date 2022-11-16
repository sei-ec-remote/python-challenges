# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

def to_alphabetize(string):
    #creating list
    list_str = list(string)
    #sorting this list
    list_str.sort()
    #after sort method, join list back to string in a sorted way
    sorted_string = ''.join(list_str)
    #printing alphabetized string and removing empty spaces
    print(sorted_string.replace(' ',''))

word = input('what word do you want to be alphabetized?: ')
#word = ' some random word'
to_alphabetize(word)