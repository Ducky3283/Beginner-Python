import math

#Create function in case of later use
def conversions():
	#Ask if wants to convert from radians to degrees or vice versa
	choice = input("Do you want to convert degrees to radians or from radians to degrees? \n")
	#If the choice is from radians to degrees
	if choice == "radians to degrees":
		radians = input("How many radians do you wish to convert? \n")
		#Check if input is a float or integer
		if "." in radians:
			radians = float(radians)
		else:
			radians = int(radians)
			#Undertake the conversion
			degree_conversion = math.degrees(radians)
			#Output the conversion
			return(degree_conversion)

	#IF the choice is from degrees to radians
	elif choice == "degrees to radians":
		degrees = input("How many degrees do you wish to convert? \n")
		#Check if input is a float or integer
		if "." in degrees:
			degrees = float(degrees)
		else:
			degrees = int(degrees)
			#undertake the conversion
			radian_conversion = math.radians(degrees)
			#Output the conversion
			return(radian_conversion)
	#Runs if input is invalid
	else:
		return("That is not a conversion that is able to be undertaken")

#Output function
print(conversions())
