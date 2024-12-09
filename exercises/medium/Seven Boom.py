'''
Create a function that takes a list of numbers and return "Boom!" if the digit 7 appears in the list. Otherwise, return "there is no 7 in the list".

Examples
seven_boom([1, 2, 3, 4, 5, 6, 7]) ➞ "Boom!"
# 7 contains the number seven.

seven_boom([8, 6, 33, 100]) ➞ "there is no 7 in the list"
# None of the items contain 7 within them.

seven_boom([2, 55, 60, 97, 86]) ➞ "Boom!"
# 97 contains the number seven.
'''

def seven_boom(lst):
    newlist=[]
    for i in range(1,100):
        if '7' in str(i):
            newlist.append(i)

    for i in lst:
        if i in newlist:
            return 'Boom!'
    return "there is no 7 in the list"
