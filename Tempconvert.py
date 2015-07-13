"""Temp converter"""

initques = input("Hi! Type 'C' for C to F conversion or type 'F' for F to C conversion: ").lower()

def functempc(x):
	z = int(x)*1.8+32
	return x + " degrees Celsius is " + str(z) + " degrees Fahrenheit."

def functempf(x):
	z = (int(x)-32) * 1.8
	return x + " degrees Fahrenheit is " + str(z) + " degrees Celsius."
	
def mainfunc(x):
	if x == "c":
		Cinput = input("What temperature in Celsius do you want to convert to Fahrenheit? ")
		return(functempc(Cinput))
	elif x == "f":
		Finput = input("What temperature in Fahrenheit do you want to convert to Celsius? ")
		return(functempf(Finput))
	else:
		return "Sorry, I don't understand. Please type 'C' for C to F conversion or 'F' for F to C conversion"
	
print(mainfunc(initques))