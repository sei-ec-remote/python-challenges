# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.
test_string = input("What should we sort? \n")
 
# printing original string
print("The original string : " + str(test_string))
 
# using join() + sorted()
# Sorting a string
res = ''.join(sorted(test_string))
     
# print result
print("String after sorting : " + str(res))

# the quick brown fox jumped over the lazy gorillas