'''
Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

'''

def autoComplete(words,prefix):
    final=[]
    for word in words:
        n=len(prefix)
        if(prefix==word[:n]):
            final.append(word)
    return final
words=list(input().split(' '))
prefix=input()
print(autoComplete(words,prefix))