'''
This problem was asked by Amazon.

Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.

'''
def runLength(s):
    s+=''
    c=1
    new_s=''
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            c+=1 
        else:
            new_s+=s[i]+str(c)
            c=1
    return new_s
            
    
            
s=input()
print(runLength(s))