def greet(name):
	print("Hello, " + str(name) + ' welcome to the wonderful world of zipCode')

def name_input():
	print("Enter your name: ")
	x = input()
	return x

b = name_input()
greet(b)
