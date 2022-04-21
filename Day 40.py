def nonDuplicateInteger(l):
    unique = list(set(l))
    counts=[]
    for i in unique:
        count=l.count(i)
        counts.append(count)
    k=counts.index(1)
    return unique[k]
l = list(map(int,input().split()))
print(nonDuplicateInteger(l))