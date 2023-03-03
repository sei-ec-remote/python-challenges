# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

prompt = "hello user, what's your name?"
answer = input(prompt)
alphabetized_name = ''.join(sorted(answer))
print(alphabetized_name)
