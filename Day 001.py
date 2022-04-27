def AddTwoNumbers(numbers,k):
    for num in numbers:
        if k-num in numbers:
            return True
    return False
numbers=list(map(int,input().split()))
k=int(input())
l=[]
print(AddTwoNumbers(numbers,k))
