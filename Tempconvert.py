"""Temp converter"""

initques = raw_input("Hi! Type 'C' for C to F conversion or type 'F' for F to C conversion: ").lower()

def functempc(x):
	z = int(int(x)*1.8+32)
	return x + " degrees Celsius is " + str(z) + " degrees Fahrenheit."

def functempf(x):
	z = int(((int(x)-32) * 5) /9)
	return x + " degrees Fahrenheit is " + str(z) + " degrees Celsius."
	
def mainfunc(x):
	if x == "c":
		Cinput = raw_input("What temperature in Celsius do you want to convert to Fahrenheit? ")
		return(functempc(Cinput))
	elif x == "f":
		Finput = raw_input("What temperature in Fahrenheit do you want to convert to Celsius? ")
		return(functempf(Finput))
	else:
		return "Sorry, I don't understand. Please type 'C' for C to F conversion or 'F' for F to C conversion"
	
print(mainfunc(initques))

restart = raw_input("Type 'T' to convert another temperature or press Enter to quit: ").lower()
class restarting:
	def counterfunc(x):
		if x=="t":
			i = 0
			i = i + 1	
			return i
	print(counterfunc(restart))
	def restartfunc(x):
		if x == "t":
			initques = raw_input("Type 'C' for C to F conversion or type 'F' for F to C conversion: ").lower()
			return mainfunc(initques)
		else:
			return "Bye! "

	while restart == "t" and i >= 1:
		restart = raw_input("Type 'T' to convert another temperature or press Enter to quit: ").lower()
		print(restartfunc(restart))
