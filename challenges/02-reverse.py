# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1

# Start things off.
print('Enter a string so it can be reversed!')
string = input()

# Get verything we need.
length = len(string)
rev_s = ''

# Go through the string in verse order and add char one by one.
for i in range(length):
     rev_s = rev_s + string[length - (i+1)]
print(rev_s)