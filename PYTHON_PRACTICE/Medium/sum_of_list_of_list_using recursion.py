'''
Create a function that takes a list and returns the sum of all the items in that list.
An item in the list can be another list.
Try solving it in a recursive approach without using the built-in sum() function.
'''

def sum_list(lst):
	sum=0
	for element in lst:
		if type(element) == list:
			sum+=sum_list(element)
		else:
			sum+=element
	return sum
