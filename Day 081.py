'''
This problem was asked by Yelp.

Given a mapping of digits to letters (as in a phone number), and a digit string, return all possible letters the number could represent. You can assume each valid number in the mapping is a single digit.

For example if {“2”: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], …} then “23” should return [“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"].

'''
def mapping(alpnum,s):
    lists=[]
    if len(s) == 1:
        return alpnum[s[0]]
    for i in s:
        lists.append(alpnum[i])
    for i in range(1,len(lists)):
        l=[]
        for ele in lists[i-1]:
            for ele2 in lists[i]:
                l.append(ele+ele2)
        lists[i] = l
    return lists[-1]       
        
    
alpnum = {"2":['a','b','c'],"3":['d','e','f'],"4":['g','h','i'],"5":["j","k","l"],"6":["m","n","o"],"7":["p","q","r"],"8":["s","t","u"],"9":["x","y","z"]}
s=list(input())
print(mapping(alpnum,s))
s=list(input())
print(mapping(alpnum,s))