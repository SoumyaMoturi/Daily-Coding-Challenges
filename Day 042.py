def subset_sum(elements,k):
    if not elements:
        return None
    elem = elements[0]
    if elem == k:
        return [elem]
 
    possible_subset = subset_sum(elements[1:], k - elem)
    if possible_subset is not None:
        return [elem] + possible_subset
    return subset_sum(elements[1:], k)
    
ele = list(map(int,input().split()))
k=int(input())
print(sorted(subset_sum(ele,k),reverse=True))
