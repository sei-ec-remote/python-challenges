# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1



def to_reverse(string):
    reversed = ''
    for i in string:
        reversed = i + reversed
    print(reversed)


#word = 'word to reverse'
word = input('write a word or sentence you want to reverse: ')
to_reverse(word)