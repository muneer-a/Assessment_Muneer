'''
Given three lists of integers: lst1, lst2, lst3, return the sum of integers which are common in all three lists.

Examples
sum_common([1, 2, 3], [5, 3, 2], [7, 3, 2]) ➞ 5
// 2 & 3 are common in all 3 lists.

sum_common([1, 2, 2, 3], [5, 3, 2, 2], [7, 3, 2, 2]) ➞ 7
// 2, 2 & 3 are common in all 3 lists.

sum_common([1], [1], [2]) ➞ 0
'''

def sum_common(lst1, lst2, lst3):
    set1=[]
    for element in set(lst1):
        count=min(lst1.count(element),lst2.count(element),lst3.count(element))
        set1.extend([element*count])
    
    
    return sum(set1)

print(sum_common([1, 2, 3], [5, 3, 2], [7, 3, 2]))
