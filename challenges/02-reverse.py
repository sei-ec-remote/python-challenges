# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1

#Create a new variable storing an empty string and add the letters from the first string one by one
#The for loop should iterate over the length of the string and you should access letters individually
#then the letters need to be joined
# built in function reverse()
def reverse(string):
    reverse_string = ''
    for letter in string:
        reverse_string = letter + reverse_string
    return reverse_string
input_string = 'goodbye'

print(reverse(input_string))

#Also found this: list.sort() accepts an another argument reverse. By default its value is False, 
# but if its set to True then it will sort the list in reverse order.