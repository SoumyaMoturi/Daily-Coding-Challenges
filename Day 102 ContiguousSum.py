'''

This problem was asked by Lyft.

Given a list of integers and a number K, return which contiguous elements of the list sum to K.

For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return [2, 3, 4], since 2 + 3 + 4 = 9.

'''
            
def ContiguousSum(l,k):
    for i in range(len(l)):
        total = l[i]
        for j in range(i+1,len(l)):
            total+=l[j]
            if(total == k ):
                return l[i:j+1]
    
l = list(map(int,input().split()))
k = int(input())
print(ContiguousSum(l,k))
