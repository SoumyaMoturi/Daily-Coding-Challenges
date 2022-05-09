'''
This problem was asked by Amazon.

An sorted array of integers was rotated an unknown number of times.

Given such an array, find the index of the element in the array in faster than linear time. If the element doesn't exist in the array, return null.

For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4 (the index of 8 in the array).

You can assume all the integers in the array are unique.
'''


def search(arr,x):
    start = 0
    end = len(arr)
    if x in arr:
        while start < end:
            mid = int((start+end)/2)
            if(arr[mid] == x):
                return mid
            elif(arr[mid] > x):
                end = mid
            else:
                start = mid
    else:
        return "Element not found!"
    
    
arr = list(map(int,input().split()))
x=int(input())
print(search(arr,x))
