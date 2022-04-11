# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1


# Reverse a string using a For loop and a new string.
#

choice = input("Input a string: \n")

# Setup holding the output reverse string
reverse_string = ''

# Start at length of choice, go to 0 index, -1 
#   reverse_string is the previous reverse_string plus
#     the choice[i-1] as i starts at length and index is always
#     1 less.   So reverse_string starts with last letter
#   reverse_string = reverse_string + choice[i -1]
for i in range(len(choice), 0, -1):
   reverse_string += choice[i-1]
print (reverse_string)
