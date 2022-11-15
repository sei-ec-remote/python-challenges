### Challenge 2 - Reverse a string
# Reverse a string manually. Don't use s[::-1] (even though that's awesome).
# Create a new variable storing an empty string and add the letters from
# the first string one by one. The for loop should iterate over the length
# of the string and you should access letters individually.

# Below is some sample output.

# ```
# Enter a string:
# reverse_me
# em_esrever

def reverse_string(str):
	r_string = ""
	for letter in reversed(str):
		r_string += letter
	print(r_string)

reverse_string("This is the string in reverse")