''''
This problem was asked by Google.

The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

You may also use a list or array to represent a set.

'''


from itertools import combinations
def powerset(list_ele):
    n = len(list_ele)
    for i in range(n+1):
        for l in combinations(list_ele,i):
            print(l)

elements = list(map(int,input().split()))
powerset(elements)
