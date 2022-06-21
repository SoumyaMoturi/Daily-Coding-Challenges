'''
This problem was asked by Google.

Given a word W and a string S, find all starting indices in S which are anagrams of W.

For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4.


'''
def startingIndices(s,w):
    l=[]
    for i in range(0,len(s)-1):
        #print(s[i:i+len(w)],end =" ")
        if w == s[i:i+len(w)] or w[::-1] == s[i:i+len(w)]:
            #print(s[i:i+len(w):-1],i)
            l.append(i)
    return l

s=input()
w=input()
print(startingIndices(s,w))

