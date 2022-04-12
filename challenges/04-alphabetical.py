# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

def sort(string):
    string_list = list(string)
    sorted_list = sorted(string_list)
    sorted_string = "".join(sorted_list)
    print(f"Alphabetized: {sorted_string}")

string = input('Give me a string to alphabetize \n')

sort(string) 