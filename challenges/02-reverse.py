# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1


reverse = input("Enter a string:\n")
word = reverse.split()
# print(len(reverse))
reversed_word = []
for letter in reverse:
    # print(letter)
    if len(reversed_word) < len(reverse):
        reversed_word.insert(0, letter)
        # print(sum(reversed_word))
        # print(reversed_word)
        if len(reversed_word) == len(reverse):
            print(''.join(reversed_word))
