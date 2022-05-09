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