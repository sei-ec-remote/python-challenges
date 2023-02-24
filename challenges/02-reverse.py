# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1
def revString(str):
    str_list = list(str)
    print(str_list)
    r_str = list(reversed(str_list))
    print(r_str)
    return "".join(r_str)
    # returned_str = ""
    # for letter in range(len(str_list)):
    #     print(str_list[letter])
    #     print(str_list.pop())
    # returned_str.join(r_str)
    # return returned_str

string = input("Input some stuff and I will reverse it for you! ")

# print(string[::-1])
print(revString(string))

# I have no idea how to do this one, not sure why you don't want the answer that works
