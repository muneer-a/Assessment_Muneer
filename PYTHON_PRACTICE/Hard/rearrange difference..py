'''
Given a number, return the difference between the maximum and minimum numbers that can be formed when the digits are rearranged.
'''

def rearranged_difference(num):
	str1=str(num)
	big=sorted(str1,reverse=True)
	small=sorted(str1)
	dif = int("".join(big))-int("".join(small))
	return dif
