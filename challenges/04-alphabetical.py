# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.


# alphabetize a string
# Create a function that takes a string and returns the string with the letters in alphabetical order (ie. hello becomes ehllo), Assume numbers and punctuation symbols will not be included in the string.


# words = input('youll never get out of this maze')
# my_list = list(words)
# my_list.sort()
# alphabet = ''.join(my_list)
# print(alphabet)


# def alphabetize(string):
#     string = list(string)
#     string.sort()
#     return "".join(string)

# abc_string= input("youll never get out of this maze")

# print(alphabetize(abc_string))

    # input('youll never get out of this maze')
    # string.split()


def sortString(str):
    return ''.join(sorted(str))
     
str = 'shablam'
print(sortString(str))