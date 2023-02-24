# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1

# Reverse in line using slicing -(:: starts at then end of the string and adding -1 moves one step back)
print('I like to go outside'[::-1])

# Reverse in  a function
def return_reverse(str):
      pass # slice passed in string 
      print(str[::-1])

return_reverse('Reverse that!')


