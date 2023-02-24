# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1

# Reverse in line using slicing -(:: starts at then end of the string and adding -1 moves one step back)

# def reverse(str):
#     str = ''
#     for i in str:
#         str = i + str
#     return str

# str = input('Enter a string: ')
# print(str)

# print(reverse(str))


def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

s = input('Enter a String: ')

print(s)

print(reverse(s))
