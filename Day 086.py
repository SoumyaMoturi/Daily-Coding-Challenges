"""
This problem was asked by Google.

Given a string of parentheses, write a function to compute the minimum number of parentheses to be removed to make the string valid (i.e. each open parenthesis is eventually closed).

For example, given the string "()())()", you should return 1. Given the string ")(", you should return 2, since we must remove all of them.



"""
def unbalancedCount(s):
    l=[]
    c=0
    for i in s:
        if i=="(":
            l.append("(")
        elif not l and i==")" or i==")" and l[-1]!="(" :
            c+=1
        elif i==")" and l[-1]=="(":
            l.remove("(")
    if(l):
        c+=len(l)
    return c
    
s=input()
print(unbalancedCount(s))