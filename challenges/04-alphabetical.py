# Create a function that takes a string and returns the string with the letters in 
# alphabetical order (ie. `hello` becomes `ehllo`), Assume numbers and punctuation 
# symbols will not be included in the string.

# ```
# Give me a string to alphabetize
# supercalifragilisticexpialidocious
# Alphabetized: aaacccdeefgiiiiiiillloopprrssstuux

def alphabetize(str):
	return ''.join(sorted(str))


print(alphabetize("supercalifragilisticexpialidocious"))