'''
Create a function that takes a country's name and its area as arguments and returns the area of the country's proportion of the total world's landmass.

The total world's landmass is 148,940,000 [Km^2]
Round the result to two decimal places.
'''

def area_of_country(name, area):
	percent=(area/148940000)*100
	return f"{name} is {round(percent,2)} of the total world's landmass"
