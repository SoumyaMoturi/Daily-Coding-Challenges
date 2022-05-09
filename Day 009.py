'''
This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?

'''

def Max_Sum_subSequence(arr,n):
    if n == 0:
        return 0
 
    if n == 1:
        return arr[0]

    cache = [0] * n
 
    cache[0] = arr[0]
    cache[1] = max(arr[0], arr[1])

    for i in range(2, n):
        cache[i] = max(cache[i - 1], cache[i - 2] + arr[i])
 
        cache[i] = max(cache[i], arr[i])
    
    return cache[n-1]

 
arr = list(map(int,input().split()))
print(Max_Sum_subSequence(arr,len(arr)))
    
    
    