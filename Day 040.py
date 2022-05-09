'''
This problem was asked by Google.

Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.

'''

def nonDuplicateInteger(l):
    unique = list(set(l))
    counts=[]
    for i in unique:
        count=l.count(i)
        counts.append(count)
    k=counts.index(1)
    return unique[k]
l = list(map(int,input().split()))
print(nonDuplicateInteger(l))
