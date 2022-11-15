# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1

# define the function
def reverse(string):
# define string
# loop over string
    string = [string[i] for i in range(len(string) -1, -1, -1)]
#  return string
    return ''.join(string)
# define the string to be reveresd
sample ="reverse_me"
# print the orignal string
print('original string is : ', sample)
#  print the reversed string
print('the reversed string is : ', reverse(sample))