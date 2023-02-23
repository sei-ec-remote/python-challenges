# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.



def alphabetize():
    stringy=input("\nGive me some letters to sort\n\n")
    order = sorted(stringy)
    together = ''.join(order)
    print("\nBoom:   ",together, "\n\nDon't act like you're not impressed")
alphabetize()