'''
This problem was asked by Google.

Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs come first, the Gs come second, and the Bs come last. You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].

'''

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
