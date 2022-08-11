# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

# def alphabetical(str):
#     list_of_str=[]
#     for char in str:
#         list_of_str.append(char)
#     sorted_list = sorted(str)
#     print(''.join(sorted_list))
# alphabetical("supercalifragilisticexpialidocious")

string = input ('Give me a string to alphabetize.\n')    
order = sorted(string)
combined = ''.join(order)
print(combined)