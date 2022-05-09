'''
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''

def ProductOfaList(num_list):
    new_list=[]
    for k in range(len(num_list)):
        s=1
        for i,j in enumerate(num_list):
            if i!=k:
                s*=j
        new_list.append(s)
    return new_list
num_list=list(map(int,input().split()))
print(ProductOfaList(num_list))
