'''
Write a function that returns the closest palindrome number to an integer. If two palindrome numbers tie in absolute distance, return the smaller number.

Examples
closest_palindrome(887) ➞ 888

closest_palindrome(100) ➞ 99
# 99 and 101 are equally distant, so we return the smaller palindrome.

closest_palindrome(888) ➞ 888

closest_palindrome(27) ➞ 22
Notes
If the number itself is a palindrome, return that number.
'''

def closest_palindrome(num):
    first=num
    def check(n):
    
        if str(num)==str(num)[::-1]:
            return True
        else:
            return False
    if check(num):
        return num
    while num:
        num+=1
        if check(num):
            max=num
            break
        

    while num:
        num-=1
        if check(num):
            min=num
            break

    if abs(first-max) < abs(first-min):
        return max
    elif abs(first-min) < abs(first-max):
        return min
    else:
        return min

closest_palindrome(100)
