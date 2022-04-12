# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1

# make a function with the parameter of string to refrence later
string = input('enter a string:\n')

def reverse(string):
    # make a new string that is empty
    new_string = ''
    # for each item/letter in the string(parameter)
    for item in string:
        # the new_string is = to the string(parameter) added to the old new_string
        new_string = item + new_string
        # return the new new_string which should be backwards because the first   item in the string(parameter) will be the first input into the new_string adding a new item from right to left
    print(new_string)

reverse(string)
