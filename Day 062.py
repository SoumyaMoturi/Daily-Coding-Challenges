'''
There is an N by M matrix of zeroes. Given N and M, write a function to count the number of ways of starting at the top-left corner and getting to the bottom-right corner. You can only move right or down.

For example, given a 2 by 2 matrix, you should return 2, since there are two ways to get to the bottom-right:



'''

def count_ways(n,m):
    if n==1 or m==1:
        return 1
    return count_ways(n-1,m)+count_ways(n,m-1)
n=int(input())
m=int(input())
print(count_ways(n,m))