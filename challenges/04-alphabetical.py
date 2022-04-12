# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.


# Challenge 4 - Sort a String
# Create a function that takes a string and returns the string with the
#  letters in alphabetical order (ie. hello becomes ehllo), Assume numbers 
# and punctuation symbols will not be included in the string.

def alphabetize(some_string):
    new_array =[]
    for current_char in some_string:
        if (len(new_array) == 0):
            new_array.append(current_char)
        else:
            for char in new_array:
                if(ord(current_char) <= ord(char)):
                     new_array.insert(new_array.index(char), current_char)
                     break
                elif(new_array.index(char) == (len(new_array) - 1)):
                    new_array.append(current_char)
    print("".join(new_array))
    
alphabetize('supercalifragilisticexpialidocious')
