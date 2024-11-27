'''
Create a function that takes a list of integers lst and sort the elements of the list by decreasing frequency of the elements.
If two elements have the same frequency, sort them by increasing value.
'''

from collections import Counter
def sort_freq(lst):
	counter1=Counter(lst)
	
	return sorted(lst,key=lambda x: (-counter1[x], x))
