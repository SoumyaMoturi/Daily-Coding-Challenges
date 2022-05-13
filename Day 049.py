'''
Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

Do this in O(N) time.

'''

#Kadane's algorithm
def MaxSum(arr):
    present_max=till_prev_max = 0
    for i in arr:
        present_max = max(i,present_max+i)
        till_prev_max = max(till_prev_max,present_max)
    return till_prev_max
        

if __name__ == "__main__":
    arr = list(map(int,input().split()))
    print(MaxSum(arr))