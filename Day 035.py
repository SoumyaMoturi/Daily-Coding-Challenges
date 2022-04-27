def seperate(elements):
    unique_ele = set(elements)
    counts=[]
    new_list=[]
    for i in unique_ele:
        counts.append(elements.count(i))
    for i,j in enumerate(unique_ele):
        new_list.extend([j]*counts[i])
    return sorted(new_list,reverse=True)

elements = list(input().split())
print(seperate(elements))
