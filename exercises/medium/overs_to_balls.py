'''
In cricket, an over consists of six deliveries a bowler bowls from one end. Create a function that takes the number of balls bowled by a bowler and 
calculates the number of overs and balls bowled by him/her. Return the value as a float, in the format overs.balls

Note:
The number following the decimal point represents the balls remaining after the last over. Therefore, it will only ever have a value of 1-5.
'''

def total_overs(balls):
	over=balls//6
	balance=balls%6
	
	return over+balance/10
