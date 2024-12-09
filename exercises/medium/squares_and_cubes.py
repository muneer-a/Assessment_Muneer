'''
Create a function that takes a list of two numbers and checks if the square root of the first number is equal to the cube root of the second number.

Examples
check_square_and_cube([4, 8]) ➞ True

check_square_and_cube([16, 48]) ➞ False

check_square_and_cube([9, 27]) ➞ True
Notes
Remember to return either True or False.
All lists contain two positive numbers
'''

def check_square_and_cube(lst):
    #import math
    a=lst[0]
    b=lst[1]

    return a**(1/2) == b**(1/3)

print(check_square_and_cube([25,125]))
