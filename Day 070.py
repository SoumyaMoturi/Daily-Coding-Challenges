'''

A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.

'''
def perfectNumber(n):
    num = 18
    while(n > 0):
        num+=1
        if  sum([int(i) for i in str(num)]) == 10:
            n-=1
    return num
        
    
n=int(input())
print(perfectNumber(n))