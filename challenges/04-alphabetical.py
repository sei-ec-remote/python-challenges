# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

# What we will need. ABC in order, and empty new string for the answer.
abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
new_str = ''

# Get the string from the user.
str = input('Enter a string: ')

# Go through are ABC and for each letter we will go through the whole string the user gave use and add the letter that matches to are new string.

# for letter in abc:
#      for x in str:
#           if letter == x:
#                new_str += x

# for letter in abc:
#      new_str = [character for character in str if letter == character]
# I wrote it and it still makes my head spin!

for letter in abc:
     new_str = [character for letter in abc for character in str if letter == character]
# head still spinning.

# Give the user the answer.
print(new_str)