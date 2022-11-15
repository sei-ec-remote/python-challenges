# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.


def say_hello(name, greeting):
	name = input('What is your name? ')
	greeting = input ('How do you want to be greeted? ')
	print(f"{greeting}! {name}")

say_hello("name", "greeting")

def area_function(x, y):
	area = x * y
	print(f'Your area is: {area}')


user_x = input("What is the length of you square? ")
user_y = input("What is the width of you square? ")

area_function(int(user_x), int(user_y))


