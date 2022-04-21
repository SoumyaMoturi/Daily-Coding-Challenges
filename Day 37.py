from itertools import combinations
def powerset(list_ele):
    n = len(list_ele)
    for i in range(n+1):
        for l in combinations(list_ele,i):
            print(l)

elements = list(map(int,input().split()))
powerset(elements)