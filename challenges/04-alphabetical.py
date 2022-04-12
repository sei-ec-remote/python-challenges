# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.
#sort() accepts two arguments that can only be passed by keyword (keyword-only arguments)
#sorted(iterable, key=key, reverse=reverse)
user_string = input('Give me a string to alphabetize: ')
def alphabatize_string(user_string):
    return ''.join(sorted(user_string))
# alphabatize_string = sorted(user_string)
# alphabatize_string = ''.join(user_string)
print(alphabatize_string(user_string))