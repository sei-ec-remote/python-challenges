# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

def alphabetize():
    word = input("\n Generate a string to alphabetize: \n")
    character_array = list(word)
    character_array.sort()
    sorted_word = "".join(character_array)
    print("\n Here is", word, "alphabetized: \n", sorted_word)

alphabetize()
