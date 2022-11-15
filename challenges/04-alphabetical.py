# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

def alpha():
    string = input("Give me a string to alphabetize:\n").lower()
    letter_list = list(string)
    letter_list.sort()
    sorted_string = ''.join(letter_list)
    print(f'Alphabetized:\n{sorted_string}')


alpha()
    