'''
This problem was asked by Facebook.

Given an array of integers, write a function to determine whether the array could become non-decreasing by modifying at most 1 element.

For example, given the array [10, 5, 7], you should return true, since we can modify the 10 into a 1 to make the array non-decreasing.

Given the array [10, 5, 1], you should return false, since we can't modify any one element to get a non-decreasing array.


'''
def non_decreasing_by_modifying(arr):
    c=0
    prev= arr[0]
    for i in range(1,len(arr)):
        if(arr[i] - prev < 0):
            c+=1
            if c > 1:
                return False
        prev = arr[i]
    return True
arr = list(map(int,input().split()))
print(non_decreasing_by_modifying(arr))
