def maxOfSubList(l,n):
    new_list =[]
    for i in range(len(l) - n + 1):
        new_list.append(max(l[i:i + n]))
    return new_list
    
      
l = list(map(int,input().split()))
n=int(input())  
print(maxOfSubList(l,n))