'''
This problem was asked by Pinterest.

Given an integer list where each number represents the number of hops you can make, determine whether you can reach to the last index starting at index 0.

For example, [2, 0, 1, 0] returns True while [1, 1, 0, 1] returns False.

'''
def canReachEnd(l):
    i=0
    while(i<len(l)-1):
        if(l[i] == 0 and i!=len(l)-1):
            return False
        i+= l[i]
        if(i == len(l)-1):
            return True
            
    return False
l=list(map(int,input().split(" ")))
print(canReachEnd(l))