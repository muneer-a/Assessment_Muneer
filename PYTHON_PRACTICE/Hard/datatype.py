'''
Given a function that accepts unlimited arguments, check and count how many data types are in those arguments. Finally return the total in a list.

List order is:

[int, str, bool, list, tuple, dictionary]
'''

def count_datatypes(*args):
	
	#list2=[int, str, bool, list, tuple, dictionary]
	list1=[0,0,0,0,0,0]
	for i in args:
		if type(i)==int:
			list1[0]+=1
		if type(i)==str:
			list1[1]+=1
		if type(i)==bool:
			list1[2]+=1
		if type(i)==list:
			list1[3]+=1
		if type(i)==tuple:
			list1[4]+=1
		if type(i)==dict:
			list1[5]+=1
	return list1
