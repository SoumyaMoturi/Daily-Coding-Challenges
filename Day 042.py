'''
This problem was asked by Google.

Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. If such a subset cannot be made, then return null.

Integers can appear more than once in the list. You may assume all numbers in the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.
'''


def subset_sum(elements,k):
    if not elements:
        return None
    elem = elements[0]
    if elem == k:
        return [elem]
 
    possible_subset = subset_sum(elements[1:], k - elem)
    if possible_subset is not None:
        return [elem] + possible_subset
    return subset_sum(elements[1:], k)
    
ele = list(map(int,input().split()))
k=int(input())
print(sorted(subset_sum(ele,k),reverse=True))
