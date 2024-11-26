'''
Given an integer, create a function that returns the next prime. If the number is prime, return the number itself.
'''

def next_prime(num):
	def isprime(n):
		for i in range(2,n):
			if n%i==0:
				return False
		return True
	if num:
		
		i=0
		if isprime(num):
			return num
		else:
			while i==0:
				num=num+1
				if isprime(num):
					return num
