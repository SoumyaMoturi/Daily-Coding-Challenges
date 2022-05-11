'''
This problem was asked by Facebook.

Given a list of integers, return the largest product that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.

You can assume the list has at least three integers.



'''

import itertools
def product(nums):
    p=1
    for i in nums:
        p*=i
    return p
    
def maxProduct(arr):
    arr.sort(reverse=True)
    if len(arr)>3:
        arr=[arr[0],arr[1],arr[2],arr[-2],arr[-1]]
    comb = list(set(itertools.combinations(arr,3)))
    m = 0
    ind = 0
    for i,nums in enumerate(comb):
        if product(nums) > m:
            m=product(nums)
            ind = i
    return m
    
arr=list(map(int,input().split()))
print(maxProduct(arr))