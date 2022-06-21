'''
Given a string and a set of characters, return the shortest substring containing all the characters in the set.

For example, given the string "figehaeci" and the set of characters {a, e, i}, you should return "aeci".

If there is no substring containing all the characters in the set, return null.
'''
def check(s):
    out=[]
    if(s[0:3] in 'aei'):
        return s[0:3]
    for i in range(len(s)-3):
        new_s = s[i]
        for j in range(i+1,len(s)):
            new_s+=s[j]
            #print(new_s)
            if 'a' in new_s and 'e' in new_s and 'i' in new_s:
                out.append(new_s)
    return min(out,key=len)
s=input()
print(check(s))