'''
Python got drunk and the built-in functions str() and int() are acting odd:

You need to create two functions to substitute str() and int(). A function called int_to_str() that converts integers into strings and a function called str_to_int() that converts strings into integers.

'''

def int_to_str(num):
	newstr=''
	while num:
		rem=num%10
		num=num//10
		new=chr(rem+ord('0'))
		newstr=newstr+new
	return newstr[::-1]
		
def str_to_int(num):
	newnum=0
	for i in num:
		newnum=newnum*10 +(ord(i)-ord('0'))
	return newnum
