def ProductOfaList(num_list):
    new_list=[]
    for k in range(len(num_list)):
        s=1
        for i,j in enumerate(num_list):
            if i!=k:
                s*=j
        new_list.append(s)
    return new_list
num_list=list(map(int,input().split()))
print(ProductOfaList(num_list))