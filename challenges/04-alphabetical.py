# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

def alphabetize(string):
    letter_array = sorted(string)
    alphabetized = "".join(letter_array)
    return print(f"Alphabetized: {alphabetized}")

string_to_alphabetize = input("Give me a string to alphabetize.\n")
alphabetize(string_to_alphabetize)

# print(sorted("idk"))