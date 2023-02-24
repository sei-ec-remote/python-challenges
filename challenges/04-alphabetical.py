# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

def alphabetize(string):
    letters_list = []
    alpha_string = ''
    for letters in string:
        letters_list.append(letters)
    letters_list.sort()
    for item in letters_list:
        alpha_string += item
    print(alpha_string)


alphabetize('jgoidjgjsaewhdaggreg')