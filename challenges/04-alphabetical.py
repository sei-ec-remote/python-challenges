# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

# def aphabetize(str):
#     letters = [{
#         a :{},
#         b :{},
#         c :{},
#         d :{},
#         e :{},
#         f :{},
#         g :{},
#         h :{},
#         i :{},
#         j :{},
#         k :{},
#         l :{},
#         m :{},
#         n :{},
#         o :{},
#         p :{},
#         q :{},
#         r :{},
#         s :{},
#         t :{},
#         u :{},
#         v :{},
#         w :{},
#         x :{},
#         y :{},
#         z :{}
#         }]

#     for i in str:

# word = 'allackazasmmmo'
# for i in word:
#     print(sorted(i))

def alph_string(str):
    return ''.join(sorted(str))

print(alph_string('hamburgerlerajab'))

    