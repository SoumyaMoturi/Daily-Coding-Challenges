"""

This problem was asked by Google.

You are given an N by M 2D matrix of lowercase letters. Determine the minimum number of columns that can be removed to ensure that each row is ordered from top to bottom lexicographically. That is, the letter at each column is lexicographically later as you go down each row. It does not matter whether each row itself is ordered lexicographically.

For example, given the following table:

cba
daf
ghi



This is not ordered because of the a in the center. We can remove the second column to make it ordered:

"""




def lexicographical_order(arr,m,n):
    c=0
    for i in range(n):
        for j in range(1,m):
            if ord(arr[i][j]) < ord(arr[i][j-1]):
                c+=1
                break
    return c
        

n=int(input("Enter number of rows : "))
m=int(input("Enter number of columns : "))
arr = [[ch for ch in input("Enter the elemnets in row-wise order : ").split(" ")[:m]] for i in range(n)]
#arr = [list(input().split(" ")[:m]) for j in range(n)]
print(lexicographical_order(arr,m,n))