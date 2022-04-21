
def MissingPositiveInteger(arr):
    small=1
    arr.sort()
    for i in range(len(arr)):
        if arr[i] > small:
            break
        if arr[i]==small:
            small+=1
    return small
    
arr=list(map(int,input().split()))
print(MissingPositiveInteger(arr))