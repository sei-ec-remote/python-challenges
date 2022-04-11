# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.


string = input('Enter a Word: ')

string_tolist = list(string)
string_tolist = sorted(string_tolist)
alphabet_string = ''.join(string_tolist)
print(alphabet_string)
