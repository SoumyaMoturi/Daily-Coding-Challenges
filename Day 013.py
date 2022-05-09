'''
This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".


'''
def longest_substring_with_k_distinct_characters(s,k):
    longest_substring=''
    for i in range(0,len(s)):
        for j in range(i+1,len(s)+1):
            if len(set(s[i:j]))<=k and len(s[i:j]) > len(longest_substring):
                longest_substring = s[i:j]
    return longest_substring
    
s=input()
k=int(input())
print(longest_substring_with_k_distinct_characters(s,k))
    
    