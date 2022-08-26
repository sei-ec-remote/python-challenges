# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

def alphabetical_order(string):
    letters = sorted(string)
    corrected = "".join(letters)
    return print(f"alphabetized string: {corrected}")

string_to_alphabetize = input("Enter string.\n")
alphabetical_order(string_to_alphabetize) 