'''
A Primorial is a product of the first n prime numbers (e.g. 2 x 3 x 5 = 30). 2, 3, 5, 7, 11, 13 are prime numbers. If n was 3, you'd multiply 2 x 3 x 5 = 30 or Primorial = 30.

Create a function that returns the Primorial of a number.

Examples
primorial(1) ➞ 2

primorial(2) ➞ 6

primorial(8) ➞ 9699690
'''

def primorial(n):
	def checkprime(num):
		if num==1:
			return False
		for i in range(2,num):
			if num%i==0:
				return False
		return True
	primelist=[]
	for i in range(1,1000):
	
		if checkprime(i):
			
			primelist.append(i)
	a=1
	
	for i in primelist[:n]:
		a*=i
	return a
    
print(primorial(3))
