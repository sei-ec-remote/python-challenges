# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1

def reverse_string(word):
    word_reversed = ''
    for character in word:
        word_reversed = character + word_reversed
    
    print("Here is your original word: ", word)
    print("Here is the reversed word: ", word_reversed)

reverse_string(input('What word would you like to reverse today? '))