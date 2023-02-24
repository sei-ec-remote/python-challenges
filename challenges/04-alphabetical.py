# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.
input_str = input("Gimme a crazy string and I will sort it alphabetically for you\n")

def sorter(str):
    sorted_str = sorted(str)
    joined = "".join(sorted_str)
    return joined

print(sorter(input_str))