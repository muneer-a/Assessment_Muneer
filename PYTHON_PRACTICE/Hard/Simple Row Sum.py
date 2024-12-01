'''
Imagine this triangle:

    1
   2 3
  4 5 6
 7 8 9 10
...
Create a function that takes a number n and returns the sum of all numbers in nth row.

Examples
row_sum(1) ➞ 1

row_sum(2) ➞ 5

row_sum(4) ➞ 34
Notes
1 <= N <= 1000
'''

def row_sum(n):
    #list1=[]
    #list2=[]
    def triangle(a):
        current=1
        list1=[]
        list2=[]
        for i in range(1,a+1):
            for j in range(i):
                list1.append(current+j)
            current+=i
            list2.append(tuple(list1))
            list1.clear()
        return list2
    list4=triangle(n)
    return sum(list4[n-1])

print(row_sum(5))
