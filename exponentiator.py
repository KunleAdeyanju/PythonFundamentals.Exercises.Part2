#the docstring is being displayed here
def exp(x,y) :
	"""
	Rasises the 1st number to the power of the second
	
	Args:
	x (int): The first number
	y (int): The seccond number

	Returns:
		int: x^y	
	"""
	return x ** y

def raise_to_fourth_power(x) :
	"""
	Rasises the input number to the 4th power
	"""
	return exp(x,4)

square = lambda b : exp(b,2)
cube = lambda x : exp(x,3)

#h = raise_to_fourth_power(2) 

print(square(2))
print(cube(2))
print(raise_to_fourth_power(2))
#print(h)

 
